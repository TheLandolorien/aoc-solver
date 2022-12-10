import typing

from collections import namedtuple

Solution = namedtuple("Solution", ["first", "second"])
PuzzleMetadata = namedtuple("Puzzle", ["title", "year", "day", "example_input", "puzzle_input"])


class FileSystemNode:
    ERROR_MESSAGE_INVALID_CHILD_ADDITION = "Children can only be added to directories"

    def __init__(self, name: str, object_type: str, size: int = 0, parent: "FileSystemNode" = None, children: typing.List = None):

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
        return [node for node in self.children if node.name == name]

    def add_child(self, name: str, object_type: str, size: int = 0) -> None:
        if self.object_type == "file":
            raise AttributeError(self.ERROR_MESSAGE_INVALID_CHILD_ADDITION)

        node = FileSystemNode(name=name, object_type=object_type, size=size, parent=self)
        self.children.append(node)

        if node.object_type == "file":
            self.size += node.size
            self.recalculate_size(new_node_size=node.size)

    def recalculate_size(self, new_node_size: int) -> None:
        parent = self.parent
        while parent:
            parent.size += new_node_size
            parent = parent.parent
