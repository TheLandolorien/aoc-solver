import pytest
from enum import Enum

import pytest

from aoc_solver.object_types import Solution


@pytest.mark.parametrize("mock_puzzle_num,mock_solutions", [(1, (6440, 5905))])
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


@pytest.mark.parametrize(
    "mock_deal,rank",
    [
        ("A2345", "HIGH_CARD"),
        ("AA234", "ONE_PAIR"),
        ("AA223", "TWO_PAIR"),
        ("AAA23", "THREE_OF_A_KIND"),
        ("AAA22", "FULL_HOUSE"),
        ("AAAA2", "FOUR_OF_A_KIND"),
        ("AAAAA", "FIVE_OF_A_KIND"),
    ],
)
def test_evaluate_hand_without_jacks_or_jokers(mock_deal, rank, puzzle_module) -> None:
    rank_score = puzzle_module.evaluate_hand(deal=mock_deal, use_jokers=False)
    assert rank_score.name == rank, f"should evaluate {rank} hands without Jacks"
    rank_score = puzzle_module.evaluate_hand(deal=mock_deal, use_jokers=True)
    assert rank_score.name == rank, f"should evaluate {rank} hands without Jokers"


@pytest.mark.parametrize(
    "mock_deal,rank",
    [
        ("JA234", "ONE_PAIR"),
        ("JAA23", "THREE_OF_A_KIND"),
        ("JJA23", "THREE_OF_A_KIND"),
        ("JAA22", "FULL_HOUSE"),
        ("JAAA2", "FOUR_OF_A_KIND"),
        ("JJAA2", "FOUR_OF_A_KIND"),
        ("JJJA2", "FOUR_OF_A_KIND"),
        ("JAAAA", "FIVE_OF_A_KIND"),
        ("JJAAA", "FIVE_OF_A_KIND"),
        ("JJJAA", "FIVE_OF_A_KIND"),
        ("JJJJA", "FIVE_OF_A_KIND"),
        ("JJJJJ", "FIVE_OF_A_KIND"),
    ],
)
def test_evaluate_hand_with_jokers(mock_deal, rank, puzzle_module) -> None:
    rank_score = puzzle_module.evaluate_hand(deal=mock_deal, use_jokers=True)

    assert rank_score.name == rank, f"should evaluate {rank} hands with wildcards"
