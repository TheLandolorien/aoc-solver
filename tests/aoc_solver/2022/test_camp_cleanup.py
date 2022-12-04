def test_check_assignment_containment(puzzle_module):
    assert puzzle_module.check_assignment_containment(set([2, 3, 4]), set([6, 7, 8])) == False, "should detect non-containment"
    assert puzzle_module.check_assignment_containment(set([1, 2]), set([1, 2, 3])) == True, "should detect same start containment"
    assert puzzle_module.check_assignment_containment(set([1, 2, 3]), set([2, 3])) == True, "should detect same stop containment"
    assert puzzle_module.check_assignment_containment(set([5]), set([2, 3, 4, 5, 6])) == True, "should detect single item containment"


def test_check_assignment_overlap(puzzle_module):
    assert puzzle_module.check_assignment_overlap(set([2, 3, 4]), set([6, 7, 8])) == False, "should detect non-overlap"
    assert puzzle_module.check_assignment_overlap(set([1, 2]), set([1, 2, 3])) == True, "should detect subset over"
    assert puzzle_module.check_assignment_overlap(set([1, 2, 3]), set([3, 4, 5])) == True, "should single item overlap"
    assert puzzle_module.check_assignment_overlap(set([5]), set([2, 3, 4, 5, 6])) == True, "should detect single item subset overlap"


def test_generate_range_set(puzzle_module):
    assert puzzle_module.generate_range_set(assignment="2-4") == set([2, 3, 4]), "should expand small range"
    assert puzzle_module.generate_range_set(assignment="0-10") == set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), "should expand larger range"
    assert puzzle_module.generate_range_set(assignment="7-7") == set([7]), "should collapse single item range"


def test_count_special_assignments(puzzle_module, mock_puzzle_input):
    assert puzzle_module.count_special_assignments(puzzle_input=mock_puzzle_input) == 2
    assert puzzle_module.count_special_assignments(puzzle_input=mock_puzzle_input, count_type="overlap") == 4
