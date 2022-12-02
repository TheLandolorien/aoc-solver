import importlib
import sys

import advent_of_code.utilities.puzzle_input_reader as puzzle_input_reader


def solve():
    raise_for_invalid_arguments()

    puzzle_solver = importlib.import_module(f"advent_of_code.{(puzzle_name := sys.argv[1])}")
    puzzle_solution = puzzle_solver.solve(puzzle_input=puzzle_input_reader.read(puzzle_name=puzzle_name))

    print(title := f"{puzzle_name.title().replace('_', ' ')}")
    print("".join(["="] * len(title)))
    print(f"Part 1 - {puzzle_solution.first}")
    print(f"Part 2 - {puzzle_solution.second}")


def raise_for_invalid_arguments() -> None:
    if len(sys.argv) != 2:
        raise ValueError(f"Usage: poetry run {sys.argv[0]} <PUZZLE_NAME>")


if __name__ == "__main__":
    solve()
