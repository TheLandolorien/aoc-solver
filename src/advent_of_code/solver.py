import importlib
import os
import sys
import typing


def solve():
    raise_for_invalid_arguments()

    puzzle_solver = importlib.import_module(f"advent_of_code.{(puzzle_name := sys.argv[1])}")
    puzzle_solution = puzzle_solver.solve(puzzle_input=read_puzzle_input(name=puzzle_name))

    print(title := f"{puzzle_name.title().replace('_', ' ')}")
    print("".join(["="] * len(title)))
    print(f"Part 1 - {puzzle_solution.first}")
    print(f"Part 2 - {puzzle_solution.second}")


def read_puzzle_input(name: str) -> typing.List[str]:
    puzzle_input_path = os.path.join(os.path.dirname(__file__), f"{name}.txt")
    with open(puzzle_input_path) as puzzle_input:
        return puzzle_input.readlines()


def raise_for_invalid_arguments() -> None:
    if len(sys.argv) != 2:
        raise ValueError(f"Usage: poetry run {sys.argv[0]} <PUZZLE_NAME>")


if __name__ == "__main__":
    solve()
