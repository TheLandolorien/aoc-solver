import typing
import pytest

from aoc_solver.object_types import Solution


@pytest.fixture
def mock_nodes() -> typing.Dict[str, typing.List[str]]:
    return {
        "AAA": ["BBB", "CCC"],
        "BBB": ["DDD", "EEE"],
        "CCC": ["ZZZ", "GGG"],
        "DDD": ["DDD", "DDD"],
        "EEE": ["EEE", "EEE"],
        "GGG": ["GGG", "GGG"],
        "ZZZ": ["ZZZ", "ZZZ"],
    }


def test_solve_calculates_puzzle_answers(puzzle_module, mock_puzzle_input):
    mock_puzzle_input_2 = [
        "LLR",
        "",
        "AAA = (BBB, BBB)",
        "BBB = (AAA, ZZZ)",
        "ZZZ = (ZZZ, ZZZ)",
    ]
    mock_puzzle_input_3 = [
        "LR",
        "",
        "11A = (11B, XXX)",
        "11B = (XXX, 11Z)",
        "11Z = (11B, XXX)",
        "22A = (22B, XXX)",
        "22B = (22C, 22C)",
        "22C = (22Z, 22Z)",
        "22Z = (22B, 22B)",
        "XXX = (XXX, XXX)",
    ]
    assert puzzle_module.solve(puzzle_input=mock_puzzle_input) == Solution(first=2, second=2)
    assert puzzle_module.solve(puzzle_input=mock_puzzle_input_2) == Solution(first=6, second=6)
    assert puzzle_module.solve(puzzle_input=mock_puzzle_input_3) == Solution(first=2, second=6)


def test_parse_input(puzzle_module, mock_puzzle_input, mock_nodes):
    network = puzzle_module.parse_input(raw_instructions=mock_puzzle_input)

    assert network.instructions == [1, 0], "should parse network instructions"
    assert network.nodes == mock_nodes, "should parse network nodes"
