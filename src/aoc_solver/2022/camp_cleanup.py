import typing

from aoc_solver.utilities import Solution

# --- Day 4: Camp Cleanup ---
# Source: https://adventofcode.com/2022/day/4


def count_special_assignments(puzzle_input: typing.List[str], count_type: str = "contain") -> str:
    count_method = check_assignment_overlap if count_type == "overlap" else check_assignment_containment
    return len(list(filter(lambda assignments: count_method(*generate_assignment_ranges(assignments=assignments)), puzzle_input)))


def generate_assignment_ranges(assignments: str) -> typing.Tuple[set, set]:
    return map(lambda assignment: generate_range_set(assignment=assignment), assignments.split(","))


def check_assignment_containment(first: typing.Set[int], second: typing.Set[int]) -> bool:
    return first.issubset(second) or second.issubset(first)


def check_assignment_overlap(first: typing.Set[int], second: typing.Set[int]) -> bool:
    return len(first & second) > 0


def generate_range_set(assignment: str) -> typing.Set[int]:
    start, stop = map(int, assignment.split("-"))
    return set(range(start, stop + 1))


def solve(puzzle_input=typing.List[str]) -> Solution:
    return Solution(
        first=count_special_assignments(puzzle_input=puzzle_input),
        second=count_special_assignments(puzzle_input=puzzle_input, count_type="overlap"),
    )
