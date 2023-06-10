import os
import typing
import requests

from string import Template

from aoc_solver import utilities
from aoc_solver.session import authenticator
from aoc_solver.object_types import ExamplePuzzleInputParser, PuzzleMetadata

SRC_PATH, PACKAGE_NAME = os.path.split(os.path.dirname(__file__))


def _build_puzzle_metadata(year: int, day: int) -> PuzzleMetadata:
    page = _parse_puzzle_page(year=year, day=day)
    return PuzzleMetadata(
        title=page.puzzle_title,
        year=year,
        day=day,
        formatted_day=str(day).zfill(2),
        example_input=page.example_input,
        puzzle_input=_get_puzzle_input(year=year, day=day),
    )


def _build_puzzle_resource_path(
    year: int, day: int, is_test: bool = False, is_module: bool = False
) -> str:
    top_directory = SRC_PATH
    filename = f"day_{_format_day(day)}"
    file_extension = "py" if is_module else "txt"

    if is_test:
        top_directory = os.path.join(os.path.dirname(SRC_PATH), "tests")
        filename = f"test_{filename}"

    return os.path.join(top_directory, PACKAGE_NAME, str(year), f"{filename}.{file_extension}")


def _clone_templates(metadata: PuzzleMetadata) -> None:
    templates = ["day_n.py.template", "test_day_n.py.template"]

    for template in templates:
        is_test = template.startswith("test")
        module_path = _build_puzzle_resource_path(
            year=metadata.year, day=metadata.day, is_test=is_test, is_module=True
        )

        if not os.path.isfile(path=module_path):
            with open(file=os.path.join(SRC_PATH, "templates", template), mode="r") as f:
                template_contents = Template(f.read())

            os.makedirs(name=os.path.dirname(module_path), exist_ok=True)
            with open(file=module_path, mode="w") as f:
                f.write(
                    template_contents.substitute(
                        {"title": metadata.title, "year": metadata.year, "day": metadata.day}
                    )
                )

            print(f"Created puzzle module at {module_path}")


def _format_day(day: int) -> str:
    return str(day).zfill(2)


def _get_puzzle_input(year: int, day: int, auth_provider: str = "github") -> str:
    session_cookie = authenticator.authenticate(provider=auth_provider)

    session = requests.Session()
    session.cookies.set(name="session", value=session_cookie)

    puzzle_response = session.get(url=f"https://adventofcode.com/{year}/day/{day}/input")
    puzzle_response.raise_for_status()

    return puzzle_response.text


def _parse_puzzle_page(year: int, day: int) -> ExamplePuzzleInputParser:
    parser = ExamplePuzzleInputParser()
    parser.feed(requests.get(url=f"https://adventofcode.com/{year}/day/{day}").text)
    parser.close()

    return parser


def _save_puzzle_inputs(metadata: PuzzleMetadata) -> PuzzleMetadata:
    _write_puzzle_input(
        contents=metadata.example_input,
        path=_build_puzzle_resource_path(year=metadata.year, day=metadata.day, is_test=True),
    )

    _write_puzzle_input(
        contents=metadata.puzzle_input,
        path=_build_puzzle_resource_path(year=metadata.year, day=metadata.day),
    )


def _write_puzzle_input(contents: str, path: str) -> None:
    if not os.path.isfile(path=path):
        os.makedirs(name=os.path.dirname(path), exist_ok=True)

        with open(file=path, mode="w") as f:
            f.write(contents)

        print(f"Saved puzzle input to {path}")


def create_puzzle_resources(year: int, day: int) -> None:
    # TODO: Auto-create new year if no puzzles exists for it
    metadata = _build_puzzle_metadata(year=year, day=day)
    _save_puzzle_inputs(metadata=metadata)
    _clone_templates(metadata=metadata)


def read_puzzle_input(year: int, day: int) -> typing.List[str]:
    puzzle_input_path = _build_puzzle_resource_path(year=year, day=day)
    return utilities.read_file(path=puzzle_input_path)
