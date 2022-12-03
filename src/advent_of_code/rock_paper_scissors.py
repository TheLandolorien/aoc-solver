import os
import typing
from advent_of_code import types

from advent_of_code.utilities import read_lines
from advent_of_code.types import RPSPlay

PUZZLE_NAME = os.path.splitext(os.path.basename(__file__))[0]

# TODO: Create Score Maps and Column Maps
RPS_MAP = {
    "A": ("rock", 1),
    "B": ("paper", 2),
    "C": ("scissors", 3),
    "X": ("rock", 1),
    "Y": ("paper", 2),
    "Z": ("scissors", 3),
}

CORRECTED_RPS_MAP = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}


def score_matches_by_play(puzzle_input: typing.List[str]) -> int:
    matches = [play.split(" ") for play in "".join(puzzle_input).strip().split("\n")]
    return sum([calculate_score_by_play(match) for match in matches])


def calculate_score_by_play(match: typing.List[str]) -> int:
    opponent, suggested = map(lambda play: RPSPlay(*RPS_MAP[play]), match)
    outcome = determine_outcome(play=suggested.shape, counter=opponent.shape)

    score = suggested.score
    if outcome == "win":
        score += 6
    elif outcome == "draw":
        score += 3

    return score


def score_matches_by_outcome(puzzle_input: typing.List[str]) -> int:
    matches = [play.split(" ") for play in "".join(puzzle_input).strip().split("\n")]
    return sum([calculate_score_by_outcome(match) for match in matches])


def calculate_score_by_outcome(match: typing.List[str]) -> int:
    opponent, suggestion = map(lambda x: CORRECTED_RPS_MAP[x], match)
    play = determine_play(counter=opponent, outcome=suggestion)

    shape_scores = {"rock": 1, "paper": 2, "scissors": 3}

    score = shape_scores[play]
    if suggestion == "win":
        score += 6
    elif suggestion == "draw":
        score += 3

    return score


def determine_play(counter: str, outcome: str) -> str:
    if (outcome == "win" and counter == "rock") or (outcome == "lose" and counter == "scissors"):
        return "paper"
    elif (outcome == "win" and counter == "paper") or (outcome == "lose" and counter == "rock"):
        return "scissors"
    elif (outcome == "win" and counter == "scissors") or (outcome == "lose" and counter == "paper"):
        return "rock"

    return counter


def determine_outcome(play: str, counter: str) -> str:
    if play == counter:
        return "draw"
    elif (play == "rock" and counter == "scissors") or (play == "scissors" and counter == "paper") or (play == "paper" and counter == "rock"):
        return "win"

    return "lose"


def solve() -> types.Solution:
    puzzle_input = read_lines(filepath=os.path.join(os.path.dirname(__file__), f"{PUZZLE_NAME}.txt"))
    return types.Solution(first=score_matches_by_play(puzzle_input=puzzle_input), second=score_matches_by_outcome(puzzle_input=puzzle_input))
