import pytest

from aoc_solver.object_types import Solution


@pytest.mark.parametrize(
    "scenario,assignment,range",
    [
        ("expand small ranges", "2-4", {2, 3, 4}),
        ("expand large ranges", "0-10", {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}),
        ("collapse single item ranges", "7-7", {7}),
    ],
)
def test_generate_range_set(scenario, assignment, range, puzzle_module):
    assert puzzle_module.generate_range_set(assignment=assignment) == range, f"should {scenario}"


@pytest.mark.parametrize(
    "scenario,assignment_pairs,counter_name,total",
    [
        ("detect non-containment", [["2-4", "6-8"]], "is_contained", 0),
        ("detect same start containment", [["1-2", "1-3"]], "is_contained", 1),
        ("detect same stop containment", [["1-3", "2-3"]], "is_contained", 1),
        ("detect single item containment", [["5-5", "2-6"]], "is_contained", 1),
        (
            "detect multiple containments",
            [["2-3", "1-6"], ["1-2", "3-4"], ["1-6", "1-5"], ["3-4", "2-7"]],
            "is_contained",
            3,
        ),
        ("detect no overlap", [["2-4", "6-8"]], "is_intersection", 0),
        ("detect subset overlap", [["1-2", "1-3"]], "is_intersection", 1),
        ("detect single item overlap", [["1-3", "3-5"]], "is_intersection", 1),
        ("detect single item subset overlap", [["5-5", "2-6"]], "is_intersection", 1),
        (
            "detect multiple overlaps",
            [["2-7", "1-6"], ["1-2", "3-4"], ["1-5", "1-6"], ["1-4", "2-7"]],
            "is_intersection",
            3,
        ),
    ],
)
def test_count_special_assignments(scenario, assignment_pairs, counter_name, total, puzzle_module):
    counter = getattr(puzzle_module, counter_name)
    assert (
        puzzle_module.count_special_assignments(assignment_pairs=assignment_pairs, counter=counter)
        == total
    ), f"should {scenario}"


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

    assert first == mock_first
    assert second == mock_second
