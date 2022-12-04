from datetime import datetime
import importlib
import sys


def solve() -> None:
    raise_for_invalid_arguments()

    puzzle_solution = importlib.import_module(name=f"advent_of_code.{sys.argv[1]}.{sys.argv[2]}").solve()

    print(f"Part 1 - {puzzle_solution.first}")
    print(f"Part 2 - {puzzle_solution.second}")


def raise_for_invalid_arguments() -> None:
    usage = f"Usage: poetry run {sys.argv[0]} <YYYY> <PUZZLE_NAME>"
    if len(sys.argv) != 3:
        raise ValueError(usage)

    try:
        datetime.strptime((year := sys.argv[1]), "%Y")
    except ValueError as err:
        raise ValueError(f"{usage}\nInvalid Year: {year}") from err
