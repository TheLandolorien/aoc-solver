import pytest
from aoc_solver.object_types import Solution


@pytest.mark.parametrize(
    "counter,outcome,score",
    [("A", "X", 3), ("B", "X", 1), ("C", "X", 2), ("A", "Y", 4), ("A", "Z", 8)],
)
def test_calculate_score_by_outcomes(counter, outcome, score, puzzle_module):
    assert puzzle_module.calculate_score_by_outcomes(encrypted_counter=counter, encrypted_outcome=outcome) == score


@pytest.mark.parametrize(
    "counter,play,score",
    [("A", "X", 4), ("B", "X", 1), ("C", "X", 7), ("A", "Y", 8), ("A", "Z", 3)],
)
def test_calculate_score_by_plays(counter, play, score, puzzle_module):
    assert puzzle_module.calculate_score_by_plays(encrypted_counter=counter, encrypted_play=play) == score


@pytest.mark.parametrize(
    "matches,calculator,final_score",
    [
        ([["A", "X"]], "calculate_score_by_plays", 4),
        ([["A", "X"]], "calculate_score_by_outcomes", 3),
        ([["A", "X"], ["B", "X"], ["C", "Z"], ["C", "Y"]], "calculate_score_by_plays", 13),
        ([["A", "X"], ["B", "X"], ["C", "Z"], ["C", "Y"]], "calculate_score_by_outcomes", 17),
    ],
)
def test_score_matches(matches, calculator, final_score, puzzle_module):
    assert puzzle_module.score_matches(matches=matches, calculator=getattr(puzzle_module, calculator)) == final_score


def test_solve_calculates_puzzle_answers(puzzle_module, mock_puzzle_input):
    assert puzzle_module.solve(puzzle_input=mock_puzzle_input) == Solution(first=15, second=12)
