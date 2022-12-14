import pytest
from aoc_solver.object_types import Solution


@pytest.mark.parametrize(
    "scenario,letter,priority",
    [
        ("determine priority for lowercase items", "p", 16),
        ("determine priority for uppercase items", "L", 38),
        ("have case-sensitive priorities", "P", 42),
    ],
)
def test_determine_priority(scenario, letter, priority, puzzle_module):
    assert puzzle_module.determine_priority(item_type=letter) == priority, f"should {scenario}"


@pytest.mark.parametrize(
    "scenario,rucksacks,group_size,total",
    [
        ("calculate groups of 1", ["aBcB", "dBde", "fBfg", "hghI", "IjKj", "lIlm"], 1, 68),
        ("calculate groups of 2", ["aBcB", "dBde", "fBfg", "hghI", "IjKj", "lIlm"], 2, 70),
        ("calculate groups of 3", ["aBcB", "dBde", "fBfg", "hghI", "IjKj", "lIlm"], 3, 63),
    ],
)
def test_calculate_total_common_item_priorities(scenario, rucksacks, group_size, total, puzzle_module):
    assert puzzle_module.calculate_total_common_item_priorities(rucksacks=rucksacks, group_size=group_size) == total, f"should {scenario}"


def test_solve_calculates_puzzle_answers(puzzle_module, mock_puzzle_input):
    assert puzzle_module.solve(puzzle_input=mock_puzzle_input) == Solution(first=157, second=70)
