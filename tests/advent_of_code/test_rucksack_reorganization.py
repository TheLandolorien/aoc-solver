import os
import typing
import pytest

from advent_of_code.utilities import read_lines

from advent_of_code import rucksack_reorganization

TEST_PUZZLE_NAME = os.path.splitext(os.path.basename(__file__))[0]


@pytest.fixture(scope="module")
def puzzle_input() -> typing.List[str]:
    return read_lines(filepath=os.path.join(os.path.dirname(__file__), f"{TEST_PUZZLE_NAME}.txt"))


def test_find_common_item_type(puzzle_input):
    assert rucksack_reorganization.find_common_item_type(puzzle_input[0].strip()) == "p", "should find common lowercase items"
    assert rucksack_reorganization.find_common_item_type(puzzle_input[1].strip()) == "L", "should find common uppercase items"


def test_determine_priority():
    assert rucksack_reorganization.determine_priority("p") == 16, "should determine priority for lowercase items"
    assert rucksack_reorganization.determine_priority("L") == 38, "should determine priority for uppercase items"
    assert rucksack_reorganization.determine_priority("P") == 42, "should have case-sensitive priorities "


def test_calculate_common_item(puzzle_input):
    assert rucksack_reorganization.calculate_total_common_item_priorities(puzzle_input=puzzle_input) == 157
