import os
import typing
import argparse

from datetime import datetime, timedelta, timezone

from aoc_solver import utilities, puzzle_manager

SRC_PATH, PACKAGE_NAME = os.path.split(os.path.dirname(__file__))


def run() -> None:
    year, day = _parse_puzzle_date()
    puzzle = _load_puzzle(year=year, day=day)

    first, second = puzzle.solve(puzzle_input=puzzle_manager.read_puzzle_input(year=year, day=day))
    print(f"Part One: The puzzle answer is {first}")
    print(f"Part Two: The puzzle answer is {second}")


def _get_max_puzzle_date() -> typing.Tuple[int, int]:
    now = datetime.now(timezone(timedelta(hours=-5)))

    year = now.year
    day = now.day

    if now.month != 12:
        year -= 1
        day = 25

    if now.day > 25:
        day = 25

    return [year, day]


def _get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="aoc-solver",
        description="Review your Advent of Code solutions",
    )

    parser.add_argument(
        "--date",
        type=int,
        nargs=2,
        help="year and day of puzzle: YYYY DD",
        metavar=("year", "day"),
    )

    return parser


def _load_puzzle(year: int, day: int) -> None:
    puzzle_module = utilities.load_module(year=year, day=day)

    if not puzzle_module:
        puzzle_manager.create_puzzle_resources(year=year, day=day)
        puzzle_module = utilities.load_module(year=year, day=day)

    return puzzle_module


def _parse_puzzle_date() -> typing.Tuple[int, int]:
    parser = _get_parser()
    args = parser.parse_args()

    if not args.date:
        return _get_max_puzzle_date()

    year, day = args.date

    _raise_for_invalid_date(year=year, day=day)

    return year, day


def _raise_for_invalid_date(year: int, day: int) -> None:
    parser = _get_parser()
    max_year, max_day = _get_max_puzzle_date()

    if year < 2015:
        parser.error(f"Invalid year {year}: Advent of Code began in 2015")

    if day > 25:
        parser.error(f"Invalid day {day}: Advent of Code is only 25 days per year")

    if year > max_year or (year == max_year and day > max_day):
        parser.error(f"Invalid puzzle {year} day {day}: Not yet released")
