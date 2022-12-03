import os
import typing
import pytest

from advent_of_code.utilities import read_lines

from advent_of_code import calorie_counting

TEST_PUZZLE_NAME = os.path.splitext(os.path.basename(__file__))[0]


@pytest.fixture(scope="module")
def puzzle_input() -> typing.List[str]:
    return read_lines(filepath=os.path.join(os.path.dirname(__file__), f"{TEST_PUZZLE_NAME}.txt"))


def test_find_max_carried_calories_sum_top_max(puzzle_input) -> None:
    assert calorie_counting.find_max_carried_calories(puzzle_input=puzzle_input) == 24000


def test_find_max_carried_calories_sums_multiple_top_maxes(puzzle_input) -> None:
    assert calorie_counting.find_max_carried_calories(puzzle_input=puzzle_input, top=3) == 45000
