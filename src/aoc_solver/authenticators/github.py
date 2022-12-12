import keyring
import os
import pwd
import requests
import typing

from getpass import getpass

from aoc_solver.html_parsers import GitHubLoginHTMLParser

CLIENT_ID = "7bb0a7ec13388aa67963"
CALLBACK_URL = "https://adventofcode.com/auth/github/callback"
OAUTH_QUERY_PARAMS = f"client_id={CLIENT_ID}&duration=temporary&redirect_uri={CALLBACK_URL}&response_type=code&scope=&state=x"
AUTHORIZE_ENDPOINT = "https://github.com/login/oauth/authorize"
OAUTH_AUTHORIZE_URL = f"{AUTHORIZE_ENDPOINT}?{OAUTH_QUERY_PARAMS}"
SESSION_URL = "https://github.com/session"


def login(username: str) -> requests.Session:
    """Logs into Advent of Code via GitHub

    Creates a requests Session logged into Advent of Code using GitHub as an OAuth provider.
        NOTE: Assumes the user has multi-factor authentication enabled

    Args:
        username: GitHub login/username

    Return:
        Advent of Code-authentication requests Session

    Raises:
        HTTPError for any request errors

    """
    session = requests.Session()

    login_payload = _build_login_payload(session=session, login=username)
    session_response = session.post(url=SESSION_URL, data=login_payload)
    session_response.raise_for_status()
    del login_payload

    mfa_payload = _build_mfa_payload(mfa_page=session_response.text)
    mfa_response = session.post(url=session_response.url, data=mfa_payload)
    mfa_response.raise_for_status()
    del mfa_payload

    return session


def _build_login_payload(session: requests.Session, login: str) -> typing.Dict[str, typing.Any]:
    authorize_response = session.get(url=OAUTH_AUTHORIZE_URL)
    authorize_response.raise_for_status()

    parser = _parse_github_page(data=authorize_response.text)

    return {
        "login": login,
        "password": keyring.get_password(service_name="github", username=pwd.getpwuid(os.getuid()).pw_name),
        "client_id": CLIENT_ID,
        "commit": "Sign in",
        "authenticity_token": parser.authenticity_token,
        "return_to": parser.return_to,
        parser.required_field: "",
        "timestamp": parser.timestamp,
        "timestamp_secret": parser.timestamp_secret,
    }


def _build_mfa_payload(mfa_page: str) -> typing.Dict[str, typing.Any]:
    parser = _parse_github_page(data=mfa_page)

    return {
        "authenticity_token": parser.authenticity_token,
        "otp": getpass(prompt="Enter GitHub OTP: "),
    }


def _parse_github_page(data: str) -> GitHubLoginHTMLParser:
    parser = GitHubLoginHTMLParser()
    parser.feed(data=data)
    parser.close()

    return parser
