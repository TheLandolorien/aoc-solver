import pytest

from unittest.mock import mock_open, patch

from aoc_solver.session import authenticator


@pytest.fixture
def mock_session():
    with patch("aoc_solver.session.authenticator.requests.Session") as MockSession:
        yield MockSession.return_value


@patch("aoc_solver.session.authenticator.os")
@patch("builtins.open", new_callable=mock_open, read_data='{"AOC_SESSION": "foo"}')
def test_authenticate_uses_valid_stored_session_cookie_by_default(mock_open, mock_os, mock_session):
    mock_os.path.isfile.return_value = True
    mock_session.get.return_value.status_code = 200

    assert authenticator.authenticate() == "foo", f"should load stored session"

    mock_os.path.isfile.assert_called_once_with(path=authenticator.CONFIG_FILE_PATH)
    mock_open.assert_called_once_with(file=authenticator.CONFIG_FILE_PATH, mode="r")
    mock_open().read.assert_called_once()
    mock_session.cookies.set.assert_called_once_with(name="session", value="foo")
    mock_session.get.assert_called_once_with(
        url="https://adventofcode.com/settings", allow_redirects=False
    )


@pytest.mark.parametrize("provider", [(None), ("github"), ("reddit")])
@patch("aoc_solver.session.authenticator.import_utils")
@patch("aoc_solver.session.authenticator.os")
@patch("builtins.open", new_callable=mock_open)
def test_authenticate_creates_new_session_cookie_if_missing(
    mock_open, mock_os, mock_importer, mock_session, provider
):
    mock_os.path.isfile.return_value = False
    mock_importer.module_from_spec.return_value.authenticate.return_value = "foo"

    expected_provider = provider
    if not expected_provider:
        expected_provider = "github"
        session_cookie = authenticator.authenticate()
    else:
        session_cookie = authenticator.authenticate(provider=expected_provider)

    assert session_cookie == "foo", f"should retrieve new session for {expected_provider}"

    mock_importer.find_spec.assert_called_once_with(name=f"aoc_solver.session.{expected_provider}")
    mock_importer.module_from_spec.assert_called_once_with(
        spec=mock_importer.find_spec.return_value
    )
    mock_importer.find_spec.return_value.loader.exec_module.assert_called_once_with(
        module=mock_importer.module_from_spec.return_value
    )
    mock_importer.module_from_spec.return_value.authenticate.assert_called_once()
    mock_open.assert_called_once_with(file=authenticator.CONFIG_FILE_PATH, mode="w")
    mock_open.return_value.write.assert_any_call("{")
    mock_open.return_value.write.assert_any_call('"AOC_SESSION"')
    mock_open.return_value.write.assert_any_call(": ")
    mock_open.return_value.write.assert_any_call('"foo"')
    mock_open.return_value.write.assert_any_call("}")
    mock_session.assert_not_called()


@pytest.mark.parametrize("provider", [(None), ("github"), ("reddit")])
@patch("aoc_solver.session.authenticator.import_utils")
@patch("aoc_solver.session.authenticator.os")
@patch("builtins.open", new_callable=mock_open, read_data='{"AOC_SESSION": "bar"}')
def test_authenticate_refreshes_invalid_session_cookie(
    mock_open, mock_os, mock_importer, mock_session, provider
):
    mock_os.path.isfile.return_value = True
    mock_importer.module_from_spec.return_value.authenticate.return_value = "foo"
    mock_session.get.return_value.status_code = 500

    expected_provider = provider
    if not expected_provider:
        expected_provider = "github"
        session_cookie = authenticator.authenticate()
    else:
        session_cookie = authenticator.authenticate(provider=expected_provider)

    assert session_cookie == "foo", f"should retrieve new session for {expected_provider}"

    mock_importer.find_spec.assert_called_once_with(name=f"aoc_solver.session.{expected_provider}")
    mock_importer.module_from_spec.assert_called_once_with(
        spec=mock_importer.find_spec.return_value
    )
    mock_importer.find_spec.return_value.loader.exec_module.assert_called_once_with(
        module=mock_importer.module_from_spec.return_value
    )
    mock_importer.module_from_spec.return_value.authenticate.assert_called_once()
    mock_session.cookies.set.assert_called_once_with(name="session", value="bar")
    mock_session.get.assert_called_once_with(
        url="https://adventofcode.com/settings", allow_redirects=False
    )
    mock_open.assert_any_call(file=authenticator.CONFIG_FILE_PATH, mode="w")
    mock_open.assert_any_call(file=authenticator.CONFIG_FILE_PATH, mode="r")
    mock_open.return_value.write.assert_any_call("{")
    mock_open.return_value.write.assert_any_call('"AOC_SESSION"')
    mock_open.return_value.write.assert_any_call(": ")
    mock_open.return_value.write.assert_any_call('"foo"')
    mock_open.return_value.write.assert_any_call("}")


@patch("aoc_solver.session.authenticator.import_utils")
@patch("aoc_solver.session.authenticator.os")
def test_authenticate_raises_for_unattainable_session_cookie(mock_os, mock_importer):
    mock_os.path.isfile.return_value = False
    mock_importer.module_from_spec.return_value.authenticate.return_value = None

    with pytest.raises(AttributeError) as err:
        authenticator.authenticate()

    assert (
        str(err.value) == "Unable to authenticate Advent of Code session with github"
    ), "should provide reason for AttributeError"
    mock_os.path.isfile.assert_called_once_with(path=authenticator.CONFIG_FILE_PATH)
    mock_importer.find_spec.assert_called_once_with(name=f"aoc_solver.session.github")
    mock_importer.module_from_spec.assert_called_once_with(
        spec=mock_importer.find_spec.return_value
    )
    mock_importer.find_spec.return_value.loader.exec_module.assert_called_once_with(
        module=mock_importer.module_from_spec.return_value
    )
    mock_importer.module_from_spec.return_value.authenticate.assert_called_once()
