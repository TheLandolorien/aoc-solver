import pytest

from unittest.mock import mock_open, patch

from aoc_solver.authenticators import utilities


@pytest.mark.parametrize(
    "session",
    [
        (None),
        (""),
        ("foo"),
    ],
)
@patch("builtins.open", new_callable=mock_open, read_data="{}")
def test_store_session_cookie_in_empty_config_files(mock_open, session):
    utilities.store_session_cookie(session=session)
    jsonified_session = f'"{session}"' if session is not None else "null"

    mock_open.assert_called_once_with(file=utilities.CONFIG_FILE_PATH, mode="r+")
    mock_open().read.assert_called_once()
    mock_open().write.assert_any_call("{")
    mock_open().write.assert_any_call('"AOC_SESSION"')
    mock_open().write.assert_any_call(": ")
    mock_open().write.assert_any_call(f"{jsonified_session}")
    mock_open().write.assert_any_call("}")


@pytest.mark.parametrize(
    "session",
    [
        (None),
        (""),
        ("foo"),
    ],
)
@patch("builtins.open", new_callable=mock_open, read_data='{"test": "bar"}')
def test_store_session_cookie_in_existing_config_files(mock_open, session):
    utilities.store_session_cookie(session=session)
    jsonified_session = f'"{session}"' if session is not None else "null"

    mock_open.assert_called_once_with(file=utilities.CONFIG_FILE_PATH, mode="r+")
    mock_open().read.assert_called_once()
    mock_open().write.assert_any_call("{")
    mock_open().write.assert_any_call('"test"')
    mock_open().write.assert_any_call(": ")
    mock_open().write.assert_any_call('"bar"')
    mock_open().write.assert_any_call(", ")
    mock_open().write.assert_any_call('"AOC_SESSION"')
    mock_open().write.assert_any_call(": ")
    mock_open().write.assert_any_call(f"{jsonified_session}")
    mock_open().write.assert_any_call("}")


@pytest.mark.parametrize(
    "session",
    [
        (None),
        (""),
        ("foo"),
    ],
)
@patch("builtins.open", new_callable=mock_open, read_data='{"AOC_SESSION": "bar"}')
def test_store_session_cookie_overwrite_existing_session_value(mock_open, session):
    utilities.store_session_cookie(session=session)
    jsonified_session = f'"{session}"' if session is not None else "null"

    mock_open.assert_called_once_with(file=utilities.CONFIG_FILE_PATH, mode="r+")
    mock_open().read.assert_called_once()
    mock_open().write.assert_any_call("{")
    mock_open().write.assert_any_call('"AOC_SESSION"')
    mock_open().write.assert_any_call(": ")
    mock_open().write.assert_any_call(f"{jsonified_session}")
    mock_open().write.assert_any_call("}")


@patch("builtins.open", new_callable=mock_open, read_data='{"AOC_SESSION": "foo"}')
def test_load_session_cookie_extracts_populated_session(mock_open):
    assert utilities.load_session_cookie() == "foo", f"should load stored session"

    mock_open.assert_called_once_with(file=utilities.CONFIG_FILE_PATH, mode="r")
    mock_open().read.assert_called_once()


@patch("builtins.open", new_callable=mock_open, read_data='{"AOC_SESSION": ""}')
def test_load_session_cookie_extracts_blank_session(mock_open):
    assert utilities.load_session_cookie() == "", f"should load stored blank session"

    mock_open.assert_called_once_with(file=utilities.CONFIG_FILE_PATH, mode="r")
    mock_open().read.assert_called_once()


@patch("builtins.open", new_callable=mock_open, read_data='{"AOC_SESSION": null}')
def test_load_session_cookie_extracts_existing_session(mock_open):
    assert utilities.load_session_cookie() == None, f"should load stored session"

    mock_open.assert_called_once_with(file=utilities.CONFIG_FILE_PATH, mode="r")
    mock_open().read.assert_called_once()
