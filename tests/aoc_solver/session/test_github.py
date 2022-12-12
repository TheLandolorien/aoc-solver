import pytest

from unittest.mock import patch
from selenium.common.exceptions import WebDriverException

from aoc_solver.session import github


@patch.object(github, "Firefox", side_effect=WebDriverException)
def test_authenticate_raises_for_missing_web_driver(mock_exception):
    with pytest.raises(ImportError) as ex:
        github.authenticate()

    assert "Unable to open browser for GitHub authentication." in str(ex.value), "should provide reason for WebDriverException"
    mock_exception.assert_called_once()


@patch("aoc_solver.session.github.Firefox")
def test_authenticate_returns_session_cookie(mock_browser):
    mock_browser.return_value.current_url = github.AOC_URL
    mock_browser.return_value.get_cookie.return_value = {"value": "foo"}
    github.authenticate()

    mock_browser.return_value.get.assert_called_once_with(url=github.OAUTH_AUTHORIZE_URL)
    mock_browser.return_value.get_cookie.assert_called_once_with(name="session")
    mock_browser.return_value.quit.assert_called_once()
