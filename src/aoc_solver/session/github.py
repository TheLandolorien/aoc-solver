import typing

from selenium.common.exceptions import WebDriverException
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


AOC_URL = "https://adventofcode.com"
CALLBACK_URL = f"{AOC_URL}/auth/github/callback"
CLIENT_ID = "b0b9e4e723fdb8841400"  # Be sure to pull the latest client ID
OAUTH_QUERY_PARAMS = f"client_id={CLIENT_ID}&duration=temporary&redirect_uri={CALLBACK_URL}&response_type=code&scope=&state=x"
AUTHORIZE_ENDPOINT = "https://github.com/login/oauth/authorize"
OAUTH_AUTHORIZE_URL = f"{AUTHORIZE_ENDPOINT}?{OAUTH_QUERY_PARAMS}"


def authenticate() -> typing.Union[str, None]:
    """Creates an Advent of Code session via GitHub OAuth"""
    browser = _load_webdriver()

    browser.get(url=OAUTH_AUTHORIZE_URL)
    WebDriverWait(driver=browser, timeout=60).until(
        method=expected_conditions.url_matches(pattern=AOC_URL)
    )

    session_cookie = browser.get_cookie(name="session").get("value")
    browser.quit()

    return session_cookie


def _load_webdriver() -> Firefox:
    try:
        browser = Firefox()
    except WebDriverException as ex:
        error_message = "Unable to open browser for GitHub authentication. Ensure geckodriver for Firefox is downloaded."
        additional_info = "See: https://github.com/mozilla/geckodriver/releases"
        raise ImportError(f"{error_message}\n{additional_info}") from ex

    return browser
