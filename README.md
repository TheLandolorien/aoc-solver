# Advent of Code Solutions

[TheLandolorien](https://github.com/TheLandolorien)'s solutions to [Advent of Code](https://adventofcode.com).

## ⚡️ Quick Start

Hey, [TheLandolorien](https://github.com/TheLandolorien)! Let's pick up where you left off (whether is was yesterday or last year when you gave up on solving around day 8 😅)!

### Environment Setup

You're still using a Python version manager like [pyenv](https://github.com/pyenv/pyenv), right?! And [Poetry](https://python-poetry.org) is still the new hotness for dependency manager?

If it is, you should be able to just install/update dependencies using

```shell
poetry install
```

If not, well... have fun figuring out those new management tools and updating this [README](./README.md).

### Displaying Solutions

If you want to run a solution from a previous session (say [Day 1: Calorie Counting from 2022](https://adventofcode.com/2022/day/1)), try:

```shell
aoc-solver 2022 calorie_counting
```

The format is `aoc-solver <YYYY> <puzzle_name>` where `<puzzle_name>` is the snake_case of the puzzle title.

And ta-da! You're ready to solve to jump back in! 🎉

## 🗂️ Project Organization

Puzzles solutions are grouped by year and modules are named after the title of the puzzle (snake_case). Puzzle inputs are saved with the same name as the module/puzzle and given a `.txt` extension.

```
src/
├── 2022/
│   ├── calorie_counting.py
│   ├── calorie_counting.txt
│   ├── ...
│   ├── <puzzle_name_n>.py
│   └── <puzzle_name_n>.txt
├── YYYY/
│   ├── ...
│   ├── <puzzle_name_n>.py
│   └── <puzzle_name_n>.txt
└── ...
```

Unit test modules are in the `tests/` directory (which mirrors the `src/` directory) and they use the `test_` prefix. Integration tests are under the `tests/integration/` directory.

## 🧩 Adding New Puzzle Solutions

Use the following steps to ensure the solver can automatically identify which solution to execute:

1. Create a `<puzzle_name>.py` module in the appropriate `src/aoc_solver/YYYY` directory.
1. Download the puzzle input to the corresponding `<puzzle_name>.txt` file in the same year directory.
1. Create a corresponding `test_<puzzle_name>.py` test module in the mirrored test directory.
1. Copy the example puzzle input to the corresponding `test_<puzzle_name>.txt` file in the same test directory.
1. Go ahead and write a test based on the example solution. (You know you're still doing TDD 🧪...)

   Example:

   ```python
   from aoc_solver.utilities import Solution

   def test_foo(puzzle_module, mock_puzzle_input):
       assert puzzle_module.solve(puzzle_input=mock_puzzle_input) == Solution(first="bar", second=None)
   ```

1. Add a `solve()` method that reads the corresponding puzzle input and returns a `Solution` named tuple for the solutions for 1st and 2nd parts of the puzzle. Also add the main method used for solving the puzzle that accepts the puzzle input and returns the example answer.

   Example:

   ```python
   import typing

   from aoc_solver.utilities import Solution

   # --- Day #: <Puzzle Name> ---
   # Source: https://adventofcode.com/YYYY/day/#

   def foo(puzzle_input: typing.List[str]) -> str:
       return "bar"

   def solve(puzzle_input=typing.List[str]) -> Solution:
       return Solution(
           first=foo(puzzle_input=puzzle_input),
           second=None,
       )
   ```

Huzzah! Running `aoc-solver` on the new puzzle should print the blank solution for your next puzzle and running `pytest` should pass with the hard-coded example answer! 🙌🏾

## 🧪 Running Tests

[`pytest`](https://docs.pytest.org/en/7.2.x/) is used as a test runner and its configuration can be found in the `tool.pytest.ini_options` section of [pyproject.toml](./pyproject.toml).

Running `pytest` with no arguments will:

- Automatically add `src` to `PYTHONPATH` (pythonpath: `src`)
- Only run unit tests (testpaths: `tests/aoc_solver`)
- Increase verbosity (`-vv`)
- Use the `importlib` for its import mode (`--import-mode=importlib`)

To run integration tests (which just checks how the solver executes random puzzles), use:

```shell
pytest tests/integration
```

## 🪪 License

This project template is [MIT licensed](https://github.com/thelandolorien/advent-of-code/blob/main/LICENSE).
