import pytest
import typing

from aoc_solver.utilities import read_lines


@pytest.fixture(scope="module")
def mock_puzzle_input(request) -> typing.List[str]:
    return read_lines(filepath=request.fspath.strpath.replace(".py", ".txt"))
