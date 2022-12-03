import os
import typing
import pytest

from advent_of_code.utilities import read_lines

from advent_of_code import rock_paper_scissors

TEST_PUZZLE_NAME = os.path.splitext(os.path.basename(__file__))[0]


@pytest.fixture(scope="module")
def puzzle_input() -> typing.List[str]:
    return read_lines(filepath=os.path.join(os.path.dirname(__file__), f"{TEST_PUZZLE_NAME}.txt"))


def test_score_matches_predicts_score_with_suggested_play(puzzle_input):
    assert rock_paper_scissors.score_matches_by_play(puzzle_input=puzzle_input) == 15


def test_score_matches_predicts_score_with_suggested_outcome(puzzle_input):
    assert rock_paper_scissors.score_matches_by_outcome(puzzle_input=puzzle_input) == 12
