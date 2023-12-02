import re
import typing

from aoc_solver.object_types import Solution

# --- Day 1: Trebuchet?! ---
# Source: https://adventofcode.com/2023/day/1

NUMBER_WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def sum_calibration_values(
    document: typing.List[str],
    parse_words: bool = False,
) -> typing.List[int]:
    return sum([parse_calibration_value(text=line, parse_words=parse_words) for line in document])


def parse_calibration_value(text: str, parse_words: bool = False):
    if parse_words:
        nums = re.findall(f"(?=(\\d{{1}}|{'|'.join(NUMBER_WORDS)}))", text)
        return int(parse_alphanumeric_digit(num=nums[0]) + parse_alphanumeric_digit(num=nums[-1]))
    else:
        nums = re.findall(r"\d{1}", text)
        if not nums:
            return 0

        return int(nums[0] + nums[-1])


def parse_alphanumeric_digit(num: str) -> str:
    if num.isdigit():
        return num

    return str(NUMBER_WORDS.index(num))


def solve(puzzle_input=typing.List[str]) -> Solution:
    return Solution(
        first=sum_calibration_values(document=puzzle_input),
        second=sum_calibration_values(document=puzzle_input, parse_words=True),
    )
