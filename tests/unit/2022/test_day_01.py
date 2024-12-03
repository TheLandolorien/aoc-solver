import pytest


@pytest.mark.parametrize("mock_puzzle_num,mock_solutions", [(1, (24000, 45000))])
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
    "puzzle_input,expected_totals",
    [
        (["100", "", "100", "100", "", "100", "100", "100"], [100, 200, 300]),
        (
            ["50", "100", "", "200", "400", "1000", "", "2500", "", "300", "500"],
            [150, 1600, 2500, 800],
        ),
        (["50"], [50]),
    ],
)
def test_sum_carried_calories_per_elf(puzzle_input, expected_totals, puzzle_module):
    assert puzzle_module.sum_carried_calories_per_elf(puzzle_input=puzzle_input) == expected_totals


@pytest.mark.parametrize(
    "carried_calories,top,expected_total",
    [
        ([100, 200, 300], 1, 300),
        ([100, 200, 300], 2, 500),
        ([150, 1600, 2500, 800], 4, 5050),
    ],
)
def test_sum_top_carried_calories(carried_calories, top, expected_total, puzzle_module):
    assert (
        puzzle_module.sum_top_carried_calories(carried_calories=carried_calories, top=top)
        == expected_total
    )


def test_sum_top_carried_calories_gets_single_max_by_default(puzzle_module):
    assert puzzle_module.sum_top_carried_calories(carried_calories=[150, 1600, 2500, 800]) == 2500
