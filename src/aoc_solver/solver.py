from datetime import datetime
import importlib
import sys

from aoc_solver.utilities import Solution


def solve() -> Solution:
    raise_for_invalid_arguments()

    return importlib.import_module(name=f"aoc_solver.{sys.argv[1]}.{sys.argv[2]}").solve()


def raise_for_invalid_arguments() -> None:
    usage = f"Usage: poetry run {sys.argv[0]} <YYYY> <PUZZLE_NAME>"
    if len(sys.argv) != 3:
        raise ValueError(usage)

    try:
        datetime.strptime((year := sys.argv[1]), "%Y")
    except ValueError as err:
        raise ValueError(f"{usage}\nInvalid Year: {year}") from err
