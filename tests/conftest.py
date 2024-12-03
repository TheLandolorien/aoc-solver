import importlib
import os
import pytest
import typing
import glob

from types import ModuleType


@pytest.fixture(scope="module")
def mock_puzzle_inputs(request) -> typing.List[typing.List[str]]:
    dirname, basename = os.path.split(request.fspath.strpath)
    examples = []

    for strpath in sorted(glob.glob(pathname=f"{dirname}/{basename.replace('.py', '*.txt')}")):
        with open(file=strpath, mode="r") as f:
            examples.append(f.read().splitlines())

    return examples


@pytest.fixture(scope="module")
def puzzle_module(request) -> ModuleType:
    year = request.fspath.dirname.split("/")[-1]
    puzzle_name = request.fspath.purebasename.removeprefix("test_")
    return importlib.import_module(".".join(["aoc_solver", year, puzzle_name]))


@pytest.fixture(scope="module")
def project_directory() -> str:
    return os.path.split(os.path.dirname(__file__))[0]
