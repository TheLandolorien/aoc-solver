import importlib
import os
import sys

from datetime import datetime, timedelta, timezone

from aoc_solver.utilities import read_lines, Solution


def get_usage() -> str:
    return f"Usage: poetry run {sys.argv[0]} <YEAR> <DAY_NUMBER>"


def raise_for_invalid_dates(arg_name: str, arg_idx: int, date_format: str) -> None:
    arg = sys.argv[arg_idx]
    try:
        datetime.strptime(arg, date_format)
    except ValueError as err:
        raise ValueError(f"{get_usage()}\nInvalid {arg_name}: {arg}") from err


def raise_for_incorrect_number_of_args() -> None:
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        raise ValueError(get_usage())


def get_puzzle_path():
    src_path, package_name = os.path.split(os.path.dirname(__file__))
    _, *args = sys.argv

    if args:
        year, day = args
    else:
        now = datetime.now(timezone(timedelta(hours=-5)))

        year = now.year
        day = now.day

        if now.month != 12:
            year -= 1

        if now.day > 25:
            day = 25

    return (src_path, package_name, str(year), str(day).zfill(2))


def raise_for_invalid_arguments() -> None:
    raise_for_incorrect_number_of_args()

    if len(sys.argv) == 3:
        raise_for_invalid_dates("Year", 1, "%Y")
        raise_for_invalid_dates("Day", 2, "%d")


def solve() -> Solution:
    raise_for_invalid_arguments()

    src_path, package_name, year, day = get_puzzle_path()
    puzzle_module = importlib.import_module(name=".".join([package_name, year, f"day_{day}"]))
    puzzle_input_path = os.path.join(src_path, package_name, year, f"day_{day}.txt")

    return puzzle_module.solve(puzzle_input=read_lines(filepath=puzzle_input_path))
