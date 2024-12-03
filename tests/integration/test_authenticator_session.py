import pytest

from unittest.mock import patch

from aoc_solver.session import authenticator
from aoc_solver.session.github import AOC_URL


@pytest.fixture
def mock_session():
    with patch("aoc_solver.session.authenticator.requests.Session") as MockSession:
        yield MockSession.return_value


@pytest.fixture
def mock_config_file(tmp_path):
    return tmp_path / ".env"


@patch("selenium.webdriver.Firefox")
def test_authenticate_creates_new_config(mock_browser, mock_session, mock_config_file):
    mock_browser.return_value.current_url = AOC_URL
    mock_browser.return_value.get_cookie.return_value = {"value": "foo"}
    mock_session.get.return_value.status_code == 200

    authenticator.CONFIG_FILE_PATH = mock_config_file
    authenticator.authenticate()

    assert mock_config_file.read_text() == '{"AOC_SESSION": "foo"}', "should create new config"


@patch("selenium.webdriver.Firefox")
def test_authenticate_appends_to_existing_config(mock_browser, mock_session, mock_config_file):
    mock_browser.return_value.current_url = AOC_URL
    mock_browser.return_value.get_cookie.return_value = {"value": "foo"}
    mock_session.get.return_value.status_code == 200
    mock_config_file.write_text('{"existing_key": "existing_value"}')

    authenticator.CONFIG_FILE_PATH = mock_config_file
    authenticator.authenticate()

    assert (
        mock_config_file.read_text() == '{"existing_key": "existing_value", "AOC_SESSION": "foo"}'
    ), "should extend existing config"


@patch("selenium.webdriver.Firefox")
def test_authenticate_overwrite_existing_session_cookie(
    mock_browser, mock_session, mock_config_file
):
    mock_browser.return_value.current_url = AOC_URL
    mock_browser.return_value.get_cookie.return_value = {"value": "bar"}
    mock_session.get.return_value.status_code == 200
    mock_config_file.write_text('{"AOC_SESSION": "foo"}')

    authenticator.CONFIG_FILE_PATH = mock_config_file
    authenticator.authenticate()

    assert (
        mock_config_file.read_text() == '{"AOC_SESSION": "bar"}'
    ), "should overwrite existing session"
