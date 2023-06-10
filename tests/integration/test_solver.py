import pytest
from unittest.mock import patch

import os
import shutil
from datetime import datetime

from aoc_solver import solver


@pytest.fixture
def mock_missing_puzzle(project_directory, tmp_path):
    original_module_location = os.path.join(project_directory, "src/aoc_solver/2021")
    temporary_module_location = tmp_path / "src"
    os.rename(original_module_location, temporary_module_location)
    os.mkdir(original_module_location)

    original_test_location = os.path.join(project_directory, "tests/aoc_solver/2021")
    temporary_test_location = tmp_path / "tests"
    os.rename(original_test_location, temporary_test_location)
    os.mkdir(original_test_location)

    yield

    shutil.rmtree(original_module_location)
    os.mkdir(original_module_location)
    os.rename(temporary_module_location, original_module_location)

    shutil.rmtree(original_test_location)
    os.mkdir(original_test_location)
    os.rename(temporary_test_location, original_test_location)


@patch("sys.argv", ["solve"])
@patch("aoc_solver.solver.datetime")
def test_solver_with_missing_puzzle(mock_datetime, mock_missing_puzzle, project_directory, capsys):
    mock_datetime.now.return_value = datetime(2021, 12, 1)

    solver.solve()

    captured = capsys.readouterr()
    assert captured.out == (
        f"Saved puzzle input to {project_directory}/tests/aoc_solver/2021/test_day_01.txt\n"
        f"Saved puzzle input to {project_directory}/src/aoc_solver/2021/day_01.txt\n"
        f"Created puzzle module at {project_directory}/src/aoc_solver/2021/day_01.py\n"
        f"Created puzzle module at {project_directory}/tests/aoc_solver/2021/test_day_01.py\n"
        "Part One: The puzzle answer is None\n"
        "Part Two: The puzzle answer is None\n"
    ), f"should downloading missing puzzle resources and default answers to None"


@patch("sys.argv", ["solve"])
@patch("aoc_solver.solver.datetime")
def test_solver_with_existing_puzzle(mock_datetime, capsys):
    mock_datetime.now.return_value = datetime(2022, 12, 4)

    solver.solve()

    captured = capsys.readouterr()
    assert captured.out == "Part One: The puzzle answer is 567\nPart Two: The puzzle answer is 907\n", f"should use existing answers"


@patch("sys.argv", ["solve", "2022", "1"])
def test_solver_with_integer_answers(capsys):
    solver.solve()

    captured = capsys.readouterr()
    assert captured.out == "Part One: The puzzle answer is 65912\nPart Two: The puzzle answer is 195625\n", f"should correctly cast integer answers"


@patch("sys.argv", ["solve", "2022", "5"])
def test_solver_with_string_answers(capsys):
    solver.solve()

    captured = capsys.readouterr()
    assert captured.out == (
        "Part One: The puzzle answer is VWLCWGSDQ\nPart Two: The puzzle answer is TCGLQSLPW\n"
    ), f"should correctly cast string answers"
