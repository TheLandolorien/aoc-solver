from unittest.mock import patch
import pytest

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
@patch("importlib.import_module")
def test_solve_runs_solution_for_puzzle(mock_import_module):
    solver.solve()

    mock_import_module.assert_called_once_with(name="aoc_solver.2015.foo"), "should load puzzle by name"
    mock_import_module.return_value.solve.assert_called_once(), "should call solve on puzzle module"
