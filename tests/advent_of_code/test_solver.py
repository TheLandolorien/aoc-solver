from unittest.mock import patch
import pytest

from advent_of_code import solver


@patch("sys.argv", ["solve"])
def test_solve_raises_on_invalid_arguments() -> None:
    with pytest.raises(ValueError) as err:
        solver.solve()

    assert str(err.value) == "Usage: poetry run solve <PUZZLE_NAME>", "should provide ValueError details"


@patch("sys.argv", ["solve", "foo"])
@patch("importlib.import_module")
def test_solve_runs_solution_for_puzzle(mock_import_module) -> None:
    solver.solve()

    mock_import_module.assert_called_once_with(name="advent_of_code.foo"), "should load puzzle by name"
    mock_import_module.return_value.solve.assert_called_once(), "should call solve on puzzle module"
