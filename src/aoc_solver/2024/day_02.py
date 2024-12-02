import typing
from itertools import combinations

from aoc_solver.object_types import Solution

# --- Day 2: Red-Nosed Reports ---
# Source: https://adventofcode.com/2024/day/2


def count_safe_reports(reports: typing.List[typing.List[int]], with_tolerance: bool = False) -> int:
    return [
        is_safe_report(report=report, with_tolerance=with_tolerance) for report in reports
    ].count(True)


def is_safe_report(report: typing.List[int], with_tolerance: bool) -> bool:
    report_combinations = [report[:]]
    if with_tolerance:
        report_combinations = [
            list(levels)
            for idx in range(len(report) - 1, len(report) + 1)
            for levels in combinations(report, idx)
        ]

    for report_combo in report_combinations:
        deltas = [report_combo[i] - report_combo[i - 1] for i in range(1, len(report_combo))]
        has_big_changes = any([abs(delta) > 3 for delta in deltas])
        has_static_levels = any([delta == 0 for delta in deltas])
        has_direction_change = any([deltas[i - 1] * deltas[i] < 0 for i in range(1, len(deltas))])

        if not has_big_changes and not has_direction_change and not has_static_levels:
            return True

    return False


def parse_puzzle(puzzle_input: typing.List[str]) -> typing.List[typing.List[int]]:
    return [[int(n) for n in report.split()] for report in puzzle_input]


def solve(puzzle_input: typing.List[str]) -> Solution:
    reports = parse_puzzle(puzzle_input=puzzle_input)
    return Solution(
        first=count_safe_reports(reports=reports),
        second=count_safe_reports(reports=reports, with_tolerance=True),
    )
