import typing


def parse(puzzle_input: typing.List[str], calories: bool = False, strategy_guide: bool = False) -> typing.List[int]:
    if calories:
        return _parse_calories(calories=puzzle_input)
    elif strategy_guide:
        return _parse_strategy_guide(guide=puzzle_input)
    else:
        raise AttributeError("Must specify a parser type: [calories|strategy_guide]")


def _parse_calories(calories: typing.List[str] = None) -> typing.List[int]:
    grouped_calories = "".join(calories).strip().split("\n\n")
    return [sum(map(int, calories.split("\n"))) for calories in grouped_calories]


def _parse_strategy_guide(guide: typing.List[str]) -> typing.List[typing.List[str]]:
    predictions = "".join(guide).strip().split("\n")
    return [prediction.split(" ") for prediction in predictions]
