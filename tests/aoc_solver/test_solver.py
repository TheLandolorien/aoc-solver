import os
import pytest

from unittest.mock import patch

from aoc_solver import solver


@pytest.mark.parametrize(
    "scenario,invalid_args,additional_error_message",
    [
        ("raise when missing all arguments", ["solve"], ""),
        ("raise when missing puzzle name", ["solve", "2020"], ""),
        ("raise when given invalid year", ["solve", "ABCD", "foo"], "\nInvalid Year: ABCD"),
    ],
)
def test_raise_for_invalid_arguments(scenario, invalid_args, additional_error_message):
    patcher = patch("sys.argv", invalid_args)

    patcher.start()
    with pytest.raises(ValueError) as err:
        solver.solve()

    assert str(err.value) == f"Usage: poetry run solve <YYYY> <PUZZLE_NAME>{additional_error_message}", f"should {scenario}"
    patcher.stop()


@patch("sys.argv", ["solve", "2015", "foo"])
@patch("aoc_solver.solver.read_lines", return_value=["A Y", "B X", "C Z"])
@patch("importlib.import_module")
def test_solve_runs_solution_for_puzzle(mock_import_module, mock_read_lines):
    solver.solve()

    project_root_directory = os.path.split(os.path.dirname(os.path.dirname(__file__)))[0]
    mock_read_lines.assert_called_once_with(filepath=f"{project_root_directory}/src/aoc_solver/2015/foo.txt")
    mock_import_module.assert_called_once_with(name="aoc_solver.2015.foo")
    mock_import_module.return_value.solve.assert_called_once_with(puzzle_input=mock_read_lines.return_value)
