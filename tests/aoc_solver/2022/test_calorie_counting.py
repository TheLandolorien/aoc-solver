import importlib

calorie_counting = importlib.import_module("aoc_solver.2022.calorie_counting")


def test_find_max_carried_calories_sum_top_max(mock_puzzle_input):
    assert calorie_counting.find_max_carried_calories(puzzle_input=mock_puzzle_input) == 24000


def test_find_max_carried_calories_sums_multiple_top_maxes(mock_puzzle_input):
    assert calorie_counting.find_max_carried_calories(puzzle_input=mock_puzzle_input, top=3) == 45000
