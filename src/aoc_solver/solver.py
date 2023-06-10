import os
import sys
import typing

from datetime import datetime, timedelta, timezone

from aoc_solver import object_types, utilities, puzzle_manager

SRC_PATH, PACKAGE_NAME = os.path.split(os.path.dirname(__file__))


def _get_usage() -> str:
    return f"Usage: poetry run {sys.argv[0]} <YEAR> <DAY_NUMBER>"


def _raise_for_incorrect_number_of_args() -> None:
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        raise ValueError(_get_usage())


def _raise_for_invalid_dates(value: str, date_format: str) -> None:
    try:
        datetime.strptime(value, date_format)
    except ValueError as err:
        raise ValueError(f"{_get_usage()}\nInvalid value {value} for format {date_format}") from err


def _validate_arguments() -> typing.Tuple[int, int]:
    _raise_for_incorrect_number_of_args()

    if len(sys.argv) == 3:
        year = sys.argv[1]
        day = sys.argv[2]

        _raise_for_invalid_dates(value=year, date_format="%Y")
        _raise_for_invalid_dates(value=day, date_format="%d")
    else:
        now = datetime.now(timezone(timedelta(hours=-5)))

        year = now.year
        day = now.day

        if now.month != 12:
            year -= 1
            day = 25

        if now.day > 25:
            day = 25

    return (int(year), int(day))


def solve() -> None:
    year, day = _validate_arguments()

    formatted_day = str(day).zfill(2)
    module_name = f"{year}.day_{formatted_day}"

    puzzle_module = utilities.load_module(relative_module_name=module_name)
    if not puzzle_module:
        puzzle_manager.create_puzzle_resources(year=year, day=day)
        puzzle_module = utilities.load_module(relative_module_name=module_name)

    first, second = puzzle_module.solve(
        puzzle_input=puzzle_manager.read_puzzle_input(year=year, day=day)
    )
    print(f"Part One: The puzzle answer is {first}")
    print(f"Part Two: The puzzle answer is {second}")
