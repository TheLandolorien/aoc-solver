import os
import requests
import typing

from html.parser import HTMLParser
from importlib import util as importlib_util
from importlib.machinery import ModuleSpec
from string import Template

from aoc_solver.object_types import Solution, PuzzleMetadata

SRC_PATH, PACKAGE_NAME = os.path.split(os.path.dirname(__file__))


class ExamplePuzzleInputParser(HTMLParser):
    example_input = None
    should_extract_example_input = False

    puzzle_title = None
    should_extract_puzzle_title = False

    def handle_starttag(self, tag, _) -> None:
        if tag == "h2":
            self.should_extract_puzzle_title = True

    def handle_data(self, data):
        if self.should_extract_puzzle_title:
            self.puzzle_title = data
            self.should_extract_puzzle_title = False
        elif self.should_extract_example_input and data != "\n":
            self.example_input = data
            self.should_extract_example_input = False
        elif "For example" in data:
            self.should_extract_example_input = True


def _find_puzzle_module(year: int, day: int) -> typing.Union[ModuleSpec, None]:
    return importlib_util.find_spec(name=".".join([PACKAGE_NAME, str(year), f"day_{_format_day(day)}"]))


def _format_day(day: typing.Union[int, str]) -> str:
    return str(day).zfill(2)


def _get_puzzle_file_path(metadata: PuzzleMetadata, is_test: bool = False, is_module: bool = True) -> str:
    top_directory = SRC_PATH
    filename = f"day_{_format_day(metadata.day)}"
    file_extension = "py" if is_module else "txt"

    if is_test:
        top_directory = os.path.join(os.path.dirname(SRC_PATH), "tests")
        filename = f"test_{filename}"

    return os.path.join(top_directory, PACKAGE_NAME, str(metadata.year), f"{filename}.{file_extension}")


def clone_template(metadata: PuzzleMetadata, is_test: bool = False) -> None:
    template_name = "day_n.py.template"
    if is_test:
        template_name = f"test_{template_name}"

    with open(file=os.path.join(SRC_PATH, "templates", template_name), mode="r") as f:
        template_contents = Template(f.read())

    module_path = _get_puzzle_file_path(metadata=metadata, is_test=is_test, is_module=True)
    os.makedirs(name=os.path.dirname(module_path), exist_ok=True)
    with open(file=module_path, mode="w") as f:
        f.write(template_contents.substitute({"title": metadata.title, "year": metadata.year, "day": metadata.day}))

    print(f"Downloaded missing puzzle{' test' if is_test else ''} module to {module_path} 🎉")


def read_puzzle_input(metadata: PuzzleMetadata, is_test: bool = False) -> typing.List[str]:
    puzzle_input_path = _get_puzzle_file_path(metadata=metadata, is_test=is_test, is_module=False)

    with open(file=puzzle_input_path, mode="r") as f:
        return f.read().splitlines()


def get_puzzle_metadata(year: int, day: int) -> PuzzleMetadata:
    parser = ExamplePuzzleInputParser()
    parser.feed(requests.get(url=f"https://adventofcode.com/{year}/day/{day}").text)
    parser.close()

    return PuzzleMetadata(title=parser.puzzle_title, year=year, day=day, example_input=parser.example_input, puzzle_input=None)


def save_puzzle_input(metadata: PuzzleMetadata, is_test: bool = False) -> PuzzleMetadata:
    if is_test:
        puzzle_input_path = _get_puzzle_file_path(metadata=metadata, is_test=is_test, is_module=False)
        if os.path.isfile(path=puzzle_input_path):
            return None

        os.makedirs(name=os.path.dirname(puzzle_input_path), exist_ok=True)
        with open(file=puzzle_input_path, mode="w") as f:
            f.write(metadata.example_input)

        print(f"Saved missing puzzle input to {puzzle_input_path} 🎉")


def run_solution(year: int, day: int) -> Solution:
    if puzzle_spec := _find_puzzle_module(year=year, day=day):
        puzzle_module = importlib_util.module_from_spec(spec=puzzle_spec)
        puzzle_spec.loader.exec_module(module=puzzle_module)

        metadata = PuzzleMetadata(title=None, year=year, day=day, example_input=None, puzzle_input=None)
        return puzzle_module.solve(puzzle_input=read_puzzle_input(metadata=metadata))
    else:
        # TODO: Update Docs
        metadata = get_puzzle_metadata(year=year, day=day)
        save_puzzle_input(metadata=metadata, is_test=True)
        clone_template(metadata=metadata, is_test=True)
        clone_template(metadata=metadata)
        # TODO: Download real puzzle input (requires OAuth)
        return "\nERROR: Unable to auto-download puzzle input. Please manually download and try again."
