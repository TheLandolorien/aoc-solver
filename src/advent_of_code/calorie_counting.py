import typing

from advent_of_code.utilities import parser, types


def find_max_carried_calories(calories_of_food_carried: typing.List[str], n=1) -> int:
    calories_per_elf = parser.parse(puzzle_input=calories_of_food_carried, calories=True)

    most_calories_total = 0
    for _ in range(n):
        most_calories_total += (max_calories := max(calories_per_elf))
        calories_per_elf.remove(max_calories)

    return most_calories_total


def solve(puzzle_input: typing.List[str]) -> types.Solution:
    return types.Solution(
        first=find_max_carried_calories(calories_of_food_carried=puzzle_input),
        second=find_max_carried_calories(calories_of_food_carried=puzzle_input, n=3),
    )
