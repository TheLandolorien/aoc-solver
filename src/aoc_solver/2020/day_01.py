import typing

from aoc_solver.object_types import Solution

# --- Day 1: Report Repair ---
# Source: https://adventofcode.com/2020/day/1


def find_product_of_2020_addends(puzzle_input: typing.List[str]) -> int:
    first, second = find_2020_addends(expense_report=parse_puzzle(input=puzzle_input))
    return first * second


def find_2020_addends(expense_report: typing.List[int]) -> typing.Tuple[int]:
    for entry in expense_report:
        composite = 2020 - entry
        if composite in expense_report:
            return entry, composite


def parse_puzzle(input: typing.List[str]) -> typing.List[int]:
    return [int(n) for n in input]


def solve(puzzle_input: typing.List[str]) -> Solution:
    return Solution(
        first=find_product_of_2020_addends(puzzle_input=puzzle_input),
        second=None,
    )
