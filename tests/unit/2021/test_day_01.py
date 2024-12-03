import pytest


@pytest.mark.parametrize("mock_puzzle_num,mock_solutions", [(1, (7, 5))])
def test_solve_calculates_puzzle_answers(
    mock_puzzle_num,
    mock_solutions,
    puzzle_module,
    mock_puzzle_inputs,
):
    mock_puzzle_input = mock_puzzle_inputs[mock_puzzle_num - 1]
    mock_first, mock_second = mock_solutions

    first, second = puzzle_module.solve(puzzle_input=mock_puzzle_input)

    assert first == mock_first
    assert second == mock_second


@pytest.mark.parametrize(
    "depths,num_increases",
    [
        ([1, 2, 1, 3, 5, 4, 5], 4),
        ([50, 55, 65, 75, 50, 55, 65, 75], 6),
        ([1, 1, 1], 0),
    ],
)
def test_count_depth_increases_with_default_window_size_of_1(depths, num_increases, puzzle_module):
    assert puzzle_module.count_depth_increases(depths=depths) == num_increases


@pytest.mark.parametrize(
    "depths,window_size,num_increases",
    [
        ([1, 2, 1, 3, 1, 4, 1, 5], 2, 3),
        ([50, 55, 65, 75, 50, 55, 65, 75], 4, 0),
        ([10, 20, 30, 10, 20, 30, 20, 10, 10], 3, 1),
    ],
)
def test_count_depth_increases_with_larger_window_sizes(
    depths, window_size, num_increases, puzzle_module
):
    assert (
        puzzle_module.count_depth_increases(depths=depths, window_size=window_size) == num_increases
    )
