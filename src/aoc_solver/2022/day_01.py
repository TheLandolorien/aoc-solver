import typing

from aoc_solver.object_types import Solution

# --- Day 1: Calorie Counting ---
# Source: https://adventofcode.com/2022/day/1


def solve(puzzle_input=typing.List[str]) -> Solution:
    carried_calories_per_elf = sum_carried_calories_per_elf(puzzle_input=puzzle_input)

    return Solution(
        first=sum_top_carried_calories(carried_calories=carried_calories_per_elf),
        second=sum_top_carried_calories(carried_calories=carried_calories_per_elf, top=3),
    )


def sum_carried_calories_per_elf(puzzle_input=typing.List[str]) -> typing.List[int]:
    grouped_calories = ",".join(puzzle_input).split(",,")
    return [sum(map(int, elf_calories.split(","))) for elf_calories in grouped_calories]


def sum_top_carried_calories(carried_calories: typing.List[int], top: int = 1) -> int:
    total_max_calories_carried = 0
    calories_buffer = carried_calories[:]
    for _ in range(top):
        total_max_calories_carried += (max_calories_carried := max(calories_buffer))
        calories_buffer.remove(max_calories_carried)

    return total_max_calories_carried
