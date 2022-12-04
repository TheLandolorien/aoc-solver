import importlib


rock_paper_scissors = importlib.import_module("aoc_solver.2022.rock_paper_scissors")


def test_score_matches_predicts_score_with_suggested_plays(mock_puzzle_input):
    assert rock_paper_scissors.score_matches(puzzle_input=mock_puzzle_input) == 15


def test_score_matches_predicts_score_with_suggested_outcomes(mock_puzzle_input):
    assert rock_paper_scissors.score_matches(puzzle_input=mock_puzzle_input, score_type="outcome") == 12
