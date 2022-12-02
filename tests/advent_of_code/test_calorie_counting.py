import os
import pytest
import typing

from advent_of_code import calorie_counting


@pytest.fixture(scope="module")
def puzzle_input() -> typing.List[str]:
    puzzle_input_path = os.path.join(os.path.dirname(__file__), "data/calories.txt")
    with open(puzzle_input_path) as f:
        return f.readlines()


def test_find_max_carried_calories_successfully_locates_value(puzzle_input) -> None:
    assert calorie_counting.find_max_carried_calories(calories_of_food_carried=puzzle_input) == 24000


def test_find_max_carried_calories_successfully_locates_value(puzzle_input) -> None:
    assert calorie_counting.find_max_carried_calories(calories_of_food_carried=puzzle_input, n=3) == 45000
