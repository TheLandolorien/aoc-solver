import os
import typing
import pytest

import advent_of_code.utilities.calorie_parser as parser


@pytest.fixture(scope="module")
def puzzle_input() -> typing.List[str]:
    puzzle_input_path = os.path.join(os.path.dirname(__file__), "../data/calories.txt")
    with open(puzzle_input_path) as f:
        return f.readlines()


def test_calorie_parser_sums_calories_per_elf(puzzle_input: typing.List[str]) -> None:
    assert parser.parse(item_calories=puzzle_input) == [6000, 4000, 11000, 24000, 10000]
