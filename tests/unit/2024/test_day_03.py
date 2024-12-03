import pytest


@pytest.mark.parametrize("mock_puzzle_num,mock_solutions", [(1, (161, None))])
def test_solve_calculates_puzzle_answers(
    mock_puzzle_num,
    mock_solutions,
    puzzle_module,
    mock_puzzle_inputs,
):
    mock_puzzle_input = mock_puzzle_inputs[mock_puzzle_num - 1]
    mock_first, mock_second = mock_solutions

    first, second = puzzle_module.solve(puzzle_input=mock_puzzle_input)

    assert first == mock_first, "should total mul instructions"
    assert second == mock_second, "should <PART_2_SCENARIO>"
