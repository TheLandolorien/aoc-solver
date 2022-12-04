import importlib
import os
import typing
import pytest

from aoc_solver.utilities import read_lines

camp_cleanup = importlib.import_module("aoc_solver.2022.camp_cleanup")


@pytest.fixture(scope="module")
def puzzle_input() -> typing.List[str]:
    puzzle_name = os.path.splitext(os.path.basename(__file__))[0]
    return read_lines(filepath=os.path.join(os.path.dirname(__file__), f"{puzzle_name}.txt"))


def test_check_assignment_containment():
    assert camp_cleanup.check_assignment_containment(set([2, 3, 4]), set([6, 7, 8])) == False, "should detect non-containment"
    assert camp_cleanup.check_assignment_containment(set([1, 2]), set([1, 2, 3])) == True, "should detect same start containment"
    assert camp_cleanup.check_assignment_containment(set([1, 2, 3]), set([2, 3])) == True, "should detect same stop containment"
    assert camp_cleanup.check_assignment_containment(set([5]), set([2, 3, 4, 5, 6])) == True, "should detect single item containment"


def test_check_assignment_overlap():
    assert camp_cleanup.check_assignment_overlap(set([2, 3, 4]), set([6, 7, 8])) == False, "should detect non-overlap"
    assert camp_cleanup.check_assignment_overlap(set([1, 2]), set([1, 2, 3])) == True, "should detect subset over"
    assert camp_cleanup.check_assignment_overlap(set([1, 2, 3]), set([3, 4, 5])) == True, "should single item overlap"
    assert camp_cleanup.check_assignment_overlap(set([5]), set([2, 3, 4, 5, 6])) == True, "should detect single item subset overlap"


def test_generate_range_set():
    assert camp_cleanup.generate_range_set(assignment="2-4") == set([2, 3, 4]), "should expand small range"
    assert camp_cleanup.generate_range_set(assignment="0-10") == set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), "should expand larger range"
    assert camp_cleanup.generate_range_set(assignment="7-7") == set([7]), "should collapse single item range"


def test_count_special_assignments(puzzle_input):
    assert camp_cleanup.count_special_assignments(puzzle_input=puzzle_input) == 2
    assert camp_cleanup.count_special_assignments(puzzle_input=puzzle_input, count_type="overlap") == 4
