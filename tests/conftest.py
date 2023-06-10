import importlib
import os
import pytest
import typing

from types import ModuleType


@pytest.fixture(scope="module")
def mock_puzzle_input(request) -> typing.List[str]:
    with open(file=request.fspath.strpath.replace(".py", ".txt"), mode="r") as f:
        return f.read().splitlines()


@pytest.fixture(scope="module")
def puzzle_module(request) -> ModuleType:
    package_name, year = request.fspath.dirname.split("/")[-2:]
    puzzle_name = request.fspath.purebasename.removeprefix("test_")
    return importlib.import_module(".".join([package_name, year, puzzle_name]))


@pytest.fixture(scope="module")
def project_directory() -> str:
    return os.path.split(os.path.dirname(__file__))[0]
