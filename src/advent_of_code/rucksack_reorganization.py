import os
import typing
from advent_of_code import types

from advent_of_code.utilities import read_lines

PUZZLE_NAME = os.path.splitext(os.path.basename(__file__))[0]


def calculate_total_common_item_priorities(puzzle_input: typing.List[str]) -> int:
    return sum([determine_priority(find_common_item_type(rucksack_contents.strip())) for rucksack_contents in puzzle_input])


def find_common_item_type(rucksack_contents: str) -> str:
    # Assumption: Content lengths are even
    # Source: "A given rucksack always has the same number of items in each of its two compartments..."
    first = rucksack_contents[: (midpoint_idx := len(rucksack_contents) // 2)]
    second = rucksack_contents[midpoint_idx:]

    return (set(first) & set(second)).pop()


def determine_priority(item_type: str) -> str:
    offset = 0
    base_chr = "a"
    if item_type.isupper():
        offset = 26
        base_chr = "A"

    return ord(item_type) + offset - ord(base_chr) + 1


def solve() -> types.Solution:
    puzzle_input = read_lines(filepath=os.path.join(os.path.dirname(__file__), f"{PUZZLE_NAME}.txt"))
    return types.Solution(first=calculate_total_common_item_priorities(puzzle_input=puzzle_input), second=None)
