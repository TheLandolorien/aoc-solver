import pytest

import os
import shutil


@pytest.fixture
def mock_puzzle_resources(request, project_directory, tmp_path):
    marker = request.node.get_closest_marker("date_arg")

    year = 2021
    if marker is not None:
        year = marker.args[0]

    original_module_location = os.path.join(project_directory, f"src/aoc_solver/{year}")
    temporary_module_location = tmp_path / "src"
    os.rename(original_module_location, temporary_module_location)

    original_test_location = os.path.join(project_directory, f"tests/aoc_solver/{year}")
    temporary_test_location = tmp_path / "tests"
    os.rename(original_test_location, temporary_test_location)

    yield

    shutil.rmtree(original_module_location)
    os.mkdir(original_module_location)
    os.rename(temporary_module_location, original_module_location)

    shutil.rmtree(original_test_location)
    os.mkdir(original_test_location)
    os.rename(temporary_test_location, original_test_location)


@pytest.mark.date_arg(2021)
def test_run_with_missing_puzzle(mock_puzzle_resources, project_directory):
    year, day = (2021, 11)
    result = os.popen(f"aoc-solver --date {year} {day}").read()

    assert result == (
        f"Saved puzzle input to {project_directory}/tests/aoc_solver/{year}/test_day_{day}.txt\n"
        f"Saved puzzle input to {project_directory}/src/aoc_solver/{year}/day_{day}.txt\n"
        f"Created puzzle module at {project_directory}/src/aoc_solver/{year}/day_{day}.py\n"
        f"Created puzzle module at {project_directory}/tests/aoc_solver/{year}/test_day_{day}.py\n"
        "Part One: The puzzle answer is None\n"
        "Part Two: The puzzle answer is None\n"
    ), f"should downloading missing puzzle resources and default answers to None"


def test_run_with_integer_answers():
    result = os.popen("aoc-solver --date 2022 1").read()

    assert result == (
        "Part One: The puzzle answer is 65912\n" "Part Two: The puzzle answer is 195625\n"
    ), f"should correctly cast integer answers"


def test_run_with_string_answers():
    result = os.popen("aoc-solver --date 2022 5").read()

    assert result == (
        ("Part One: The puzzle answer is VWLCWGSDQ\n" "Part Two: The puzzle answer is TCGLQSLPW\n")
    ), f"should correctly cast string answers"
