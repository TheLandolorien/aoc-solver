import pytest

from unittest.mock import patch

from aoc_solver.authenticators import github


@pytest.fixture
def mock_session():
    with patch("aoc_solver.authenticators.github.requests.Session") as MockSession:
        yield MockSession.return_value


@pytest.fixture
def mock_parser():
    with patch("aoc_solver.authenticators.github.GitHubLoginHTMLParser") as MockParser:
        yield MockParser.return_value


@patch("aoc_solver.authenticators.github.os")
@patch("aoc_solver.authenticators.github.pwd")
@patch("aoc_solver.authenticators.github.keyring")
@patch("aoc_solver.authenticators.github.getpass")
def test_login_creates_logged_in_session(mock_getpass, mock_keyring, mock_pwd, mock_os, mock_session, mock_parser):
    session = github.login(username="foo")

    assert session == mock_session, "should return requests session"
    mock_session.get.assert_called_once_with(url=github.OAUTH_AUTHORIZE_URL)
    mock_session.get.return_value.raise_for_status.assert_called_once()

    mock_parser.feed.assert_any_call(data=mock_session.get.return_value.text)

    mock_os.getuid.assert_called_once()
    mock_pwd.getpwuid.assert_called_once_with(mock_os.getuid.return_value)
    mock_keyring.get_password.assert_called_once_with(service_name="github", username=mock_pwd.getpwuid.return_value.pw_name)
    mock_session.post.assert_any_call(
        url=github.SESSION_URL,
        data={
            "login": "foo",
            "password": mock_keyring.get_password.return_value,
            "client_id": github.CLIENT_ID,
            "commit": "Sign in",
            "authenticity_token": mock_parser.authenticity_token,
            "return_to": mock_parser.return_to,
            mock_parser.required_field: "",
            "timestamp": mock_parser.timestamp,
            "timestamp_secret": mock_parser.timestamp_secret,
        },
    )
    assert mock_session.post.return_value.raise_for_status.call_count == 2, "should check status code errors for both POST requests"

    mock_parser.feed.assert_any_call(data=mock_session.post.return_value.text)
    assert mock_parser.close.call_count == 2, "should parse HTML data 2 times"

    mock_getpass.assert_called_once_with(prompt="Enter GitHub OTP: ")
    mock_session.post.assert_any_call(
        url=mock_session.post.return_value.url,
        data={
            "authenticity_token": mock_parser.authenticity_token,
            "otp": mock_getpass.return_value,
        },
    )
