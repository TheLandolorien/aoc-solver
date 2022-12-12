import pytest

from unittest.mock import patch

from aoc_solver import puzzle_manager


@pytest.fixture
def mock_session():
    with patch("aoc_solver.puzzle_manager.requests.Session") as MockSession:
        yield MockSession.return_value


@pytest.mark.parametrize("auth_provider", [(None), ("github"), ("reddit")])
@patch("aoc_solver.puzzle_manager.authenticator")
def test_get_puzzle_input_authenicates_using_session_cookie(mock_authenticator, mock_session, auth_provider):
    expected_auth_provider = auth_provider if auth_provider else "github"
    additional_args = {"auth_provider": auth_provider} if auth_provider else {}

    puzzle_input = puzzle_manager.get_puzzle_input(year=2022, day=12, **additional_args)

    assert puzzle_input == mock_session.get.return_value.text, f"should return retrieved puzzle input using {expected_auth_provider} provider"
    mock_authenticator.authenticate.assert_called_once_with(provider=expected_auth_provider)
    mock_session.cookies.set.assert_called_once_with(name="session", value=mock_authenticator.authenticate.return_value)
    mock_session.get.assert_called_once_with(url=f"https://adventofcode.com/2022/day/12/input")
    mock_session.get.return_value.raise_for_status.assert_called_once()
