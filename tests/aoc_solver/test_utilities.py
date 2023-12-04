from unittest.mock import ANY, mock_open, patch

import pytest

from aoc_solver import utilities


@patch("aoc_solver.utilities.import_utilities")
def test_load_module_locates_and_bootstraps_module(mock_importer):
    assert utilities.load_module(year=1900, day=1) is not None, "should load available module"

    mock_importer.find_spec.assert_called_once_with(name=f"aoc_solver.1900.day_01")
    mock_importer.module_from_spec.assert_called_once_with(
        spec=mock_importer.find_spec.return_value
    )
    mock_importer.find_spec.return_value.loader.exec_module.assert_called_once_with(
        module=mock_importer.module_from_spec.return_value
    )


@patch("aoc_solver.utilities.import_utilities")
def test_load_module_return_none_for_unavailable_modules(mock_importer):
    mock_importer.find_spec.return_value = None

    assert utilities.load_module(year=1900, day=1) is None, "should skip load for missing module"

    mock_importer.find_spec.assert_called_once_with(name="aoc_solver.1900.day_01")
    mock_importer.module_from_spec.assert_not_called()


@patch("aoc_solver.utilities.os")
@patch("aoc_solver.utilities.import_utilities")
def test_load_module_auto_creates_new_year_modules(mock_importer, mock_os):
    mock_importer.find_spec.side_effect = ModuleNotFoundError

    assert utilities.load_module(year=1900, day=1) is None, "should skip load for missing module"

    mock_importer.find_spec.assert_called_once_with(name="aoc_solver.1900.day_01")
    mock_os.path.join.assert_called_once_with(ANY, "aoc_solver", "1900")
    mock_os.makedirs.assert_called_once_with(mock_os.path.join.return_value)
    mock_importer.module_from_spec.assert_not_called()


@patch("builtins.open", new_callable=mock_open, read_data="A\nB\n\nC\n")
def test_read_file_reads_lines_for_text_files(mock_open):
    assert utilities.read_file(path="foo") == ["A", "B", "", "C"], "should read file as text"

    mock_open.assert_called_once_with(file="foo", mode="r")
    mock_open.return_value.read.assert_called_once()


@patch("builtins.open", new_callable=mock_open, read_data='{"foo": "bar"}')
def test_read_file_reads_lines_for_json_files(mock_open):
    assert utilities.read_file(path="foo", type="json") == {
        "foo": "bar"
    }, "should read file as json"

    mock_open.assert_called_once_with(file="foo", mode="r")
    mock_open.return_value.read.assert_called_once()


def test_read_file_raises_for_unsupported_file_type():
    with pytest.raises(AttributeError) as err:
        utilities.read_file(path="foo", type="yaml")

    assert (
        str(err.value) == "Unsupported file type: yaml"
    ), "should provide details for AttributeError"
