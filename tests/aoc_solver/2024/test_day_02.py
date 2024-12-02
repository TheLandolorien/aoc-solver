import pytest


def test_parse_puzzle(puzzle_module, mock_puzzle_inputs):
    reports = puzzle_module.parse_puzzle(puzzle_input=mock_puzzle_inputs[0])

    assert reports == [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ], "should parse reports"


@pytest.mark.parametrize(
    "report,is_safe",
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], False),
        ([8, 6, 4, 4, 1], False),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_is_safe_report_without_tolerance(report, is_safe, puzzle_module):
    assert is_safe == puzzle_module.is_safe_report(
        report=report, with_tolerance=False
    ), "should determine if report is safe without tolerance"


@pytest.mark.parametrize(
    "report,is_safe",
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], True),
        ([8, 6, 4, 4, 1], True),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_is_safe_report_with_tolerance(report, is_safe, puzzle_module):
    assert is_safe == puzzle_module.is_safe_report(
        report=report, with_tolerance=True
    ), "should determine if report is safe with tolerance"


@pytest.mark.parametrize("mock_puzzle_num,mock_solutions", [(1, (2, 4))])
def test_solve_calculates_puzzle_answers(
    mock_puzzle_num,
    mock_solutions,
    puzzle_module,
    mock_puzzle_inputs,
):
    mock_puzzle_input = mock_puzzle_inputs[mock_puzzle_num - 1]
    mock_first, mock_second = mock_solutions

    first, second = puzzle_module.solve(puzzle_input=mock_puzzle_input)

    assert first == mock_first, "should count safe reports"
    assert second == mock_second, "should count safe reports with tolerances"
