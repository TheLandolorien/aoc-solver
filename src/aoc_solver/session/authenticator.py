import json
import os
import requests
import typing

from importlib import util as import_utils
from types import ModuleType


PACKAGE_DIRECTORY, NAMESPACE = os.path.split(os.path.dirname(__file__))
SRC_DIRECTORY, PACKAGE_NAME = os.path.split(PACKAGE_DIRECTORY)
CONFIG_FILE_PATH = os.path.join(os.path.dirname(SRC_DIRECTORY), ".env")
SESSION_KEY = "AOC_SESSION"


def _is_valid_session(session_cookie: str) -> bool:
    session = requests.Session()
    session.cookies.set(name="session", value=session_cookie)

    response = session.get(url="https://adventofcode.com/settings", allow_redirects=False)
    session.close()

    return response.status_code == 200


def _load_authenticator_module(provider: str) -> ModuleType:
    auth_spec = import_utils.find_spec(name=".".join([PACKAGE_NAME, NAMESPACE, provider]))
    auth_module = import_utils.module_from_spec(spec=auth_spec)
    auth_spec.loader.exec_module(module=auth_module)

    return auth_module


def _load_existing_config() -> typing.Dict[str, typing.Any]:
    config = {}
    if os.path.isfile(path=CONFIG_FILE_PATH):
        with open(file=CONFIG_FILE_PATH, mode="r") as config_file:
            config = json.load(config_file)

    return config


def _load_session_cookie() -> typing.Union[str, None]:
    config = _load_existing_config()

    return config.get(SESSION_KEY)


def _store_session_cookie(session_cookie: typing.Optional[str] = None) -> None:
    config = _load_existing_config()
    config[SESSION_KEY] = session_cookie

    with open(file=CONFIG_FILE_PATH, mode="w") as config_file:
        json.dump(config, config_file)


def authenticate(provider: str = "github") -> str:
    """Authenticate with Advent of Code with specified OAuth provider

    If no session exists or session is expired, complete authentication
    in browser and store session locally.

    Args:
        provider: Name of the OAuth provider [github] (Default: github)

    Returns:
        Authenticated session cookie

    Raises:
        AttributeError if unable to authenticate via OAuth provider
    """
    session_cookie = _load_session_cookie()

    if not session_cookie or not _is_valid_session(session_cookie=session_cookie):
        authenticator = _load_authenticator_module(provider=provider)
        session_cookie = authenticator.authenticate()

        if session_cookie:
            _store_session_cookie(session_cookie=session_cookie)

    if not session_cookie:
        raise AttributeError(f"Unable to authenticate Advent of Code session with {provider}")

    return session_cookie
