import typing

from aoc_solver.utilities import Solution
from aoc_solver.object_types import FileSystemNode


# --- Day 7: No Space Left On Device ---
# Source: https://adventofcode.com/2022/day/7


# Part 1 -  Commands are a Depth-First Search (DFS) order
# See: HackerRank's Algorithms: Graph Search, DFS and BFS Video
# Source: https://www.youtube.com/watch?v=zaBhtODEL0w


def parse_filesystem(terminal_output: typing.List[str]) -> FileSystemNode:
    # Assumption: Output always starts at root folder
    root = FileSystemNode(name="/", object_type="dir", size=0)
    current_node = root

    for line in terminal_output[1:]:
        if line == "$ cd ..":
            current_node = current_node.parent
        elif line.startswith("$ cd"):
            _, _, directory_name = line.split()
            current_node = current_node.find_children(name=directory_name)[0]
        elif line == "$ ls":
            continue
        elif line.startswith("dir"):
            object_type, directory_name = line.split()
            current_node.add_child(name=directory_name, object_type=object_type, size=0)
        else:
            size, filename = line.split()
            current_node.add_child(name=filename, object_type="file", size=size)

    return root


# What is the sum of the total sizes of those directories?
def calculate_total_directory_sizes_under_max(terminal_output: typing.List[str], max_directory_size: int = 100000) -> int:
    filesystem = parse_filesystem(terminal_output=terminal_output)

    queue = [filesystem]
    total = 0

    while queue:
        current_node = queue.pop()
        queue.extend(current_node.children)

        if current_node.name != filesystem.name and current_node.object_type == "dir" and current_node.size < max_directory_size + 1:
            total += current_node.size

    return total


def solve(puzzle_input=typing.List[str]) -> Solution:
    return Solution(
        first=calculate_total_directory_sizes_under_max(terminal_output=puzzle_input),
        second=None,
    )
