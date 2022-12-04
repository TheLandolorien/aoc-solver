import os
import typing
from advent_of_code import types

from advent_of_code.utilities import read_lines

PUZZLE_NAME = os.path.splitext(os.path.basename(__file__))[0]

SHAPE_SCORES = {"rock": 1, "paper": 2, "scissors": 3}
OUTCOME_SCORES = {"lose": 0, "draw": 3, "win": 6}
COUNTER_MAP = {"A": "rock", "B": "paper", "C": "scissors"}
PLAY_MAP = {"X": "rock", "Y": "paper", "Z": "scissors"}
OUTCOME_MAP = {"X": "lose", "Y": "draw", "Z": "win"}


def calculate_score_by_outcomes(encrypted_counter: str, encrypted_outcome: str) -> int:
    counter = COUNTER_MAP[encrypted_counter]
    outcome = OUTCOME_MAP[encrypted_outcome]

    return SHAPE_SCORES[determine_play(counter=counter, outcome=outcome)] + OUTCOME_SCORES[outcome]


def calculate_score_by_plays(encrypted_counter: str, encrypted_play: str) -> int:
    counter = COUNTER_MAP[encrypted_counter]
    play = PLAY_MAP[encrypted_play]

    return SHAPE_SCORES[play] + OUTCOME_SCORES[determine_outcome(counter=counter, play=play)]


def determine_outcome(counter: str, play: str) -> str:
    if play == counter:
        return "draw"
    elif (play == "rock" and counter == "scissors") or (play == "scissors" and counter == "paper") or (play == "paper" and counter == "rock"):
        return "win"

    return "lose"


def determine_play(counter: str, outcome: str) -> str:
    if (outcome == "win" and counter == "rock") or (outcome == "lose" and counter == "scissors"):
        return "paper"
    elif (outcome == "win" and counter == "paper") or (outcome == "lose" and counter == "rock"):
        return "scissors"
    elif (outcome == "win" and counter == "scissors") or (outcome == "lose" and counter == "paper"):
        return "rock"

    return counter


def score_matches(puzzle_input: typing.List[str], by_plays: bool = True) -> int:
    matches = [play.split(" ") for play in puzzle_input]
    calculation_func = calculate_score_by_plays if by_plays else calculate_score_by_outcomes

    return sum([calculation_func(*match) for match in matches])


def solve() -> types.Solution:
    puzzle_input = read_lines(filepath=os.path.join(os.path.dirname(__file__), f"{PUZZLE_NAME}.txt"))
    return types.Solution(first=score_matches(puzzle_input=puzzle_input), second=score_matches(puzzle_input=puzzle_input, by_plays=False))
