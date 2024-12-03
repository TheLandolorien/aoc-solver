import typing
import re
import operator
from functools import reduce

from aoc_solver.object_types import Solution

# --- Day 3: Mull It Over ---
# Source: https://adventofcode.com/2024/day/3


def total_product(total: int, factors: typing.Tuple[str]) -> int:
    total += operator.mul(*[int(x) for x in factors])
    return total


def calculate_instructions(memory: str, pattern: str) -> int:
    instruction_pattern = re.compile(pattern=pattern)
    string_factors = instruction_pattern.findall(string=memory)

    return reduce(total_product, string_factors, 0)


def solve(puzzle_input: typing.List[str]) -> Solution:
    memory = puzzle_input[0]
    return Solution(
        first=calculate_instructions(memory=memory, pattern=r"mul\((\d{1,3}),(\d{1,3})\)"),
        second=None,
    )
