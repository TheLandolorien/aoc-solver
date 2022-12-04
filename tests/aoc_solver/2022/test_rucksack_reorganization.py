import importlib

rucksack_reorganization = importlib.import_module("aoc_solver.2022.rucksack_reorganization")


def test_find_common_item_type(mock_puzzle_input):
    first_rucksack = mock_puzzle_input[0].strip()
    second_rucksack = mock_puzzle_input[1].strip()
    third_rucksack = mock_puzzle_input[2].strip()

    assert rucksack_reorganization.find_common_item_type(rucksacks=[first_rucksack]) == "p", "should find common lowercase items"
    assert rucksack_reorganization.find_common_item_type(rucksacks=[second_rucksack]) == "L", "should find common uppercase items"
    assert (
        rucksack_reorganization.find_common_item_type(rucksacks=[first_rucksack, second_rucksack, third_rucksack]) == "r"
    ), "should find common uppercase items in group"


def test_determine_priority():
    assert rucksack_reorganization.determine_priority("p") == 16, "should determine priority for lowercase items"
    assert rucksack_reorganization.determine_priority("L") == 38, "should determine priority for uppercase items"
    assert rucksack_reorganization.determine_priority("P") == 42, "should have case-sensitive priorities "


def test_calculate_total_common_item_priorities_by_rucksack(mock_puzzle_input):
    assert rucksack_reorganization.calculate_total_common_item_priorities(puzzle_input=mock_puzzle_input) == 157


def test_calculate_total_common_item_priorities_by_elf_trio(mock_puzzle_input):
    assert rucksack_reorganization.calculate_total_common_item_priorities(puzzle_input=mock_puzzle_input, group_size=3) == 70
