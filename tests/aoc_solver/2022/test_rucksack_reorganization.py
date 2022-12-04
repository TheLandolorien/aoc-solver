def test_find_common_item_type(puzzle_module, mock_puzzle_input):
    first_rucksack = mock_puzzle_input[0].strip()
    second_rucksack = mock_puzzle_input[1].strip()
    third_rucksack = mock_puzzle_input[2].strip()

    assert puzzle_module.find_common_item_type(rucksacks=[first_rucksack]) == "p", "should find common lowercase items"
    assert puzzle_module.find_common_item_type(rucksacks=[second_rucksack]) == "L", "should find common uppercase items"
    assert (
        puzzle_module.find_common_item_type(rucksacks=[first_rucksack, second_rucksack, third_rucksack]) == "r"
    ), "should find common uppercase items in group"


def test_determine_priority(puzzle_module):
    assert puzzle_module.determine_priority("p") == 16, "should determine priority for lowercase items"
    assert puzzle_module.determine_priority("L") == 38, "should determine priority for uppercase items"
    assert puzzle_module.determine_priority("P") == 42, "should have case-sensitive priorities "


def test_calculate_total_common_item_priorities_by_rucksack(puzzle_module, mock_puzzle_input):
    assert puzzle_module.calculate_total_common_item_priorities(puzzle_input=mock_puzzle_input) == 157


def test_calculate_total_common_item_priorities_by_elf_trio(puzzle_module, mock_puzzle_input):
    assert puzzle_module.calculate_total_common_item_priorities(puzzle_input=mock_puzzle_input, group_size=3) == 70
