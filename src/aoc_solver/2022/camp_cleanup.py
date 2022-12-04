import os
import typing

from aoc_solver.utilities import Solution, read_lines

# --- Day 4: Camp Cleanup ---
# Source: https://adventofcode.com/2022/day/4


def count_fully_contained_assignments(puzzle_input: typing.List[str]) -> str:
    fully_contained_assignments = list(filter(check_assignment_containment, puzzle_input))
    return len(fully_contained_assignments)


def check_assignment_containment(section_assignments: str) -> bool:
    first, second = map(lambda assignment: generate_range_set(assignment=assignment), section_assignments.split(","))
    return first.issubset(second) or second.issubset(first)


def generate_range_set(assignment: str) -> typing.Set[int]:
    start, stop = map(int, assignment.split("-"))
    return set(range(start, stop + 1))


def solve() -> Solution:
    puzzle_name = os.path.splitext(os.path.basename(__file__))[0]
    puzzle_input = read_lines(filepath=os.path.join(os.path.dirname(__file__), f"{puzzle_name}.txt"))

    return Solution(
        first=count_fully_contained_assignments(puzzle_input=puzzle_input),
        second=None,
    )
