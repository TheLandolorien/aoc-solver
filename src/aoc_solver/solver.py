import sys
import typing

from datetime import datetime, timedelta, timezone

from aoc_solver.utilities import run_solution


def _get_usage() -> str:
    return f"Usage: poetry run {sys.argv[0]} <YEAR> <DAY_NUMBER>"


def _raise_for_invalid_dates(value: str, date_format: str) -> None:
    try:
        datetime.strptime(value, date_format)
    except ValueError as err:
        raise ValueError(f"{_get_usage()}\nInvalid value {value} for format {date_format}") from err


def _raise_for_incorrect_number_of_args() -> None:
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        raise ValueError(_get_usage())


def validate_arguments() -> typing.Tuple[int, int]:
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

        if now.day > 25:
            day = 25

    return (int(year), int(day))


def solve() -> typing.Any:
    year, day = validate_arguments()

    return run_solution(year=year, day=day)
