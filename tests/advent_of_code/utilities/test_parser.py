import os
import typing

import advent_of_code.utilities.parser as parser


def read(data_name: str) -> typing.List[str]:
    puzzle_input_path = os.path.join(os.path.dirname(__file__), f"../data/{data_name}.txt")
    with open(puzzle_input_path) as f:
        return f.readlines()


def test_calorie_parser_sums_calories_per_elf() -> None:
    assert parser.parse(puzzle_input=read("calories"), calories=True) == [6000, 4000, 11000, 24000, 10000]


def test_strategy_guide_parser_groups_predictions() -> None:
    assert parser.parse(puzzle_input=read("strategy_guide"), strategy_guide=True) == [["A", "Y"], ["B", "X"], ["C", "Z"]]
