import re
import typing
from collections import namedtuple

from aoc_solver.object_types import Solution

Scorecard = namedtuple("Scorecard", ["card_number", "winning_numbers", "revealed_numbers"])

# --- Day 4: Scratchcards ---
# Source: https://adventofcode.com/2023/day/4


def total_score(scratchcards: typing.List[Scorecard]) -> int:
    scores = []
    for card in scratchcards:
        num_matches = -1
        for num in card.revealed_numbers:
            if num in card.winning_numbers:
                num_matches += 1

        if num_matches >= 0:
            scores.append(pow(2, num_matches))

    return sum(scores)


def count_total(scratchcards: typing.List[Scorecard]) -> int:
    num_copies = {}
    for card in scratchcards:
        if card.card_number not in num_copies:
            num_copies[card.card_number] = 0

        num_copies[card.card_number] += 1
        num_matches = 0

        for num in card.revealed_numbers:
            if num in card.winning_numbers:
                num_matches += 1

        for _ in range(num_copies[card.card_number]):
            for j in range(num_matches):
                card_number = card.card_number + j + 1
                if card_number not in num_copies:
                    num_copies[card_number] = 0
                num_copies[card_number] += 1

    return sum(num_copies.values())


def parse_input(puzzle: typing.List[str]) -> typing.List[Scorecard]:
    scratchcard_pattern = r"Card +\d+: (.+) \| (.+)"
    scratchcards = []
    for idx, line in enumerate(puzzle):
        winning_numbers, revealed_numbers = re.match(scratchcard_pattern, line).group(1, 2)

        scratchcards.append(
            Scorecard(
                card_number=idx,
                winning_numbers=cast_numbers(nums=winning_numbers),
                revealed_numbers=cast_numbers(nums=revealed_numbers),
            )
        )

    return scratchcards


def cast_numbers(nums: typing.List[str]) -> typing.List[int]:
    return [int(num) for num in nums.split()]


def solve(puzzle_input: typing.List[str]) -> Solution:
    scratchcards = parse_input(puzzle=puzzle_input)
    return Solution(
        first=total_score(scratchcards=scratchcards),
        second=count_total(scratchcards=scratchcards),
    )
