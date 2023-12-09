import typing
from collections import namedtuple

from aoc_solver.object_types import Solution

Network = namedtuple("Network", ["instructions", "nodes"])

# --- Day 8: Haunted Wasteland ---
# Source: https://adventofcode.com/2023/day/8


def count_steps(raw_instructions: typing.List[str], has_multi_paths: bool = False) -> int:
    network = parse_input(raw_instructions=raw_instructions)

    current_nodes = (
        [node for node in network.nodes.keys() if node.endswith("A")]
        if has_multi_paths
        else [list(network.nodes.keys())[0]]
    )
    step = 0
    num_instructions = len(network.instructions)
    num_paths = len(current_nodes)
    all_zs = all([node.endswith("Z") for node in current_nodes])

    while not all_zs:
        z_enders = 0
        for idx, node in enumerate(current_nodes):
            current_nodes[idx] = network.nodes[node][network.instructions[step % num_instructions]]
            if current_nodes[idx].endswith("Z"):
                z_enders += 1

        all_zs = z_enders == num_paths
        step += 1

    return step


def parse_input(raw_instructions: typing.List[str]) -> Network:
    instructions = [1 if x == "R" else 0 for x in raw_instructions[0]]
    nodes = {}

    for raw_node in raw_instructions[2:]:
        node, edges = raw_node.split(" = ")
        nodes[node] = edges[1:-1].split(", ")

    return Network(instructions=instructions, nodes=nodes)


def solve(puzzle_input: typing.List[str]) -> Solution:
    return Solution(
        first=count_steps(raw_instructions=puzzle_input),
        second=count_steps(raw_instructions=puzzle_input, has_multi_paths=True),
    )
