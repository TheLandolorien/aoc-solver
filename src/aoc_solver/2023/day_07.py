import typing

from collections import namedtuple
from enum import Enum
from itertools import groupby

from aoc_solver.object_types import Solution

CardValue = Enum("CardValue", ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"])
CardValueWild = Enum(
    "CardValueWild", ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
)
Rank = Enum(
    "Rank",
    [
        "HIGH_CARD",
        "ONE_PAIR",
        "TWO_PAIR",
        "THREE_OF_A_KIND",
        "FULL_HOUSE",
        "FOUR_OF_A_KIND",
        "FIVE_OF_A_KIND",
    ],
)
CardHand = namedtuple("CardHand", ["deal", "label", "bid"])


# --- Day 7: Camel Cards ---
# Source: https://adventofcode.com/2023/day/7
def calculate_total_winnings(raw_hands: typing.List[str], use_jokers: bool = False) -> int:
    ranked_hands = parse_hands(raw_hands=raw_hands, use_jokers=use_jokers)

    total_winnings = 0
    for idx, hand in enumerate(ranked_hands):
        total_winnings += hand.bid * (idx + 1)

    return total_winnings


def parse_hands(raw_hands: typing.List[str], use_jokers: bool) -> typing.List[CardHand]:
    hands = []
    for hand in raw_hands:
        deal, bid = hand.split()
        label = evaluate_hand(deal=deal, use_jokers=use_jokers).name
        hands.append(CardHand(deal=deal, label=label, bid=int(bid)))

    card_values = CardValueWild if use_jokers else CardValue
    return sorted(
        hands,
        key=lambda x: (
            Rank[x.label].value,
            card_values[x.deal[0]].value,
            card_values[x.deal[1]].value,
            card_values[x.deal[2]].value,
            card_values[x.deal[3]].value,
            card_values[x.deal[4]].value,
        ),
    )


def evaluate_hand(deal: str, use_jokers: bool) -> int:
    grouped_cards = [list(g) for _, g in groupby(sorted(deal))]
    num_wildcards = deal.count("J") if use_jokers else 0
    score = Rank.FIVE_OF_A_KIND
    if len(grouped_cards) == 5:
        score = Rank.ONE_PAIR if num_wildcards else Rank.HIGH_CARD
    elif len(grouped_cards) == 4:
        score = Rank.THREE_OF_A_KIND if num_wildcards else Rank.ONE_PAIR
    elif len(grouped_cards) == 3:
        if any([len(group) == 3 for group in grouped_cards]):
            score = Rank.FOUR_OF_A_KIND if num_wildcards else Rank.THREE_OF_A_KIND
        else:
            if num_wildcards == 2:
                score = Rank.FOUR_OF_A_KIND
            elif num_wildcards == 1:
                score = Rank.FULL_HOUSE
            else:
                score = Rank.TWO_PAIR
    elif len(grouped_cards) == 2:
        if any([len(group) == 4 for group in grouped_cards]):
            score = Rank.FIVE_OF_A_KIND if num_wildcards else Rank.FOUR_OF_A_KIND
        else:
            if num_wildcards == 3 or num_wildcards == 2:
                score = Rank.FIVE_OF_A_KIND
            elif num_wildcards == 1:
                score = Rank.FOUR_OF_A_KIND
            else:
                score = Rank.FULL_HOUSE
    return score


def solve(puzzle_input: typing.List[str]) -> Solution:
    return Solution(
        first=calculate_total_winnings(raw_hands=puzzle_input),
        second=calculate_total_winnings(raw_hands=puzzle_input, use_jokers=True),
    )
