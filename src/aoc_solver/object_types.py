import typing

from collections import namedtuple
from html.parser import HTMLParser

Solution = namedtuple("Solution", ["first", "second"])
PuzzleMetadata = namedtuple(
    "Puzzle", ["title", "year", "day", "formatted_day", "example_input", "puzzle_input"]
)


class ExamplePuzzleInputParser(HTMLParser):
    example_input = None
    should_check_for_example_code = False
    should_extract_example_input = False

    puzzle_title = None
    should_extract_puzzle_title = False

    def handle_starttag(self, tag, _) -> None:
        if tag == "h2":
            self.should_extract_puzzle_title = True
        elif tag == "pre":
            self.should_check_for_example_code = True
        elif tag == "code" and self.should_check_for_example_code and self.example_input is None:
            self.should_extract_example_input = True

    def handle_data(self, data):
        if self.should_extract_puzzle_title:
            self.puzzle_title = data
            self.should_extract_puzzle_title = False
        elif self.should_extract_example_input and data != "\n":
            self.example_input = data
            self.should_check_for_example_code = False
            self.should_extract_example_input = False


class FileSystemNode:
    ERROR_MESSAGE_INVALID_CHILD_ADDITION = "Children can only be added to directories"

    def __init__(
        self,
        name: str,
        object_type: str,
        size: int = 0,
        parent: "FileSystemNode" = None,
        children: typing.List = None,
    ):
        if children and object_type == "file":
            raise AttributeError(self.ERROR_MESSAGE_INVALID_CHILD_ADDITION)

        self.name = name
        self.object_type = object_type
        self.size = int(size)
        self.parent = parent
        self.children = children if children else []  # Avoid pass by reference issues

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name}, object_type={self.object_type}, size={self.size}, children={self.children})"

    def find_children(self, name: str) -> typing.List["FileSystemNode"]:
        # deepcode ignore AttributeLoadOnNone: self.childen will initialize to an empty list
        return [node for node in self.children if node.name == name]

    def add_child(self, name: str, object_type: str, size: int = 0) -> None:
        if self.object_type == "file":
            raise AttributeError(self.ERROR_MESSAGE_INVALID_CHILD_ADDITION)

        node = FileSystemNode(name=name, object_type=object_type, size=size, parent=self)
        # deepcode ignore AttributeLoadOnNone: self.childen will initialize to an empty list
        self.children.append(node)

        if node.object_type == "file":
            self.size += node.size
            self.recalculate_size(new_node_size=node.size)

    def recalculate_size(self, new_node_size: int) -> None:
        # deepcode ignore AttributeLoadOnNone: Avoid load due to while loop initiation
        parent = self.parent
        while parent:
            parent.size += new_node_size
            parent = parent.parent
