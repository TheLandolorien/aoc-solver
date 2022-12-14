import pytest
from unittest.mock import DEFAULT, patch

from datetime import datetime
from aoc_solver.object_types import PuzzleMetadata

from aoc_solver import solver


@pytest.mark.parametrize(
    "scenario,invalid_args,additional_error_message",
    [
        ("raise when missing puzzle day", ["solve", "2015"], ""),
        ("raise when given too many values", ["solve", "2015", "1", "foo"], ""),
        ("raise when given invalid year", ["solve", "ABCD", "1"], "\nInvalid value ABCD for format %Y"),
        ("raise when given invalid day", ["solve", "2015", "Z"], "\nInvalid value Z for format %d"),
    ],
)
def test_solve_with_invalid_arguments(scenario, invalid_args, additional_error_message):
    sys_patch = patch("sys.argv", invalid_args)

    sys_patch.start()
    with pytest.raises(ValueError) as err:
        solver.solve()
    sys_patch.stop()

    print(err.value)
    assert str(err.value) == f"Usage: poetry run solve <YEAR> <DAY_NUMBER>{additional_error_message}", f"should {scenario}"


@pytest.mark.parametrize(
    "scenario,now,cli_args,expected_dates",
    [
        ("latest solution available during active event", datetime(2022, 12, 1), ["solve"], (2022, 1)),
        ("latest solution available immediately after event", datetime(2022, 12, 26), ["solve"], (2022, 25)),
        ("latest solution available from previous event", datetime(2023, 11, 30), ["solve"], (2022, 25)),
        ("previous solution given puzzle info", None, ["solve", "2015", "1"], (2015, 1)),
    ],
)
@patch("aoc_solver.solver.datetime")
@patch("aoc_solver.solver.puzzle_manager")
@patch("aoc_solver.solver.utilities")
def test_solve_existing_puzzle_with_valid_arguments(mock_utilities, mock_puzzle_manager, mock_datetime, scenario, now, cli_args, expected_dates):
    mock_datetime.now.return_value = now
    sys_patch = patch("sys.argv", cli_args)

    sys_patch.start()
    solution = solver.solve()
    sys_patch.stop()

    assert solution is not None, f"should run {scenario}"

    year, day = expected_dates

    mock_utilities.load_module.assert_called_once_with(relative_module_name=f"{year}.day_{str(day).zfill(2)}")
    mock_puzzle_manager.read_puzzle_input.assert_called_once_with(year=year, day=day)


@pytest.mark.parametrize(
    "scenario,mock_now,cli_args,expected_dates",
    [
        ("latest solution available during active event", datetime(2022, 12, 1), ["solve"], (2022, 1)),
        ("latest solution available immediately after event", datetime(2022, 12, 26), ["solve"], (2022, 25)),
        ("latest solution available from previous event", datetime(2023, 11, 30), ["solve"], (2022, 25)),
        ("previous solution given puzzle info", None, ["solve", "2015", "1"], (2015, 1)),
    ],
)
@patch("aoc_solver.solver.datetime")
@patch("aoc_solver.solver.puzzle_manager")
@patch("aoc_solver.solver.utilities")
def test_solve_missing_puzzle_with_valid_arguments(mock_utilities, mock_puzzle_manager, mock_datetime, scenario, mock_now, cli_args, expected_dates):
    mock_datetime.now.return_value = mock_now
    mock_utilities.load_module.side_effect = [None, DEFAULT]

    sys_patch = patch("sys.argv", cli_args)

    sys_patch.start()
    solution = solver.solve()
    sys_patch.stop()

    assert solution is not None, f"should run {scenario}"

    year, day = expected_dates
    mock_utilities.load_module.assert_any_call(relative_module_name=f"{year}.day_{str(day).zfill(2)}")
    assert mock_utilities.load_module.call_count == 2, "should reload module after creating resources"
    mock_puzzle_manager.read_puzzle_input.assert_called_once_with(year=year, day=day)
