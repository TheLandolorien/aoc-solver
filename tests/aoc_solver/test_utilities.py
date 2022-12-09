import pytest
from unittest.mock import ANY, mock_open, patch


from aoc_solver import utilities


def get_mock_metadata(year: int, day: int) -> utilities.PuzzleMetadata:
    return utilities.PuzzleMetadata(
        title=f"--- Day {day}: Clever Title ---", year=year, day=day, example_input="A\nB\n\nC\n", puzzle_input="D\nF\nX\nY\n\nG\nE\n"
    )


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
    lines = utilities.read_puzzle_input(metadata=get_mock_metadata(year=year, day=day), is_test=is_test)

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


@patch("aoc_solver.utilities.clone_template")
@patch("aoc_solver.utilities.save_puzzle_input")
@patch("aoc_solver.utilities.get_puzzle_metadata")
@patch("aoc_solver.utilities.importlib_util")
def test_run_solution_attempts_to_create_missing_resources(
    mock_importlib_util, mock_get_puzzle_metadata, mock_save_puzzle_input, mock_clone_template
):
    mock_importlib_util.find_spec.return_value = None

    solution = utilities.run_solution(year=2021, day=25)

    assert (
        solution == "\nERROR: Unable to auto-download puzzle input. Please manually download and try again."
    ), "should prompt to manually create resources"
    mock_importlib_util.find_spec.assert_called_once_with(name=f"aoc_solver.2021.day_25")
    mock_importlib_util.module_from_spec.assert_not_called()
    mock_get_puzzle_metadata.assert_called_once_with(year=2021, day=25)
    mock_save_puzzle_input.assert_called_once_with(metadata=mock_get_puzzle_metadata.return_value, is_test=True)
    mock_clone_template.assert_any_call(metadata=mock_get_puzzle_metadata.return_value, is_test=True)
    mock_clone_template.assert_any_call(metadata=mock_get_puzzle_metadata.return_value)


@patch("aoc_solver.utilities.requests")
def test_get_puzzle_metadata_parses_puzzle_metadata(mock_requests):
    mock_requests.get.return_value.text = "<h2>--- Day 0: Clever Puzzle Title ---</h2><p>For example</p>\n<pre><code>A\nB\n\nC\n</code></pre>"

    puzzle = utilities.get_puzzle_metadata(year=2014, day=0)

    assert puzzle.title == "--- Day 0: Clever Puzzle Title ---", "should parse puzzle title"
    assert puzzle.year == 2014, "should use provided puzzle year"
    assert puzzle.day == 0, "should use provided puzzle day"
    assert puzzle.example_input == "A\nB\n\nC\n", "should parse example puzzle input"

    mock_requests.get.assert_called_once_with(url="https://adventofcode.com/2014/day/0")


@patch("aoc_solver.utilities.os")
@patch("builtins.open", new_callable=mock_open)
def test_save_puzzle_input_for_modules(mock_open, mock_os):
    mock_os.path.isfile.return_value = False

    result = utilities.save_puzzle_input(metadata=get_mock_metadata(year=2015, day=1), is_test=False)

    assert result is None, f"should skip saving puzzle module inputs"

    mock_os.path.join.assert_not_called()
    mock_os.path.isfile.assert_not_called()
    mock_os.path.dirname.assert_not_called()
    mock_os.makedirs.assert_not_called()
    mock_open.assert_not_called()
    mock_open().write.assert_not_called()


@patch("aoc_solver.utilities.os")
@patch("builtins.open", new_callable=mock_open)
def test_save_puzzle_input_for_tests(mock_open, mock_os, project_directory):
    mock_os.path.isfile.return_value = False
    mock_metadata = get_mock_metadata(year=2015, day=1)

    utilities.save_puzzle_input(metadata=mock_metadata, is_test=True)

    mock_os.path.join.assert_any_call(mock_os.path.dirname.return_value, "tests")
    mock_os.path.join.assert_any_call(mock_os.path.join.return_value, "aoc_solver", "2015", "test_day_01.txt")
    mock_os.path.isfile.assert_called_once_with(path=mock_os.path.join.return_value)
    mock_os.path.dirname.assert_any_call(mock_os.path.join.return_value)
    mock_os.path.dirname.assert_any_call(f"{project_directory}/src")
    mock_os.makedirs.assert_called_once_with(name=mock_os.path.dirname.return_value, exist_ok=True)
    mock_open.assert_called_once_with(file=mock_os.path.join.return_value, mode="w")
    mock_open().write.assert_called_once_with(mock_metadata.example_input)


@patch("aoc_solver.utilities.os")
@patch("builtins.open", new_callable=mock_open)
def test_save_puzzle_input_skips_if_exists(mock_open, mock_os):
    mock_os.path.isfile.return_value = True

    utilities.save_puzzle_input(metadata=get_mock_metadata(year=2021, day=25), is_test=True)

    mock_os.path.isfile.assert_called_once_with(path=mock_os.path.join.return_value)
    mock_os.makedirs.assert_not_called()
    mock_open.assert_not_called()
    mock_open().write.assert_not_called()


@patch("aoc_solver.utilities.Template")
@patch("aoc_solver.utilities.os")
@patch("builtins.open", new_callable=mock_open, read_data="A\nB\n\nC\n")
def test_clone_template_for_puzzle_solutions(mock_open, mock_os, mock_template, project_directory):
    mock_metadata = get_mock_metadata(year=2020, day=12)

    utilities.clone_template(metadata=mock_metadata, is_test=False)

    mock_os.path.join.assert_any_call(f"{project_directory}/src", "templates", "day_n.py.template")
    mock_os.path.join.assert_any_call(f"{project_directory}/src", "aoc_solver", "2020", "day_12.py")
    mock_os.path.dirname.assert_called_once_with(mock_os.path.join.return_value)
    mock_os.makedirs.assert_called_once_with(name=mock_os.path.dirname.return_value, exist_ok=True)
    mock_open.assert_any_call(file=mock_os.path.join.return_value, mode="r")
    mock_open.assert_any_call(file=mock_os.path.join.return_value, mode="w")
    mock_open().read.assert_called_once()
    mock_open().write.assert_called_once_with(mock_template.return_value.substitute.return_value)
    mock_template.assert_called_once_with("A\nB\n\nC\n")
    mock_template.return_value.substitute.assert_called_once_with(
        {"title": mock_metadata.title, "year": mock_metadata.year, "day": mock_metadata.day}
    )


@patch("aoc_solver.utilities.Template")
@patch("aoc_solver.utilities.os")
@patch("builtins.open", new_callable=mock_open, read_data="A\nB\n\nC\n")
def test_clone_template_for_tests(mock_open, mock_os, mock_template, project_directory):
    mock_metadata = get_mock_metadata(year=2019, day=21)

    utilities.clone_template(metadata=mock_metadata, is_test=True)

    mock_os.path.join.assert_any_call(mock_os.path.dirname.return_value, "tests")
    mock_os.path.join.assert_any_call(f"{project_directory}/src", "templates", "test_day_n.py.template")
    mock_os.path.join.assert_any_call(mock_os.path.join.return_value, "aoc_solver", "2019", "test_day_21.py")
    mock_os.path.dirname.assert_any_call(mock_os.path.join.return_value)
    mock_os.path.dirname.assert_any_call(f"{project_directory}/src")
    mock_os.makedirs.assert_called_once_with(name=mock_os.path.dirname.return_value, exist_ok=True)
    mock_open.assert_any_call(file=mock_os.path.join.return_value, mode="r")
    mock_open.assert_any_call(file=mock_os.path.join.return_value, mode="w")
    mock_open().read.assert_called_once()
    mock_open().write.assert_called_once_with(mock_template.return_value.substitute.return_value)
    mock_template.assert_called_once_with("A\nB\n\nC\n")
    mock_template.return_value.substitute.assert_called_once_with(
        {"title": mock_metadata.title, "year": mock_metadata.year, "day": mock_metadata.day}
    )
