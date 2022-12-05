import typing

from aoc_solver.utilities import Solution

# --- Day 1: Calorie Counting ---
# Source: https://adventofcode.com/2022/day/1


def find_max_carried_calories(puzzle_input: typing.List[str], top: int = 1) -> int:
    calories_carried_by_each_elf = [sum(map(int, calorie_counts.split(","))) for calorie_counts in ",".join(puzzle_input).split(",,")]

    total_max_calories_carried = 0
    for _ in range(top):
        total_max_calories_carried += (max_calories_carried := max(calories_carried_by_each_elf))
        calories_carried_by_each_elf.remove(max_calories_carried)

    return total_max_calories_carried


def solve(puzzle_input=typing.List[str]) -> Solution:
    return Solution(
        first=find_max_carried_calories(puzzle_input=puzzle_input),
        second=find_max_carried_calories(puzzle_input=puzzle_input, top=3),
    )
