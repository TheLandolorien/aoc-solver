import pytest

from aoc_solver.object_types import Solution


@pytest.mark.parametrize(
    "mock_datastream,package_marker_end,message_marker_end",
    [
        (["mjqjpqmgbljsphdztnvjfqwrcgsmlb"], 7, 19),
        (["bvwbjplbgvbhsrlpgdmjqwftvncz"], 5, 23),
        (["nppdvjthqldpwncqszvftbrmjlhg"], 6, 23),
        (["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"], 10, 29),
        (["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"], 11, 26),
        (["aaabbbcccdddeeefffggghhhiiijjjk"], -1, -1),
    ],
)
def test_solve_calculates_puzzle_answers(
    mock_datastream, package_marker_end, message_marker_end, puzzle_module
):
    assert puzzle_module.solve(puzzle_input=mock_datastream) == Solution(
        first=package_marker_end, second=message_marker_end
    )
