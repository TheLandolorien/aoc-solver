import typing

from aoc_solver.object_types import Solution

# --- Day 3: Rucksack Reorganization ---
# Source: https://adventofcode.com/2022/day/3


def calculate_total_common_item_priorities(rucksacks: typing.List[str], group_size: int = 1) -> int:
    rucksack_groups = []
    for i in range(len(rucksacks)):
        if i % group_size == 0:
            rucksack_groups.append([])
        rucksack_groups[-1].append(rucksacks[i])

    return sum(
        [determine_priority(find_common_item_type(rucksacks)) for rucksacks in rucksack_groups]
    )


def determine_intersection(*args) -> str:
    intersection = set(args[0])
    for items in args[1:]:
        intersection = intersection & set(items)

    return intersection.pop()


def determine_priority(item_type: str) -> str:
    offset = 0
    base_chr = "a"
    if item_type.isupper():
        offset = 26
        base_chr = "A"

    return ord(item_type) + offset - ord(base_chr) + 1


def find_common_item_type(rucksacks: typing.List[str]) -> str:
    # Assumption: Content lengths are even
    # Source: "A given rucksack always has the same number of items in each of its two compartments..."
    if len(rucksacks) == 1:
        midpoint_idx = len(items := rucksacks[0]) // 2
        return determine_intersection(items[:midpoint_idx], items[midpoint_idx:])
    else:
        return determine_intersection(*rucksacks)


def solve(puzzle_input=typing.List[str]) -> Solution:
    return Solution(
        first=calculate_total_common_item_priorities(rucksacks=puzzle_input[:]),
        second=calculate_total_common_item_priorities(rucksacks=puzzle_input[:], group_size=3),
    )
