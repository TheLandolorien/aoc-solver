import typing


def read_lines(filepath: str) -> typing.List[str]:
    with open(file=filepath, mode="r") as f:
        return f.read().splitlines()
