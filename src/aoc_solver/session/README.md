# Authenticators

Advent of Code uses OAuth providers to authenticate your login (See: [How does authentication work?](https://adventofcode.com/2022/about#faq_auth)). Each supported OAuth provider just needs a new module using the Authenticator contract.

Each Authenticator should use [Selenium WebDriver](https://www.selenium.dev/documentation/) to prompt for provider login and streamline the OAuth process.

## Supported Providers

- [GitHub](https://adventofcode.com/auth/github)

## Methods

Authenticators are expected to have the following methods in order to be dynamically loaded into the solver.

| Name           | Description                                                                                    | Returns                       |
| -------------- | ---------------------------------------------------------------------------------------------- | ----------------------------- |
| `authenticate` | Authenticates via the indicated provider and stores an Advent of Code session cookie in `.env` | Advent of Code session cookie |
