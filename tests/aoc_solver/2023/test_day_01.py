def test_solve_with_numerical_digits_only(puzzle_module, mock_puzzle_input):
    first, second = puzzle_module.solve(puzzle_input=mock_puzzle_input)
    assert first == 142, "should sum calibration values with digits only"
    assert second == 142, "should sum calibration values with number words"


def test_solve_with_number_words(puzzle_module):
    mock_puzzle_input = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    first, second = puzzle_module.solve(puzzle_input=mock_puzzle_input)

    assert first == 209, "should sum calibration values with digits only"
    assert second == 281, "should sum calibration values with number words"
