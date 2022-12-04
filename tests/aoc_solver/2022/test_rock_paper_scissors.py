import importlib
import os
import typing
import pytest

from aoc_solver.utilities import read_lines

rock_paper_scissors = importlib.import_module("aoc_solver.2022.rock_paper_scissors")


@pytest.fixture(scope="module")
def puzzle_input() -> typing.List[str]:
    puzzle_name = os.path.splitext(os.path.basename(__file__))[0]
    return read_lines(filepath=os.path.join(os.path.dirname(__file__), f"{puzzle_name}.txt"))


def test_score_matches_predicts_score_with_suggested_plays(puzzle_input):
    assert rock_paper_scissors.score_matches(puzzle_input=puzzle_input) == 15


def test_score_matches_predicts_score_with_suggested_outcomes(puzzle_input):
    assert rock_paper_scissors.score_matches(puzzle_input=puzzle_input, score_type="outcome") == 12
