from unittest.mock import mock_open, patch

from aoc_solver import utilities


@patch("builtins.open", new_callable=mock_open, read_data="A\nB\n\nC\n")
def test_read_lines_trims_new_lines(mock_open):
    lines = utilities.read_lines("foo/bar")

    assert lines == ["A", "B", "", "C"], "should trim newline characters"
    mock_open.assert_called_once_with(file="foo/bar", mode="r")
