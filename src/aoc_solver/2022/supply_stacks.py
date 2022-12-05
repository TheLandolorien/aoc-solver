import textwrap
import typing


from aoc_solver.utilities import Solution

# --- Day #: Supply Stacks ---
# Source: https://adventofcode.com/2022/day/5


def get_top_crates(stacks: typing.List[typing.List[str]], rearrangement_procedure: typing.List[str]) -> str:
    flattened_stacks = flatten_stacks(stacks=stacks)
    for step in rearrangement_procedure:
        move_crates(flattened_stacks=flattened_stacks, step=step)

    return "".join([stack[-1] for stack in flattened_stacks])


def flatten_stacks(stacks: typing.List[str]) -> typing.List[typing.List[str]]:
    num_stacks = len(stacks.pop().split())
    flattened_stacks = [[] for _ in range(num_stacks)]  # Avoids [[]] * num_stacks due to reference issue

    for row in stacks:
        crates = textwrap.wrap(f" {row}", width=4, drop_whitespace=False)  # Add leading space to make columns even
        for i in range(num_stacks):
            if not (crate := crates[i]).isspace():
                flattened_stacks[i].insert(0, crate.strip("[ ]"))

    return flattened_stacks


def move_crates(flattened_stacks: typing.List[typing.List[str]], step: str) -> typing.List[typing.List[str]]:
    num_crates, source_stack, target_stack = [int(item) for item in step.split() if item.isdigit()]

    for _ in range(num_crates):
        crate = flattened_stacks[source_stack - 1].pop()
        flattened_stacks[target_stack - 1].append(crate)

    return flattened_stacks


def solve(puzzle_input=typing.List[str]) -> Solution:
    split_idx = puzzle_input.index("")

    return Solution(
        first=get_top_crates(stacks=puzzle_input[:split_idx], rearrangement_procedure=puzzle_input[split_idx + 1 :]),
        second=None,
    )
