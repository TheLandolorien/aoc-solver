import typing

from aoc_solver.object_types import Solution

# --- Day 9: Mirage Maintenance ---
# Source: https://adventofcode.com/2023/day/9


def sum_extrapolated_values(raw_dataset: typing.List[str], backward: bool = False) -> int:
    dataset = parse_input(raw_dataset=raw_dataset)
    values = 0
    for history in dataset:
        values += extrapolate_value(sequence=history, backward=backward)

    return values


def extrapolate_value(sequence: typing.List[int], backward: bool) -> int:
    if len(set(sequence)) == 1:
        return sequence[0]

    anchor = sequence[0] if backward else sequence[-1]
    pattern = extrapolate_value(
        sequence=[term - sequence[idx - 1] for idx, term in enumerate(sequence) if idx > 0],
        backward=backward,
    )

    direction = -1 if backward else 1

    return anchor + (direction * pattern)


def parse_input(raw_dataset: typing.List[str]) -> typing.List[typing.List[int]]:
    return [[int(value) for value in history.split()] for history in raw_dataset]


def solve(puzzle_input: typing.List[str]) -> Solution:
    return Solution(
        first=sum_extrapolated_values(raw_dataset=puzzle_input),
        second=sum_extrapolated_values(raw_dataset=puzzle_input, backward=True),
    )
