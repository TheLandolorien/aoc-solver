import typing

from aoc_solver.object_types import Solution

# --- Day 1: Sonar Sweep ---
# Source: https://adventofcode.com/2021/day/1


def count_depth_increases(depths: typing.List[int], window_size: int = 1) -> int:
    grouped_depths = [sum(depths[i : i + window_size]) for i in range(len(depths) - window_size + 1)]
    return len([grouped_depths[i] for i in range(1, len(grouped_depths)) if grouped_depths[i] > grouped_depths[i - 1]])


def solve(puzzle_input=typing.List[str]) -> Solution:
    depths = [int(depth) for depth in puzzle_input]

    return Solution(
        first=count_depth_increases(depths=depths[:]),
        second=count_depth_increases(depths=depths[:], window_size=3),
    )
