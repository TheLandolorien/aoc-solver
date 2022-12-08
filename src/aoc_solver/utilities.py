import os
import requests
import typing

from importlib import util as importlib_util
from html.parser import HTMLParser

from collections import namedtuple
from importlib.machinery import ModuleSpec


SRC_PATH, PACKAGE_NAME = os.path.split(os.path.dirname(__file__))

Solution = namedtuple("Solution", ["first", "second"])


class ExamplePuzzleInputParser(HTMLParser):
    example_input = None
    should_extract_example_input = False

    def handle_data(self, data):
        if self.should_extract_example_input and data != "\n":
            self.example_input = data
            self.should_extract_example_input = False
        elif "For example" in data:
            self.should_extract_example_input = True


def _find_puzzle_module(year: int, day: int) -> typing.Union[ModuleSpec, None]:
    return importlib_util.find_spec(name=".".join([PACKAGE_NAME, str(year), f"day_{_format_day(day)}"]))


def _format_day(day: typing.Union[int, str]) -> str:
    return str(day).zfill(2)


def _get_puzzle_input_path(year: int, day: int, is_test: bool = False) -> str:
    top_directory = SRC_PATH
    puzzle_input_filename = f"day_{_format_day(day)}.txt"

    if is_test:
        top_directory = os.path.join(os.path.dirname(SRC_PATH), "tests")
        puzzle_input_filename = f"test_{puzzle_input_filename}"

    return os.path.join(top_directory, PACKAGE_NAME, str(year), puzzle_input_filename)


def read_puzzle_input(year: int, day: int, is_test: bool = False) -> typing.List[str]:
    puzzle_input_path = _get_puzzle_input_path(year=year, day=day, is_test=is_test)

    with open(file=puzzle_input_path, mode="r") as f:
        return f.read().splitlines()


def download_puzzle_input(year: str, day: str, is_test: bool = False) -> None:
    puzzle_input_path = _get_puzzle_input_path(year=year, day=day, is_test=is_test)
    if os.path.isfile(path=puzzle_input_path):
        return None

    raw_puzzle_input = None
    if is_test:
        parser = ExamplePuzzleInputParser()
        parser.feed(requests.get(url=f"https://adventofcode.com/{year}/day/{day}").text)
        parser.close()

        raw_puzzle_input = parser.example_input
    # TODO: Write non-test download logic (requires OAuth)

    if raw_puzzle_input:
        os.makedirs(name=os.path.dirname(puzzle_input_path), exist_ok=True)
        with open(file=puzzle_input_path, mode="w") as f:
            f.write(raw_puzzle_input)

    print(f"Downloaded missing puzzle input to {puzzle_input_path} 🎉\n")


def run_solution(year: int, day: int) -> Solution:
    if puzzle_spec := _find_puzzle_module(year=year, day=day):
        puzzle_module = importlib_util.module_from_spec(spec=puzzle_spec)
        puzzle_spec.loader.exec_module(module=puzzle_module)

        return puzzle_module.solve(puzzle_input=read_puzzle_input(year=year, day=day))
    else:
        download_puzzle_input(year=year, day=day, is_test=True)
        # TODO: Download real puzzle input
        # TODO: Generate test module
        # TODO: Generate puzzle module
        return "ERROR: Unable to create all missing puzzle resources.\nPlease manually create puzzle modules and tests and try again."
