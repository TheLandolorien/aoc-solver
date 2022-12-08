import pytest
from unittest.mock import mock_open, patch


from aoc_solver import utilities


@pytest.mark.parametrize(
    "scenario,year,day,is_test,expected_path",
    [
        ("reading real puzzle input by default", 2022, 1, None, "src/aoc_solver/2022/day_01.txt"),
        ("reading example puzzle input with override", 2021, 2, True, "tests/aoc_solver/2021/test_day_02.txt"),
        ("reading real puzzle input with override", 2020, 3, False, "src/aoc_solver/2020/day_03.txt"),
    ],
)
@patch("builtins.open", new_callable=mock_open, read_data="A\nB\n\nC\n")
def test_read_puzzle_input(mock_open, scenario, year, day, is_test, expected_path, project_directory):
    lines = utilities.read_puzzle_input(year=year, day=day, is_test=is_test)

    assert lines == ["A", "B", "", "C"], f"should trim newline characters when {scenario}"
    mock_open.assert_called_once_with(file=f"{project_directory}/{expected_path}", mode="r")


@patch("aoc_solver.utilities.importlib_util")
@patch("builtins.open", new_callable=mock_open, read_data="A\nB\n\nC\n")
def test_run_solution_calls_solve_when_module_exists(mock_open, mock_importlib_util, project_directory):
    solution = utilities.run_solution(year=2022, day=1)

    assert hasattr(solution, "first") and hasattr(solution, "second") is not None, "should return Solution namedtuple"
    mock_importlib_util.find_spec.assert_called_once_with(name=f"aoc_solver.2022.day_01")
    mock_importlib_util.module_from_spec.assert_called_once_with(spec=mock_importlib_util.find_spec.return_value)
    mock_importlib_util.find_spec.return_value.loader.exec_module.assert_called_once_with(module=mock_importlib_util.module_from_spec.return_value)
    mock_importlib_util.module_from_spec.return_value.solve.assert_called_once_with(puzzle_input=["A", "B", "", "C"])
    mock_open.assert_called_once_with(file=f"{project_directory}/src/aoc_solver/2022/day_01.txt", mode="r")


@patch("aoc_solver.utilities.importlib_util")
@patch("aoc_solver.utilities.download_puzzle_input")
def test_run_solution_attempts_to_create_missing_resources(mock_download_puzzle_input, mock_importlib_util):
    mock_importlib_util.find_spec.return_value = None

    solution = utilities.run_solution(year=2021, day=25)

    assert (
        solution == "ERROR: Unable to create all missing puzzle resources.\nPlease manually create puzzle modules and tests and try again."
    ), "should prompt to manually create resources"
    mock_importlib_util.find_spec.assert_called_once_with(name=f"aoc_solver.2021.day_25")
    mock_importlib_util.module_from_spec.assert_not_called()
    mock_download_puzzle_input.assert_called_with(year=2021, day=25, is_test=True)


@patch("aoc_solver.utilities.os")
@patch("aoc_solver.utilities.requests")
@patch("builtins.open", new_callable=mock_open)
def test_download_puzzle_input_for_tests(mock_open, mock_requests, mock_os):
    mock_os.path.isfile.return_value = False
    mock_requests.get.return_value.text = "<p>For example</p>\n<pre><code>A\nB\n\nC\n</code></pre>"

    utilities.download_puzzle_input(year=2021, day=25, is_test=True)

    mock_requests.get.assert_called_once_with(url="https://adventofcode.com/2021/day/25")
    mock_os.path.isfile.assert_called_once_with(path=mock_os.path.join.return_value)
    mock_os.makedirs.assert_called_once_with(name=mock_os.path.dirname.return_value, exist_ok=True)
    mock_open.assert_called_once_with(file=mock_os.path.join.return_value, mode="w")
    mock_open().write.assert_called_once_with("A\nB\n\nC\n")


@patch("aoc_solver.utilities.ExamplePuzzleInputParser")
@patch("aoc_solver.utilities.os")
@patch("aoc_solver.utilities.requests")
@patch("builtins.open", new_callable=mock_open)
def test_download_puzzle_input_for_modules(mock_open, mock_requests, mock_os, mock_parser):
    mock_os.path.isfile.return_value = False

    utilities.download_puzzle_input(year=2021, day=25, is_test=False)

    mock_parser.assert_not_called()
    mock_requests.get.assert_not_called()
    mock_os.path.isfile.assert_called_once_with(path=mock_os.path.join.return_value)
    mock_os.makedirs.assert_not_called()
    mock_open.assert_not_called()
    mock_open().write.assert_not_called()


@patch("aoc_solver.utilities.ExamplePuzzleInputParser")
@patch("aoc_solver.utilities.os")
@patch("aoc_solver.utilities.requests")
@patch("builtins.open", new_callable=mock_open)
def test_download_puzzle_input_skips_if_exists(mock_open, mock_requests, mock_os, mock_parser):
    mock_os.path.isfile.return_value = True

    utilities.download_puzzle_input(year=2021, day=25, is_test=False)

    mock_parser.assert_not_called()
    mock_requests.get.assert_not_called()
    mock_os.path.isfile.assert_called_once_with(path=mock_os.path.join.return_value)
    mock_os.makedirs.assert_not_called()
    mock_open.assert_not_called()
    mock_open().write.assert_not_called()
