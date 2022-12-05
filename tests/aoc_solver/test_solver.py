import os
import pytest

from unittest.mock import patch

from aoc_solver import solver


@patch("sys.argv", ["solve"])
def test_solve_raises_when_missing_all_arguments():
    with pytest.raises(ValueError) as err:
        solver.solve()

    assert str(err.value) == "Usage: poetry run solve <YYYY> <PUZZLE_NAME>", "should provide ValueError details"


@patch("sys.argv", ["solve", "2020"])
def test_solve_raises_when_missing_puzzle_name():
    with pytest.raises(ValueError) as err:
        solver.solve()

    assert str(err.value) == "Usage: poetry run solve <YYYY> <PUZZLE_NAME>", "should provide ValueError details"


@patch("sys.argv", ["solve", "ABCD", "foo"])
def test_solve_raises_for_invalid_year():
    with pytest.raises(ValueError) as err:
        solver.solve()

    assert str(err.value) == "Usage: poetry run solve <YYYY> <PUZZLE_NAME>\nInvalid Year: ABCD", "should provide ValueError details"


@patch("sys.argv", ["solve", "2015", "foo"])
@patch("aoc_solver.solver.read_lines", return_value=["A Y", "B X", "C Z"])
@patch("importlib.import_module")
def test_solve_runs_solution_for_puzzle(mock_import_module, mock_read_lines):
    solver.solve()

    project_root_directory = os.path.split(os.path.dirname(os.path.dirname(__file__)))[0]
    mock_read_lines.assert_called_once_with(filepath=f"{project_root_directory}/src/aoc_solver/2015/foo.txt")
    mock_import_module.assert_called_once_with(name="aoc_solver.2015.foo")
    mock_import_module.return_value.solve.assert_called_once_with(puzzle_input=mock_read_lines.return_value)
