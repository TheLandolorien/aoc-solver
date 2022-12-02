import os
import typing


def read(puzzle_name) -> typing.List[str]:
    puzzle_input_path = os.path.join(os.path.dirname(__file__), f"../../puzzle_inputs/{puzzle_name}.txt")
    with open(puzzle_input_path) as f:
        return f.readlines()
