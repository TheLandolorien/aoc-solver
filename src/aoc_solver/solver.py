import os
import sys
import typing

from datetime import datetime, timedelta, timezone

from aoc_solver import utilities, puzzle_manager

SRC_PATH, PACKAGE_NAME = os.path.split(os.path.dirname(__file__))


def _get_usage() -> str:
    return f"Usage: poetry run {sys.argv[0]} <YEAR> <DAY_NUMBER>"


def _raise_for_incorrect_number_of_args() -> None:
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        raise ValueError(_get_usage())


def _raise_for_invalid_dates(value: str, date_format: str) -> None:
    try:
        datetime.strptime(value, date_format)
        return int(value)
    except ValueError as err:
        raise ValueError(f"{_get_usage()}\nInvalid value {value} for format {date_format}") from err


def _determine_most_recent_puzzle_date() -> typing.Tuple[int, int]:
    now = datetime.now(timezone(timedelta(hours=-5)))

    year = now.year
    day = now.day

    if now.month != 12:
        year -= 1
        day = 25

    if now.day > 25:
        day = 25

    return (year, day)


def _validate_arguments() -> typing.Tuple[int, int]:
    _raise_for_incorrect_number_of_args()

    latest_year, latest_day = _determine_most_recent_puzzle_date()

    if len(sys.argv) == 3:
        year = _raise_for_invalid_dates(value=sys.argv[1], date_format="%Y")
        day = _raise_for_invalid_dates(value=sys.argv[2], date_format="%d")

        if year < 2015:
            raise ValueError(f"{_get_usage()}\nInvalid year {year}: Advent of Code began in 2015")
        if day > 25:
            raise ValueError(
                f"{_get_usage()}\nInvalid day {day}: Advent of Code is only 25 days per year"
            )
        if year > latest_year or (year == latest_year and day > latest_day):
            raise ValueError(f"{_get_usage()}\nInvalid puzzle {year} day {day}: Not yet released")

        return (year, day)

    return (latest_year, latest_day)


def solve() -> None:
    year, day = _validate_arguments()

    puzzle_module = utilities.load_module(year=year, day=day)
    if not puzzle_module:
        puzzle_manager.create_puzzle_resources(year=year, day=day)
        puzzle_module = utilities.load_module(year=year, day=day)

    first, second = puzzle_module.solve(
        puzzle_input=puzzle_manager.read_puzzle_input(year=year, day=day)
    )
    print(f"Part One: The puzzle answer is {first}")
    print(f"Part Two: The puzzle answer is {second}")
