from aoc_solver.utilities import Solution


def test_find_max_carried_calories_sum_top_max(puzzle_module, mock_puzzle_input):
    assert puzzle_module.find_max_carried_calories(puzzle_input=mock_puzzle_input) == 24000


def test_find_max_carried_calories_sums_multiple_top_maxes(puzzle_module, mock_puzzle_input):
    assert puzzle_module.find_max_carried_calories(puzzle_input=mock_puzzle_input, top=3) == 45000


def test_solve_calculates_puzzle_answers(puzzle_module, mock_puzzle_input):
    assert puzzle_module.solve(puzzle_input=mock_puzzle_input) == Solution(first=24000, second=45000)
