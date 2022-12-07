from types import FunctionType
import typing

from aoc_solver.utilities import Solution

# --- Day 2: Rock Paper Scissors ---
# Source: https://adventofcode.com/2022/day/2

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


def score_matches(matches: typing.List[typing.List[str]], calculator: FunctionType) -> int:
    return sum([calculator(*match) for match in matches])


def solve(puzzle_input=typing.List[str]) -> Solution:
    matches = [match.split(" ") for match in puzzle_input]

    return Solution(
        first=score_matches(matches=matches, calculator=calculate_score_by_plays),
        second=score_matches(matches=matches, calculator=calculate_score_by_outcomes),
    )
