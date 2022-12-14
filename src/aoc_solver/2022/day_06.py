import typing

from aoc_solver.object_types import Solution

# --- Day 6: Tuning Trouble ---
# Source: https://adventofcode.com/2022/day/6


def detect_start_of_packet_marker(datastream: str, marker_size: int = 4) -> int:
    for i in range(len(datastream) - marker_size):
        marker = datastream[i : i + marker_size]
        if len(set(marker)) == marker_size:
            return i + marker_size

    return -1


def solve(puzzle_input=typing.List[str]) -> Solution:
    datastream = puzzle_input[0]
    return Solution(
        first=detect_start_of_packet_marker(datastream=datastream),
        second=detect_start_of_packet_marker(datastream=datastream, marker_size=14),
    )
