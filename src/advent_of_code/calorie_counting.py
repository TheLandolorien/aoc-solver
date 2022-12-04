import os
import typing

from advent_of_code import types
from advent_of_code.utilities import read_lines

PUZZLE_NAME = os.path.splitext(os.path.basename(__file__))[0]


def find_max_carried_calories(puzzle_input: typing.List[str], top: int = 1) -> int:
    calories_carried_by_each_elf = [sum(map(int, calorie_counts.split(","))) for calorie_counts in ",".join(puzzle_input).split(",,")]

    total_max_calories_carried = 0
    for _ in range(top):
        total_max_calories_carried += (max_calories_carried := max(calories_carried_by_each_elf))
        calories_carried_by_each_elf.remove(max_calories_carried)

    return total_max_calories_carried


def solve() -> types.Solution:
    puzzle_input = read_lines(filepath=os.path.join(os.path.dirname(__file__), f"{PUZZLE_NAME}.txt"))

    return types.Solution(
        first=find_max_carried_calories(puzzle_input=puzzle_input),
        second=find_max_carried_calories(puzzle_input=puzzle_input, top=3),
    )
