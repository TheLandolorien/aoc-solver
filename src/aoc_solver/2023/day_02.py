import math
import typing

from aoc_solver.object_types import Solution

# --- Day 2: Cube Conundrum ---
# Source: https://adventofcode.com/2023/day/2

GAME_SCENARIO = {"red": 12, "green": 13, "blue": 14}


def sum_possible_game_ids(puzzle_input: typing.List[str]) -> int:
    game_record = parse_input(puzzle=puzzle_input)
    possible_game_ids = []
    for idx, game in enumerate(game_record):
        max_draws = find_max_drawn(game=game)
        if is_possible_game(max_draws=max_draws):
            possible_game_ids.append(idx + 1)

    return sum(possible_game_ids)


def sum_cube_set_powers(puzzle_input: typing.List[str]) -> int:
    game_record = parse_input(puzzle=puzzle_input)
    set_powers = []
    for game in game_record:
        max_draws = find_max_drawn(game=game)
        set_powers.append(math.prod(max_draws.values()))

    return sum(set_powers)


def find_max_drawn(game: typing.List[typing.Dict[str, int]]) -> typing.Dict[str, int]:
    max_draws = {}
    for cube_set in game:
        for color, num_drawn in cube_set.items():
            if color not in max_draws or num_drawn > max_draws[color]:
                max_draws[color] = num_drawn
    return max_draws


def is_possible_game(max_draws: typing.Dict[str, int]) -> bool:
    return (
        GAME_SCENARIO["blue"] >= max_draws.get("blue", 0)
        and GAME_SCENARIO["red"] >= max_draws.get("red", 0)
        and GAME_SCENARIO["green"] >= max_draws.get("green", 0)
    )


def parse_input(puzzle=typing.List[str]) -> typing.List[typing.List[typing.Dict[str, int]]]:
    """Transform cube sets into a list of dictionaries

    Example:
        Game 1: 3 blue, 4 red; 1 red; 2 green => [{'blue': 3, 'red': 4}, {'red': 1}, {'green': 2}]
    """
    return [
        [
            {cubes.split(" ")[1]: int(cubes.split(" ")[0]) for cubes in cube_set.split(", ")}
            for cube_set in game.split(": ")[-1].split("; ")
        ]
        for game in puzzle
    ]


def solve(puzzle_input: typing.List[str]) -> Solution:
    return Solution(
        first=sum_possible_game_ids(puzzle_input=puzzle_input),
        second=sum_cube_set_powers(puzzle_input=puzzle_input),
    )
