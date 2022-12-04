import importlib
import pytest
import typing
from types import ModuleType

from aoc_solver.utilities import read_lines


@pytest.fixture(scope="module")
def mock_puzzle_input(request) -> typing.List[str]:
    return read_lines(filepath=request.fspath.strpath.replace(".py", ".txt"))


@pytest.fixture(scope="module")
def puzzle_module(request) -> ModuleType:
    package_name, year = request.fspath.dirname.split("/")[-2:]
    puzzle_name = request.fspath.purebasename.removeprefix("test_")
    return importlib.import_module(".".join([package_name, year, puzzle_name]))
