from types import FunctionType
import typing

from aoc_solver.object_types import Solution

# --- Day 4: Camp Cleanup ---
# Source: https://adventofcode.com/2022/day/4


def is_contained(first: typing.Set[int], second: typing.Set[int]) -> bool:
    return first.issubset(second) or second.issubset(first)


def is_intersection(first: typing.Set[int], second: typing.Set[int]) -> bool:
    return len(first & second) > 0


def generate_range_set(assignment: str) -> typing.Set[int]:
    start, stop = map(int, assignment.split("-"))
    return set(range(start, stop + 1))


def count_special_assignments(
    assignment_pairs: typing.List[typing.List[str]], counter: FunctionType = is_contained
) -> int:
    return len(
        [
            result
            for assignments in assignment_pairs
            if (result := counter(*map(generate_range_set, assignments)))
        ]
    )


def solve(puzzle_input=typing.List[str]) -> Solution:
    assignment_pairs = [pair.split(",") for pair in puzzle_input]

    return Solution(
        first=count_special_assignments(assignment_pairs=assignment_pairs[:]),
        second=count_special_assignments(
            assignment_pairs=assignment_pairs[:], counter=is_intersection
        ),
    )
