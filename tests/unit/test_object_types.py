import pytest

from aoc_solver.object_types import ExamplePuzzleInputParser, FileSystemNode


class TestFileSystemNode:
    def test_constructor_raises_for_invalid_child_addition(self):
        with pytest.raises(AttributeError) as err:
            FileSystemNode(
                name="a.txt",
                object_type="file",
                size=100,
                children=[FileSystemNode(name="b.log", object_type="file", size=200)],
            )

        assert (
            str(err.value) == "Children can only be added to directories"
        ), "should raise for invalid child addition"

    @pytest.mark.parametrize(
        "scenario,node,expected_output",
        [
            (
                "root without children",
                FileSystemNode(name="/", object_type="dir"),
                "FileSystemNode(name=/, object_type=dir, size=0, children=[])",
            ),
            (
                "flat directory structure",
                FileSystemNode(
                    name="/",
                    object_type="dir",
                    children=[
                        FileSystemNode(name="a.txt", object_type="file", size=100),
                        FileSystemNode(name="b.log", object_type="file", size=200),
                    ],
                ),
                "FileSystemNode(name=/, object_type=dir, size=0, children=[FileSystemNode(name=a.txt, object_type=file, size=100, children=[]), FileSystemNode(name=b.log, object_type=file, size=200, children=[])])",
            ),
            (
                "nested directory structure",
                FileSystemNode(
                    name="/",
                    object_type="dir",
                    children=[
                        FileSystemNode(
                            name="a",
                            object_type="dir",
                            children=[FileSystemNode(name="b.log", object_type="file", size=200)],
                        ),
                    ],
                ),
                "FileSystemNode(name=/, object_type=dir, size=0, children=[FileSystemNode(name=a, object_type=dir, size=0, children=[FileSystemNode(name=b.log, object_type=file, size=200, children=[])])])",
            ),
        ],
    )
    def test_string_representation(self, scenario, node, expected_output):
        assert str(node) == expected_output, f"should print {scenario}"

    def test_add_child_raises_for_invalid_addition(self):
        with pytest.raises(AttributeError) as err:
            FileSystemNode(name="a.txt", object_type="file", size=100).add_child(
                name="b.log", object_type="file", size=200
            )

        assert (
            str(err.value) == "Children can only be added to directories"
        ), "should raise for invalid child addition"

    def test_add_and_find_children(self):
        root = FileSystemNode(name="/", object_type="dir")
        root.add_child(name="a", object_type="dir")
        root.add_child(name="a", object_type="dir")

        assert len(root.children) == 2, "should append children"
        assert len(root.find_children(name="a")) == 2, "should find duplicate children"

    def test_recalculate_size_updates_ancestors_of_new_files(self):
        root = FileSystemNode(name="/", object_type="dir")
        assert root.size == 0, "should initialize root directory at size 0"

        root.add_child(name="a", object_type="dir")
        assert root.size == 0, "should not increase size for new child directories"

        root.add_child(name="b.txt", object_type="file", size=200)
        assert root.size == 200, "should increase size for new child files"

        root.children[0].add_child(name="c", object_type="dir")
        assert root.size == 200, "should not increase size for new grandchild directories"

        root.children[0].add_child(name="d.log", object_type="file", size=400)
        assert root.size == 600, "should increase size for new grandchild files"

        root.children[0].children[0].add_child(name="e.csv", object_type="file", size=500)
        assert root.size == 1100, "should increase size for new great-grandchild files"


class TestExamplePuzzleInputParser:
    @pytest.fixture
    def instance(self):
        return ExamplePuzzleInputParser()

    def test_parser_extracts_puzzle_title(self, instance):
        instance.feed("<h2>--- Day 0: Puzzle Title ---</h2>")
        instance.close()

        assert instance.puzzle_title == "--- Day 0: Puzzle Title ---", "should extract puzzle title"

    def test_parser_extracts_example_input(self, instance):
        puzzle_example_html = "<p>For example:</p>\n" "<pre><code>" "A\nB\nC" "</code></pre>"
        instance.feed(puzzle_example_html)
        instance.close()

        assert instance.example_input == "A\nB\nC", "should extract example input"
