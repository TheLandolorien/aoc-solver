import pytest

from aoc_solver.utilities import Solution


def test_solve_calculates_puzzle_answers(puzzle_module, mock_puzzle_input):
    assert puzzle_module.solve(puzzle_input=mock_puzzle_input) == Solution(first="CMZ", second="MCD")


@pytest.mark.parametrize(
    "stacks,flattened_stacks",
    [
        (
            [
                "   ",
                "   ",
                "[L]",
                " 1 ",
            ],
            [["L"]],
        ),
        (
            [
                "    [X]    ",
                "    [B] [O]",
                "[L] [C] [E]",
                " 1   2   3 ",
            ],
            [["L"], ["C", "B", "X"], ["E", "O"]],
        ),
        (
            [
                "    [W]            ",
                "    [X]     [D]    ",
                "[P] [B] [O] [J]    ",
                "[L] [C] [E] [A] [Z]",
                " 1   2   3   4   5 ",
            ],
            [["L", "P"], ["C", "B", "X", "W"], ["E", "O"], ["A", "J", "D"], ["Z"]],
        ),
    ],
)
def test_flatten_stacks(stacks, flattened_stacks, puzzle_module):
    assert puzzle_module.flatten_stacks(stacks=stacks) == flattened_stacks


@pytest.mark.parametrize(
    "flattened_stacks,step,new_arrangement",
    [
        (
            [["L"], ["C", "B", "X"], ["E", "O"]],
            "move 2 from 3 to 1",
            [["L", "O", "E"], ["C", "B", "X"], []],
        ),
        (
            [["L", "O", "E"], ["C", "B", "X"], []],
            "move 1 from 2 to 3",
            [["L", "O", "E"], ["C", "B"], ["X"]],
        ),
    ],
)
def test_move_crates_in_reverse_by_default(flattened_stacks, step, new_arrangement, puzzle_module):
    assert puzzle_module.move_crates(flattened_stacks=flattened_stacks, step=step) == new_arrangement


@pytest.mark.parametrize(
    "flattened_stacks,step,new_arrangement",
    [
        (
            [["L"], ["C", "B", "X"], ["E", "O"]],
            "move 2 from 3 to 1",
            [["L", "E", "O"], ["C", "B", "X"], []],
        ),
        (
            [["L", "E", "O"], ["C", "B", "X"], []],
            "move 3 from 1 to 3",
            [[], ["C", "B", "X"], ["L", "E", "O"]],
        ),
    ],
)
def test_move_crates_in_order(flattened_stacks, step, new_arrangement, puzzle_module):
    assert puzzle_module.move_crates(flattened_stacks=flattened_stacks, step=step, in_order=True) == new_arrangement
