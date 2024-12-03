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


def calculate_all_instructions(memory: str) -> int:
    instruction_pattern = re.compile(pattern=r"mul\((\d{1,3}),(\d{1,3})\)")
    string_factors = instruction_pattern.findall(string=memory)

    return reduce(total_product, string_factors, 0)


def calculate_enabled_instructions(memory: str) -> int:
    instruction_pattern = re.compile(pattern=r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
    instructions = instruction_pattern.findall(string=memory)

    string_factors = []
    enabled = True
    for instruction in instructions:
        if instruction == "do()":
            enabled = True
            continue
        elif instruction == "don't()":
            enabled = False
            continue
        elif instruction.startswith("mul(") and enabled:
            string_factors.append(instruction[4:-1].split(","))

    return reduce(total_product, string_factors, 0)


def solve(puzzle_input: typing.List[str]) -> Solution:
    memory = puzzle_input[0]
    return Solution(
        first=calculate_all_instructions(memory=memory),
        second=calculate_enabled_instructions(memory=memory),
    )
