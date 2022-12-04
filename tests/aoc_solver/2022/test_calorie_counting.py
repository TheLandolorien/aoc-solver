import importlib
import os
import typing
import pytest

from aoc_solver.utilities import read_lines

calorie_counting = importlib.import_module("aoc_solver.2022.calorie_counting")


@pytest.fixture(scope="module")
def puzzle_input() -> typing.List[str]:
    puzzle_name = os.path.splitext(os.path.basename(__file__))[0]
    return read_lines(filepath=os.path.join(os.path.dirname(__file__), f"{puzzle_name}.txt"))


def test_find_max_carried_calories_sum_top_max(puzzle_input):
    assert calorie_counting.find_max_carried_calories(puzzle_input=puzzle_input) == 24000


def test_find_max_carried_calories_sums_multiple_top_maxes(puzzle_input):
    assert calorie_counting.find_max_carried_calories(puzzle_input=puzzle_input, top=3) == 45000
