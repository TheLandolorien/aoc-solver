# Advent of Code Solver

A python-based CLI tool to implement and review my solutions to [Advent of Code](https://adventofcode.com) puzzles.

> Disclaimer: These docs are written for me and by me. I offer no troubleshooting or support but feel to peruse my solutions and use a similar structure if you like my project organization.

## 🎄 Quick Start

Hey, [TheLandolorien](https://github.com/TheLandolorien)! Let's pick up where you left off (whether is was yesterday or last year when you gave up around day 8 😅)!

### Environment Setup

You're still using a Python version manager like [pyenv](https://github.com/pyenv/pyenv), right?! And [Poetry](https://python-poetry.org) is still the new hotness for dependency management?

If it is, clone this repo (if you need to) and just install/update dependencies using

```shell
poetry update
```

If not, well... have fun figuring out those new management tools and updating this [README](./README.md) 😉.

### Displaying Solutions

If you want to run a solution from a previous puzzle (say [Day 1: Calorie Counting from 2022](https://adventofcode.com/2022/day/1)), try:

```shell
aoc-solver --date 2022 1
```

And ta-da! You're ready to jump back in! 🎉

## 🗂️ Project Organization

Puzzles solutions are grouped by year and modules are named after the day the puzzle was released (format: `day_##.py`). Puzzle inputs are saved with the same name as the module/puzzle and given a `.txt` extension.

```
src/
├── 2022/
│   ├── day_01.py
│   ├── day_01.txt
│   ├── ...
│   ├── day_##.py
│   └── day_##.txt
├── YYYY/
│   ├── ...
│   ├── day_##.py
│   └── day_##.txt
└── ...
```

As for tests, unit tests are in the `tests/aoc_solver/` directory (which mirrors the `src/aoc_solver/` directory). Integration tests are under the `tests/integration/` directory.

## 🧩 Adding New Puzzle Solutions

Simply run `aoc-solver --date <year> <day>` to automatically download the example input and create a new solution module and corresponding test (if it hasn't been download already). The functionality is idempotent (it's safe to run back-to-back). It will only download resources if the solution module is missing and will not overwrite existing puzzle resources. (Worst case scenario: use `git` to roll-back any accidental overwrites 💻)

If you just want to download the latest puzzle available, you can run `aoc-solver` without any arguments.

Huzzah! Running `pytest -k '<year> and <day>'` will automatically pass with a default solution of `None`. May you never be in a state of having untested code! 🙌🏾

## 🧪 Running Tests

[`pytest`](https://docs.pytest.org/en/7.2.x/) is used as a test runner and its configuration can be found in the `tool.pytest.ini_options` section of [pyproject.toml](./pyproject.toml). [`pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/index.html) is used as a coverage reporter.

Running `pytest` with no arguments will:

- Automatically add `src` to `PYTHONPATH` (pythonpath: `src`)
- Only run unit tests (testpaths: `tests/aoc_solver`)
- Increase verbosity (`-vv`)
- Use the `importlib` for its import mode (`--import-mode=importlib`)
- Calculate coverage (using `pytest-cov`) and display any modules missing coverage

### Unit Tests

The [conftest.py](./tests/aoc_solver/conftest.py) for the `aoc_solver` package contains some helpful pytest fixtures:

- `mock_puzzle_inputs`: Automatically loads the correct example puzzle inputs based on the context of the test being run.
- `puzzle_module`: Automatically imports the module under test based on the context of the test being run (and allows us to have a numeric directory name when importing 😉).
- `project_directory`: Returns the project root directory to help with path building.

### Integration Tests

You can run integration tests using

```shell
pytest tests/integration
```

The main integration test ([test_solver.py](./tests/integration/test_solver.py)) just makes sure the CLI arguments end up running the correct puzzle solution.

## 🪪 License

This project template is [MIT licensed](./LICENSE).
