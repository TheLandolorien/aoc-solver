import textwrap
import typing


from aoc_solver.object_types import Solution

# --- Day #: Supply Stacks ---
# Source: https://adventofcode.com/2022/day/5


def flatten_stacks(stacks: typing.List[str]) -> typing.List[typing.List[str]]:
    num_stacks = len(stacks.pop().split())
    flattened_stacks = [[] for _ in range(num_stacks)]  # Avoids [[]] * num_stacks due to reference issue

    for row in stacks:
        crates = textwrap.wrap(f" {row}", width=4, drop_whitespace=False)  # Add leading space to make columns even
        for i in range(num_stacks):
            if not (crate := crates[i]).isspace():
                flattened_stacks[i].insert(0, crate.strip("[ ]"))

    return flattened_stacks


def get_top_crates(stacks: typing.List[typing.List[str]], rearrangement_procedure: typing.List[str], move_in_order: bool = False) -> str:
    flattened_stacks = flatten_stacks(stacks=stacks)
    for step in rearrangement_procedure:
        move_crates(flattened_stacks=flattened_stacks, step=step, in_order=move_in_order)

    return "".join([stack[-1] for stack in flattened_stacks])


def move_crates(flattened_stacks: typing.List[typing.List[str]], step: str, in_order: bool = False) -> typing.List[typing.List[str]]:
    num_crates, source_stack, target_stack = [int(item) for item in step.split() if item.isdigit()]

    moved_crates = []
    for _ in range(num_crates):
        crate = flattened_stacks[source_stack - 1].pop()
        moved_crates.append(crate)

    if in_order:
        moved_crates.reverse()

    flattened_stacks[target_stack - 1].extend(moved_crates)

    return flattened_stacks


def solve(puzzle_input=typing.List[str]) -> Solution:
    stacks = puzzle_input[: (split_idx := puzzle_input.index(""))]
    steps = puzzle_input[split_idx + 1 :]

    return Solution(
        first=get_top_crates(stacks=stacks[:], rearrangement_procedure=steps[:]),
        second=get_top_crates(stacks=stacks[:], rearrangement_procedure=steps[:], move_in_order=True),
    )
