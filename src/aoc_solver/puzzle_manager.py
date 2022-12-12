import os
import requests

from aoc_solver.session import authenticator

# TODO: Migrate puzzle management methods from utilities
SRC_PATH, PACKAGE_NAME = os.path.split(os.path.dirname(__file__))


def get_puzzle_input(year: int, day: int, auth_provider: str = "github") -> str:
    session_cookie = authenticator.authenticate(provider=auth_provider)

    session = requests.Session()
    session.cookies.set(name="session", value=session_cookie)

    puzzle_response = session.get(url=f"https://adventofcode.com/{year}/day/{day}/input")
    puzzle_response.raise_for_status()

    return puzzle_response.text
