import importlib
import sys


def solve() -> None:
    raise_for_invalid_arguments()

    puzzle_solution = importlib.import_module(name=f"advent_of_code.{sys.argv[1]}").solve()

    print(f"Part 1 - {puzzle_solution.first}")
    print(f"Part 2 - {puzzle_solution.second}")


def raise_for_invalid_arguments() -> None:
    if len(sys.argv) != 2:
        raise ValueError(f"Usage: poetry run {sys.argv[0]} <PUZZLE_NAME>")
