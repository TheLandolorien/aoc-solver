from unittest.mock import patch
import pytest

from advent_of_code import solver


@patch("sys.argv", ["solve"])
def test_solve_raises_when_missing_all_arguments() -> None:
    with pytest.raises(ValueError) as err:
        solver.solve()

    assert str(err.value) == "Usage: poetry run solve <YYYY> <PUZZLE_NAME>", "should provide ValueError details"


@patch("sys.argv", ["solve", "2020"])
def test_solve_raises_when_missing_puzzle_name() -> None:
    with pytest.raises(ValueError) as err:
        solver.solve()

    assert str(err.value) == "Usage: poetry run solve <YYYY> <PUZZLE_NAME>", "should provide ValueError details"


@patch("sys.argv", ["solve", "ABCD", "foo"])
def test_solve_raises_for_invalid_year() -> None:
    with pytest.raises(ValueError) as err:
        solver.solve()

    assert str(err.value) == "Usage: poetry run solve <YYYY> <PUZZLE_NAME>\nInvalid Year: ABCD", "should provide ValueError details"


@patch("sys.argv", ["solve", "2015", "foo"])
@patch("importlib.import_module")
def test_solve_runs_solution_for_puzzle(mock_import_module) -> None:
    solver.solve()

    mock_import_module.assert_called_once_with(name="advent_of_code.2015.foo"), "should load puzzle by name"
    mock_import_module.return_value.solve.assert_called_once(), "should call solve on puzzle module"
