import importlib
import os
import sys

from datetime import datetime

from aoc_solver.utilities import read_lines, Solution


def get_puzzle_path():
    src_path, package_name = os.path.split(os.path.dirname(__file__))
    _, year, puzzle_name = sys.argv

    return (src_path, package_name, year, puzzle_name)


def raise_for_invalid_arguments() -> None:
    usage = f"Usage: poetry run {sys.argv[0]} <YYYY> <PUZZLE_NAME>"
    if len(sys.argv) != 3:
        raise ValueError(usage)

    try:
        datetime.strptime((year := sys.argv[1]), "%Y")
    except ValueError as err:
        raise ValueError(f"{usage}\nInvalid Year: {year}") from err


def solve() -> Solution:
    raise_for_invalid_arguments()

    src_path, package_name, year, puzzle_name = get_puzzle_path()
    puzzle_module = importlib.import_module(name=".".join([package_name, year, puzzle_name]))
    puzzle_input_path = os.path.join(src_path, package_name, year, f"{puzzle_name}.txt")

    return puzzle_module.solve(puzzle_input=read_lines(filepath=puzzle_input_path))
