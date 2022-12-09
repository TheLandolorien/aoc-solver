import pytest
from aoc_solver.utilities import Solution


@pytest.mark.parametrize(
    "mock_datastream,start",
    [
        (["mjqjpqmgbljsphdztnvjfqwrcgsmlb"], 7),
        (["bvwbjplbgvbhsrlpgdmjqwftvncz"], 5),
        (["nppdvjthqldpwncqszvftbrmjlhg"], 6),
        (["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"], 10),
        (["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"], 11),
        (["aaabbbcccdddeeefffggghhhiiijjjk"], -1),
    ],
)
def test_solve_calculates_puzzle_answers(mock_datastream, start, puzzle_module):
    assert puzzle_module.solve(puzzle_input=mock_datastream) == Solution(first=start, second=None)
