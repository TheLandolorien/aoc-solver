import typing

from advent_of_code.utilities import calorie_parser


def find_max_carried_calories(puzzle_input: typing.List[str]) -> int:
    calories_per_elf = calorie_parser.parse(item_calories=puzzle_input)
    return max(calories_per_elf)
