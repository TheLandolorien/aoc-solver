import typing

from aoc_solver.object_types import Solution

# --- Day 2: Red-Nosed Reports ---
# Source: https://adventofcode.com/2024/day/2


def count_safe_reports(reports: typing.List[typing.List[int]]) -> int:
    return [is_safe_report(report) for report in reports].count(True)


def is_safe_report(report: typing.List[int]) -> bool:
    deltas = []

    for idx in range(1, len(report)):
        delta = report[idx] - report[idx - 1]
        if abs(delta) > 3 or (idx > 1 and deltas[-1] * delta < 1):
            return False

        deltas.append(delta)

    return True


def parse_puzzle(puzzle_input: typing.List[str]) -> typing.List[typing.List[int]]:
    return [[int(n) for n in report.split()] for report in puzzle_input]


def solve(puzzle_input: typing.List[str]) -> Solution:
    reports = parse_puzzle(puzzle_input=puzzle_input)
    return Solution(
        first=count_safe_reports(reports=reports),
        second=None,
    )
