import pytest
import typing

from aoc_solver.object_types import Solution


@pytest.fixture
def mock_nodes() -> typing.Dict[str, typing.List[str]]:
    return {
        "AAA": {"L": "BBB", "R": "CCC"},
        "BBB": {"L": "DDD", "R": "EEE"},
        "CCC": {"L": "ZZZ", "R": "GGG"},
        "DDD": {"L": "DDD", "R": "DDD"},
        "EEE": {"L": "EEE", "R": "EEE"},
        "GGG": {"L": "GGG", "R": "GGG"},
        "ZZZ": {"L": "ZZZ", "R": "ZZZ"},
    }


@pytest.mark.parametrize("mock_puzzle_num,mock_solutions", [(1, (2, 1)), (2, (6, 1)), (3, (2, 6))])
def test_solve_calculates_puzzle_answers(
    mock_puzzle_num,
    mock_solutions,
    puzzle_module,
    mock_puzzle_inputs,
):
    mock_puzzle_input = mock_puzzle_inputs[mock_puzzle_num - 1]
    mock_first, mock_second = mock_solutions

    first, second = puzzle_module.solve(puzzle_input=mock_puzzle_input)

    assert first == mock_first
    assert second == mock_second


def test_parse_input(puzzle_module, mock_puzzle_inputs, mock_nodes):
    mock_puzzle_input = mock_puzzle_inputs[0]
    network = puzzle_module.parse_input(raw_instructions=mock_puzzle_input, has_multi_paths=False)

    assert network.instructions == "RL", "should parse network instructions"
    assert network.nodes == mock_nodes, "should parse network nodes"
