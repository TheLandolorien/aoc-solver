import math
import typing
from itertools import combinations

from aoc_solver.object_types import Solution

# --- Day 1: Report Repair ---
# Source: https://adventofcode.com/2020/day/1


def find_product_of_2020_addends(puzzle_input: typing.List[str], count: int) -> int:
    expense_report = parse_puzzle(input=puzzle_input)
    for addends in combinations(expense_report, count):
        if sum(addends) == 2020:
            return math.prod(addends)


def parse_puzzle(input: typing.List[str]) -> typing.List[int]:
    return [int(n) for n in input]


def solve(puzzle_input: typing.List[str]) -> Solution:
    return Solution(
        first=find_product_of_2020_addends(puzzle_input=puzzle_input, count=2),
        second=find_product_of_2020_addends(puzzle_input=puzzle_input, count=3),
    )
