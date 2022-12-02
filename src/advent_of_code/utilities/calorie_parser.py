import typing


def parse(item_calories: typing.List[str]) -> typing.List[int]:
    grouped_calories = "".join(item_calories).strip().split("\n\n")
    return [sum(map(int, calories.split("\n"))) for calories in grouped_calories]
