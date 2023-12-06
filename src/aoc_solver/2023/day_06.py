import typing

from aoc_solver.object_types import Solution

# --- Day 6: Wait For It ---
# Source: https://adventofcode.com/2023/day/6


def determine_num_ways_to_win(puzzle_input: typing.List[str], is_single_race: bool = False) -> int:
    document = parse_input(puzzle=puzzle_input, is_single_race=is_single_race)
    margin_of_error = 1
    for race in document:
        duration, record_distance = map(int, race)
        num_ways_to_win = 0
        for hold in range(duration + 1):
            travel = duration - hold
            distance = travel * hold
            if distance > record_distance:
                num_ways_to_win += 1
        margin_of_error *= num_ways_to_win

    return margin_of_error


def parse_input(puzzle: typing.List[str], is_single_race: bool) -> typing.List[typing.Tuple[str]]:
    if is_single_race:
        times = [puzzle[0].split(":")[1].replace(" ", "")]
        distances = [puzzle[1].split(":")[1].replace(" ", "")]
    else:
        times = puzzle[0].split(":")[1].split()
        distances = puzzle[1].split(":")[1].split()

    return list(zip(times, distances))


def solve(puzzle_input: typing.List[str]) -> Solution:
    return Solution(
        first=determine_num_ways_to_win(puzzle_input=puzzle_input),
        second=determine_num_ways_to_win(puzzle_input=puzzle_input, is_single_race=True),
    )
