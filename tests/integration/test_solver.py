from datetime import datetime
from unittest.mock import patch

from aoc_solver import solver


@patch("sys.argv", ["solve"])
@patch("aoc_solver.solver.datetime")
def test_solver_with_missing_puzzle(mock_datetime, project_directory, capsys):
    mock_datetime.now.return_value = datetime(2022, 12, 25)

    solver.solve()

    captured = capsys.readouterr()
    assert captured.out == (
        f"Saved puzzle input to {project_directory}/tests/aoc_solver/2022/test_day_25.txt\n"
        f"Saved puzzle input to {project_directory}/src/aoc_solver/2022/day_25.txt\n"
        f"Created puzzle module at {project_directory}/src/aoc_solver/2022/day_25.py\n"
        f"Created puzzle module at {project_directory}/tests/aoc_solver/2022/test_day_25.py\n"
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


@patch("sys.argv", ["solve", "2021", "1"])
def test_solver_with_integer_answers(capsys):
    solver.solve()

    captured = capsys.readouterr()
    assert captured.out == "Part One: The puzzle answer is 1228\nPart Two: The puzzle answer is 1257\n", f"should correctly cast integer answers"


@patch("sys.argv", ["solve", "2022", "5"])
def test_solver_with_string_answers(capsys):
    solver.solve()

    captured = capsys.readouterr()
    assert captured.out == (
        "Part One: The puzzle answer is VWLCWGSDQ\nPart Two: The puzzle answer is TCGLQSLPW\n"
    ), f"should correctly cast string answers"
