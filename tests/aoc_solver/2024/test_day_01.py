import pytest


def test_parse_puzzle(puzzle_module, mock_puzzle_inputs):
    left_list, right_list = puzzle_module.parse_puzzle(input=mock_puzzle_inputs[0])

    assert left_list == [3, 4, 2, 1, 3, 3], "should extract left list"
    assert right_list == [4, 3, 5, 3, 9, 3], "should extract right list"


@pytest.mark.parametrize("mock_puzzle_num,mock_solutions", [(1, (11, None))])
def test_solve_calculates_puzzle_answers(
    mock_puzzle_num,
    mock_solutions,
    puzzle_module,
    mock_puzzle_inputs,
):
    mock_puzzle_input = mock_puzzle_inputs[mock_puzzle_num - 1]
    mock_first, mock_second = mock_solutions

    first, second = puzzle_module.solve(puzzle_input=mock_puzzle_input)

    assert first == mock_first, "should find the total distance"
    assert second == mock_second, "should <PART_2_SCENARIO>"
