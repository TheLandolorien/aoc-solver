from datetime import datetime
from unittest.mock import patch

from aoc_solver import solver
from aoc_solver.utilities import Solution


@patch("sys.argv", ["solve"])
@patch("aoc_solver.solver.datetime")
def test_default_solver_with_post_event_request(mock_datetime):
    mock_datetime.now.return_value = datetime(2022, 11, 30)

    solution = solver.solve()

    assert solution == Solution(first=None, second=None)


@patch("sys.argv", ["solve"])
@patch("aoc_solver.solver.datetime")
def test_default_solver_with_current_event_request(mock_datetime):
    mock_datetime.now.return_value = datetime(2022, 12, 4)

    solution = solver.solve()

    assert solution == Solution(first=567, second=907)


@patch("sys.argv", ["solve", "2021", "1"])
def test_explicit_solver_with_int_results():
    solution = solver.solve()

    assert solution == Solution(first=1228, second=1257)


@patch("sys.argv", ["solve", "2022", "1"])
def test_explicit_solver_with_string_results():
    solution = solver.solve()

    assert solution == Solution(first=65912, second=195625)
