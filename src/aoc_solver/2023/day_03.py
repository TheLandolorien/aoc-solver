import re
import typing

from aoc_solver.object_types import Solution

# --- Day 3: Gear Ratios ---
# Source: https://adventofcode.com/2023/day/3


def sum_part_numbers(puzzle_input: typing.List[str]) -> int:
    return sum(find_part_numbers(schematic=puzzle_input))


def find_part_numbers(schematic: typing.List[str]) -> typing.List[int]:
    part_numbers = []
    for idx, line in enumerate(schematic):
        for m in re.finditer(r"(\d+)", line):
            part_number = extract_part_number(match=m, line_number=idx, schematic=schematic)
            if part_number:
                part_numbers.append(part_number)

    return part_numbers


def extract_part_number(
    match: re.Match,
    line_number: int,
    schematic: typing.List[str],
) -> int | None:
    left, right, top, bottom = calculate_bounds(match=match, idx=line_number, schematic=schematic)

    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if re.match(r"[^a-zA-Z0-9_.]", schematic[i][j]):
                part_number = int(match.group())
                return part_number
    return None


def sum_gear_ratios(puzzle_input: typing.List[str]) -> int:
    return sum(find_gear_ratios(schematic=puzzle_input))


def find_gear_ratios(schematic: typing.List[str]) -> typing.List[int]:
    gear_ratios = []
    for idx, line in enumerate(schematic):
        for m in re.finditer(r"(\*)", line):
            gear_ratio = extract_gear_ratio(match=m, line_number=idx, schematic=schematic)
            if gear_ratio:
                gear_ratios.append(gear_ratio)

    return gear_ratios


def extract_gear_ratio(
    match: re.Match,
    line_number: int,
    schematic: typing.List[str],
) -> int | None:
    left, right, top, bottom = calculate_bounds(match=match, idx=line_number, schematic=schematic)

    part_numbers = []

    bounds = {"start": left, "end": right}
    part_numbers.extend(extract_gear_part_nums(line=schematic[top], **bounds))
    part_numbers.extend(extract_gear_part_nums(line=schematic[line_number], **bounds))
    part_numbers.extend(extract_gear_part_nums(line=schematic[bottom], **bounds))

    if len(part_numbers) == 2:
        return part_numbers[0] * part_numbers[1]

    return None


def extract_gear_part_nums(line: str, start: int, end: int) -> typing.List[int]:
    part_numbers = [
        int(m.group())
        for m in re.finditer(r"(\d+)", line)
        if m.end() - 1 >= start and m.start() <= end
    ]
    return part_numbers


def calculate_bounds(
    match: re.Match,
    idx: int,
    schematic: typing.List[str],
) -> typing.Tuple[int]:
    heigth = len(schematic)
    width = len(schematic[0])
    left = match.start() if match.start() == 0 else match.start() - 1
    right = match.end() if match.end() < width else match.end() - 1
    top = idx if idx == 0 else idx - 1
    bottom = idx + 1 if idx < heigth - 1 else idx

    return left, right, top, bottom


def solve(puzzle_input: typing.List[str]) -> Solution:
    return Solution(
        first=sum_part_numbers(puzzle_input=puzzle_input),
        second=sum_gear_ratios(puzzle_input=puzzle_input),
    )
