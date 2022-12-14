import pytest
from aoc_solver.object_types import Solution


@pytest.fixture
def mock_terminal_output():
    return [
        "$ cd /",
        "$ ls",
        "dir a",
        "dir b",
        "300 c.txt",
        "$ cd a",
        "$ ls",
        "400 d.exe",
        "dir e",
        "$ cd e",
        "$ ls",
        "600 f.png",
        "$ cd ..",
        "$ cd ..",
        "$ cd b",
        "$ ls",
        "dir h",
        "700 g.ico",
        "$ cd h",
        "$ ls",
        "dir j",
        "900 i.csv",
        "$ cd j",
        "$ ls",
        "1100 k.svg",
    ]


def test_parse_filesystem_containing_only_subdirectories(mock_terminal_output, puzzle_module):
    filesystem = puzzle_module.parse_filesystem(terminal_output=mock_terminal_output)

    assert filesystem.name == "/", "should start with root directory"
    assert filesystem.object_type == "dir", "should categorize root as directory"
    assert filesystem.size == 4000, "should sum child object sizes"
    assert len(filesystem.children) == 3, "should parse child objects"

    dir_1, dir_2, file_1 = filesystem.children
    assert file_1.name == "c.txt", "should parse child object names"
    assert file_1.object_type == "file", "should parse child object types"
    assert file_1.size == 300, "should sum grandchild objects sizes"
    assert file_1.children == [], "should parse grandchild objects"

    assert dir_1.name == "a", "should parse child object names"
    assert dir_1.object_type == "dir", "should parse child object types"
    assert dir_1.size == 1000, "should sum grandchild objects sizes"
    assert len(dir_1.children) == 2, "should parse grandchild objects"

    sub_file_1, sub_dir_1 = dir_1.children
    assert sub_file_1.name == "d.exe", "should parse grandchild object names"
    assert sub_file_1.object_type == "file", "should parse grandchild object types"
    assert sub_file_1.size == 400, "should sum great-grandchild objects sizes"
    assert sub_file_1.children == [], "should parse great-grandchild objects"

    assert sub_dir_1.name == "e", "should parse grandchild object names"
    assert sub_dir_1.object_type == "dir", "should parse grandchild object types"
    assert sub_dir_1.size == 600, "should sum great-grandchild objects sizes"
    assert len(sub_dir_1.children) == 1, "should parse great-grandchild objects"

    sub_sub_file_1 = sub_dir_1.children[0]
    assert sub_sub_file_1.name == "f.png", "should parse great-grandchild object names"
    assert sub_sub_file_1.object_type == "file", "should parse great-grandchild object types"
    assert sub_sub_file_1.size == 600, "should sum great-great-grandchild objects sizes"
    assert sub_sub_file_1.children == [], "should parse great-great-grandchild objects"

    assert dir_2.name == "b", "should parse child object names"
    assert dir_2.object_type == "dir", "should parse child object types"
    assert dir_2.size == 2700, "should sum grandchild objects sizes"
    assert len(dir_2.children) == 2, "should parse grandchild objects"

    sub_dir_2, sub_file_2 = dir_2.children
    assert sub_file_2.name == "g.ico", "should parse grandchild object names"
    assert sub_file_2.object_type == "file", "should parse grandchild object types"
    assert sub_file_2.size == 700, "should sum great-grandchild objects sizes"
    assert sub_file_2.children == [], "should parse great-grandchild objects"

    assert sub_dir_2.name == "h", "should parse grandchild object names"
    assert sub_dir_2.object_type == "dir", "should parse grandchild object types"
    assert sub_dir_2.size == 2000, "should sum great-grandchild objects sizes"
    assert len(sub_dir_2.children) == 2, "should parse great-grandchild objects"

    sub_sub_dir_1, sub_sub_file_2 = sub_dir_2.children
    assert sub_sub_file_2.name == "i.csv", "should parse great-grandchild object names"
    assert sub_sub_file_2.object_type == "file", "should parse great-grandchild object types"
    assert sub_sub_file_2.size == 900, "should sum great-great-grandchild objects sizes"
    assert sub_sub_file_2.children == [], "should parse great-great-grandchild objects"

    assert sub_sub_dir_1.name == "j", "should parse great-grandchild object names"
    assert sub_sub_dir_1.object_type == "dir", "should parse great-grandchild object types"
    assert sub_sub_dir_1.size == 1100, "should sum great-great-grandchild objects sizes"
    assert len(sub_sub_dir_1.children) == 1, "should parse great-great-grandchild objects"

    sub_sub_sub_file_1 = sub_sub_dir_1.children[0]
    assert sub_sub_sub_file_1.name == "k.svg", "should parse great-great-grandchild object names"
    assert sub_sub_sub_file_1.object_type == "file", "should parse great-great-grandchild object types"
    assert sub_sub_sub_file_1.size == 1100, "should sum great-great-great-grandchild objects sizes"
    assert sub_sub_sub_file_1.children == [], "should parse great-great-great-grandchild objects"


@pytest.mark.parametrize(
    "max_directory_size,expected_total",
    [
        (1000, 1600),
        (1500, 2700),
        (2000, 4700),
    ],
)
def test_calculate_total_directory_sizes(max_directory_size, expected_total, mock_terminal_output, puzzle_module):
    assert (
        puzzle_module.calculate_total_directory_sizes_under_max(terminal_output=mock_terminal_output, max_directory_size=max_directory_size)
        == expected_total
    ), f"should only total directory sizes of at most {max_directory_size}"


def test_solve_calculates_puzzle_answers(puzzle_module, mock_puzzle_input):
    assert puzzle_module.solve(puzzle_input=mock_puzzle_input) == Solution(
        first=95437, second=24933642
    ), "should calculate correct example input answer"
