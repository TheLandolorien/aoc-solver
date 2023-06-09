from unittest.mock import ANY, mock_open, patch

from aoc_solver import puzzle_manager


@patch("aoc_solver.puzzle_manager.authenticator")
@patch("aoc_solver.puzzle_manager.ExamplePuzzleInputParser")
@patch("aoc_solver.puzzle_manager.requests")
@patch("aoc_solver.puzzle_manager.os")
@patch("aoc_solver.puzzle_manager.Template")
@patch("builtins.open", new_callable=mock_open, read_data="$title\n$year\n$day")
def test_create_puzzle_resources_writes_missing_files(mock_open, mock_template, mock_os, mock_requests, mock_parser, mock_authenticator, project_directory):
    mock_os.path.isfile.return_value = False

    puzzle_manager.create_puzzle_resources(year=2022, day=1)

    mock_parser.assert_called_once()
    mock_requests.get.assert_called_once_with(url="https://adventofcode.com/2022/day/1")
    mock_parser.return_value.feed.assert_called_once_with(mock_requests.get.return_value.text)
    mock_parser.return_value.close.assert_called_once()
    mock_authenticator.authenticate.assert_called_once_with(provider="github")
    mock_requests.Session.assert_called_once()
    mock_requests.Session.return_value.cookies.set.assert_called_once_with(name="session", value=mock_authenticator.authenticate.return_value)
    mock_requests.Session.return_value.get.assert_called_once_with(url="https://adventofcode.com/2022/day/1/input")
    mock_requests.Session.return_value.get.return_value.raise_for_status.assert_called_once()
    mock_os.path.isfile.assert_any_call(path=mock_os.path.join.return_value)
    mock_os.path.join.assert_any_call(ANY, 'aoc_solver', '2022', 'day_01.txt')
    mock_os.path.join.assert_any_call(ANY, 'aoc_solver', '2022', 'test_day_01.txt')
    mock_os.path.join.assert_any_call(ANY, 'aoc_solver', '2022', 'day_01.py')
    mock_os.path.join.assert_any_call(ANY, 'aoc_solver', '2022', 'test_day_01.py')
    mock_open.return_value.write.assert_any_call(mock_parser.return_value.example_input)
    mock_open.return_value.write.assert_any_call(mock_requests.Session.return_value.get.return_value.text)
    mock_open.return_value.write.assert_any_call(mock_template().substitute.return_value)


@patch("aoc_solver.puzzle_manager.authenticator")
@patch("aoc_solver.puzzle_manager.ExamplePuzzleInputParser")
@patch("aoc_solver.puzzle_manager.requests")
@patch("aoc_solver.puzzle_manager.os")
@patch("builtins.open", new_callable=mock_open)
def test_create_puzzle_resources_skips_existing_files(mock_open, mock_os, mock_requests, mock_parser, mock_authenticator):
    mock_os.path.isfile.return_value = True

    puzzle_manager.create_puzzle_resources(year=2022, day=1)

    mock_parser.assert_called_once()
    mock_requests.get.assert_called_once_with(url="https://adventofcode.com/2022/day/1")
    mock_parser.return_value.feed.assert_called_once_with(mock_requests.get.return_value.text)
    mock_parser.return_value.close.assert_called_once()
    mock_authenticator.authenticate.assert_called_once_with(provider="github")
    mock_requests.Session.assert_called_once()
    mock_requests.Session.return_value.cookies.set.assert_called_once_with(name="session", value=mock_authenticator.authenticate.return_value)
    mock_requests.Session.return_value.get.assert_called_once_with(url="https://adventofcode.com/2022/day/1/input")
    mock_requests.Session.return_value.get.return_value.raise_for_status.assert_called_once()
    mock_os.path.isfile.assert_any_call(path=mock_os.path.join.return_value)
    mock_os.makedirs.assert_not_called()
    mock_open.assert_not_called()


@patch("aoc_solver.puzzle_manager.os")
@patch("aoc_solver.puzzle_manager.utilities")
def test_read_puzzle_input_reads_puzzle_input(mock_utilities, mock_os, project_directory):
    # TODO: Test name is sign of poorly factored code
    puzzle_input = puzzle_manager.read_puzzle_input(year=2022, day=25)

    assert puzzle_input == mock_utilities.read_file.return_value, "should read puzzle input via utilities"
    mock_os.path.join.assert_called_once_with(f"{project_directory}/src", "aoc_solver", "2022", "day_25.txt")
    mock_utilities.read_file.assert_called_once_with(path=mock_os.path.join.return_value)
