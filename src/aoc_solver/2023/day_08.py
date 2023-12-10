import typing
from collections import namedtuple
from math import lcm

from aoc_solver.object_types import Solution

Network = namedtuple("Network", ["instructions", "nodes", "starting_nodes"])

# --- Day 8: Haunted Wasteland ---
# Source: https://adventofcode.com/2023/day/8


def count_steps(raw_instructions: typing.List[str]) -> int:
    network = parse_input(raw_instructions=raw_instructions, has_multi_paths=False)

    step = 0
    node = network.starting_nodes[0]

    while not node.endswith("Z"):
        node = network.nodes[node][network.instructions[step % len(network.instructions)]]
        step += 1

    return step


def calculate_steps(raw_instructions: typing.List[str]) -> int:
    network = parse_input(raw_instructions=raw_instructions, has_multi_paths=True)

    patterns = []
    for node in network.starting_nodes:
        pattern = calculate_z_ender_pattern(node=node, network=network)
        patterns.append(pattern)

    return lcm(*patterns)


def calculate_z_ender_pattern(node: str, network: Network) -> int:
    z_indices = []
    current_node = node
    i = 0

    while len(z_indices) < 10:
        current_node = network.nodes[current_node][
            network.instructions[i % len(network.instructions)]
        ]
        if current_node.endswith("Z"):
            z_indices.append(i)
        i += 1

    return calculate_pattern(sequence=z_indices)


def calculate_pattern(sequence: typing.List[int]) -> int:
    if len(set(sequence)) == 1:
        return sequence[0]

    return calculate_pattern(
        sequence=[term - sequence[idx - 1] for idx, term in enumerate(sequence) if idx > 0],
    )


def parse_input(raw_instructions: typing.List[str], has_multi_paths: bool) -> Network:
    nodes = {}
    starting_nodes = []

    for raw_node in raw_instructions[2:]:
        node, edges = raw_node.split(" = ")
        nodes[node] = dict(zip(["L", "R"], edges[1:-1].split(", ")))
        if node.endswith("A"):
            starting_nodes.append(node)

    if not has_multi_paths:
        starting_nodes = starting_nodes[:1]

    return Network(instructions=raw_instructions[0], nodes=nodes, starting_nodes=starting_nodes)


def solve(puzzle_input: typing.List[str]) -> Solution:
    return Solution(
        first=count_steps(raw_instructions=puzzle_input),
        second=calculate_steps(raw_instructions=puzzle_input),
    )
