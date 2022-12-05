from aoc_solver.utilities import Solution


def test_score_matches_predicts_score_with_suggested_plays(puzzle_module, mock_puzzle_input):
    assert puzzle_module.score_matches(puzzle_input=mock_puzzle_input) == 15


def test_score_matches_predicts_score_with_suggested_outcomes(puzzle_module, mock_puzzle_input):
    assert puzzle_module.score_matches(puzzle_input=mock_puzzle_input, score_type="outcome") == 12


def test_solve_calculates_puzzle_answers(puzzle_module, mock_puzzle_input):
    assert puzzle_module.solve(puzzle_input=mock_puzzle_input) == Solution(first=15, second=12)
