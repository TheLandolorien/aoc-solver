import typing

from advent_of_code.utilities import calorie_parser, types


def find_max_carried_calories(calories_of_food_carried: typing.List[str]) -> int:
    calories_per_elf = calorie_parser.parse(item_calories=calories_of_food_carried)
    return max(calories_per_elf)


def solve(puzzle_input: typing.List[str]) -> types.Solution:
    return types.Solution(first=find_max_carried_calories(calories_of_food_carried=puzzle_input), second=None)
