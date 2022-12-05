from unittest.mock import patch

from aoc_solver import solver
from aoc_solver.utilities import Solution


@patch("sys.argv", ["solve", "2021", "sonar_sweep"])
def test_solver_with_2021_day_1_puzzle():
    solution = solver.solve()

    assert solution == Solution(first=1228, second=1257)


@patch("sys.argv", ["solve", "2022", "calorie_counting"])
def test_solver_with_2022_day_1_puzzle():
    solution = solver.solve()

    assert solution == Solution(first=65912, second=195625)


@patch("sys.argv", ["solve", "2022", "supply_stacks"])
def test_solver_with_2022_day_5_puzzle():
    solution = solver.solve()

    assert solution == Solution(first="VWLCWGSDQ", second="TCGLQSLPW")
