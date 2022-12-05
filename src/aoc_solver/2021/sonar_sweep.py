import typing

from aoc_solver.utilities import Solution

# --- Day 1: Sonar Sweep ---
# Source: https://adventofcode.com/2021/day/1


def count_depth_increases(depths: typing.List[int]) -> int:
    return len([depths[i] for i in range(1, len(depths)) if depths[i] > depths[i - 1]])


def solve(puzzle_input=typing.List[str]) -> Solution:
    depths = [int(depth) for depth in puzzle_input]

    return Solution(
        first=count_depth_increases(depths=depths[:]),
        second=None,
    )
