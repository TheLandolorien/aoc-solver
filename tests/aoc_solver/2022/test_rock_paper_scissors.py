def test_score_matches_predicts_score_with_suggested_plays(puzzle_module, mock_puzzle_input):
    assert puzzle_module.score_matches(puzzle_input=mock_puzzle_input) == 15


def test_score_matches_predicts_score_with_suggested_outcomes(puzzle_module, mock_puzzle_input):
    assert puzzle_module.score_matches(puzzle_input=mock_puzzle_input, score_type="outcome") == 12
