import pytest

from aoc_solver.utilities import Solution


def test_solve_calculates_puzzle_answers(puzzle_module, mock_puzzle_input):
    assert puzzle_module.solve(puzzle_input=mock_puzzle_input) == Solution(first=7, second=None)


@pytest.mark.parametrize(
    "depths,num_increases",
    [
        (["1", "2", "1", "3", "5", "4", "5"], 4),
        (["50", "55", "65", "75", "50", "55", "65", "75"], 6),
        (["1", "1", "1"], 0),
    ],
)
def test_count_depth_increases(depths, num_increases, puzzle_module):
    assert puzzle_module.count_depth_increases(depths=depths) == num_increases
