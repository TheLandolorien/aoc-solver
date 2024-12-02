import typing

from aoc_solver.object_types import Solution

# --- Day 1: Historian Hysteria ---
# Source: https://adventofcode.com/2024/day/1


def sum_distances(left_list: typing.List[int], right_list: typing.List[int]) -> int:
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)

    total = 0

    for idx, left in enumerate(sorted_left):
        total += abs(left - sorted_right[idx])

    return total


def parse_puzzle(input: typing.List[str]) -> typing.Tuple[typing.List[int], typing.List[int]]:
    left = []
    right = []

    for line in input:
        l, r = [int(n) for n in line.split()]
        left.append(l)
        right.append(r)

    return left, right


def solve(puzzle_input: typing.List[str]) -> Solution:
    left, right = parse_puzzle(input=puzzle_input)
    return Solution(
        first=sum_distances(left_list=left, right_list=right),
        second=None,
    )
