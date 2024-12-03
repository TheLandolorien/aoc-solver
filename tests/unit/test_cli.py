import pytest
from unittest.mock import patch, Mock

from datetime import datetime


from aoc_solver import cli


@pytest.fixture
def mock_puzzle_module():
    return Mock(**{"solve.return_value": [None, None]})


@pytest.mark.parametrize(
    "mock_now,expected_year,expected_day",
    [
        (
            datetime(2018, 12, 13),
            (2018, "should use provided year during December"),
            (13, "should use provided day between 1 - 25"),
        ),
        (
            datetime(2020, 12, 26),
            (2020, "should use provided year during December"),
            (25, "should use not use day > 25"),
        ),
        (
            datetime(2015, 4, 1),
            (2014, "should use previous year if not December"),
            (25, "should use 25 if not December"),
        ),
    ],
)
@patch("aoc_solver.cli.datetime")
def test_get_max_puzzle_date(mock_datetime, mock_now, expected_year, expected_day):
    mock_datetime.now.return_value = mock_now

    year, day = cli._get_max_puzzle_date()

    assert year == expected_year[0], expected_year[1]
    assert day == expected_day[0], expected_day[1]


@patch("aoc_solver.cli.puzzle_manager")
@patch("aoc_solver.cli.utilities")
def test_load_puzzle_loads_existing_resources(mock_utilities, mock_puzzle_manager):
    mock_utilities.load_module.return_value = "foo"

    cli._load_puzzle(year=1, day=1)

    mock_utilities.load_module.assert_called_once_with(year=1, day=1)
    mock_puzzle_manager.create_puzzle_resources.assert_not_called()


@patch("aoc_solver.cli.puzzle_manager")
@patch("aoc_solver.cli.utilities")
def test_load_puzzle_creates_resources_for_missing_puzzle(mock_utilities, mock_puzzle_manager):
    mock_utilities.load_module.return_value = None

    cli._load_puzzle(year=1, day=1)

    mock_utilities.load_module.assert_called == 2, "should call load module again after creating resources"
    mock_utilities.load_module.assert_called_with(year=1, day=1)
    mock_puzzle_manager.create_puzzle_resources.assert_called_once_with(year=1, day=1)


@pytest.mark.parametrize(
    "mock_args,error_message",
    [
        (["--date"], "argument --date: expected 2 arguments"),
        (["--date", "2014", "14"], "Invalid year 2014: Advent of Code began in 2015"),
        (["--date", "2019", "27"], "Invalid day 27: Advent of Code is only 25 days per year"),
        (["--date", "2020", "1"], "Invalid puzzle 2020 day 1: Not yet released"),
    ],
)
@patch("aoc_solver.cli.datetime")
@patch("aoc_solver.cli.argparse._sys.argv")
def test_parse_puzzle_date_raises_for_invalid_dates(
    mock_argv,
    mock_datetime,
    mock_args,
    error_message,
    capsys,
):
    mock_argv.__getitem__.return_value = mock_args
    mock_datetime.now.return_value = datetime(2020, 11, 30)

    with pytest.raises(SystemExit):
        cli._parse_puzzle_date()
        assert False, "should raise SystemExit for invalid dates"

    _, err = capsys.readouterr()
    assert err == (
        "usage: aoc-solver [-h] [--date year day]\n" f"aoc-solver: error: {error_message}\n"
    ), f"should provide usage on exit due to invalid dates"


@pytest.mark.parametrize(
    "mock_args,expected_date",
    [
        ([], (2019, 25)),
        (["--date", "2017", "4"], (2017, 4)),
    ],
)
@patch("aoc_solver.cli.datetime")
@patch("aoc_solver.cli.argparse._sys.argv")
def test_parse_puzzle_date(mock_argv, mock_datetime, mock_args, expected_date):
    mock_argv.__getitem__.return_value = mock_args
    mock_datetime.now.return_value = datetime(2020, 11, 30)

    year, day = cli._parse_puzzle_date()

    expected_year, expected_day = expected_date
    assert year == expected_year, "should parse valid year to int"
    assert day == expected_day, "should parse valid day to int"


@patch("aoc_solver.cli.datetime")
@patch("aoc_solver.cli.puzzle_manager")
@patch("aoc_solver.cli.utilities")
@patch("aoc_solver.cli.argparse._sys.argv")
def test_run(
    mock_argv,
    mock_utilities,
    mock_puzzle_manager,
    mock_datetime,
    mock_puzzle_module,
    capsys,
):
    mock_datetime.now.return_value = datetime(2020, 11, 30)
    mock_utilities.load_module.return_value = mock_puzzle_module
    mock_argv.__getitem__.return_value = ["--date", "2019", "11"]

    cli.run()

    out, _ = capsys.readouterr()
    assert out == (
        "Part One: The puzzle answer is None\n" "Part Two: The puzzle answer is None\n"
    ), f"should run "

    mock_utilities.load_module.assert_called_once_with(year=2019, day=11)
    mock_puzzle_manager.read_puzzle_input.assert_called_once_with(year=2019, day=11)
