import os
import typing
from advent_of_code import types

from advent_of_code.utilities import read_lines
from advent_of_code.types import RPSPlay

PUZZLE_NAME = os.path.splitext(os.path.basename(__file__))[0]

RPS_MAP = {
    "A": ("rock", 1),
    "B": ("paper", 2),
    "C": ("scissors", 3),
    "X": ("rock", 1),
    "Y": ("paper", 2),
    "Z": ("scissors", 3),
}


def score_matches(puzzle_input: typing.List[str]) -> int:
    matches = [play.split(" ") for play in "".join(puzzle_input).strip().split("\n")]
    return sum([calculate_score(match) for match in matches])


def calculate_score(match: typing.List[str]) -> str:
    opponent, suggested = map(lambda play: RPSPlay(*RPS_MAP[play]), match)
    outcome = determine_outcome(play=suggested.shape, counter=opponent.shape)

    score = suggested.score
    if outcome == "win":
        score += 6
    elif outcome == "draw":
        score += 3

    return score


def determine_outcome(play: str, counter: str) -> str:
    if play == counter:
        return "draw"
    elif (play == "rock" and counter == "scissors") or (play == "scissors" and counter == "paper") or (play == "paper" and counter == "rock"):
        return "win"

    return "lose"


def solve() -> types.Solution:
    puzzle_input = read_lines(filepath=os.path.join(os.path.dirname(__file__), f"{PUZZLE_NAME}.txt"))
    return types.Solution(first=score_matches(puzzle_input=puzzle_input), second=None)
