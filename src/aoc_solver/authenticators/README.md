# Authenticators

Advent of Code uses OAuth providers to authenticate your login (See: [How does authentication work?](https://adventofcode.com/2022/about#faq_auth)). Each supported OAuth provider just needs a new module using the Authenticator contract.

## Supported Providers

- [GitHub](https://adventofcode.com/auth/github)
  - NOTE: Currently expects 2FA authentication to be enabled and will prompt for a one-time password (OTP) when retrieving puzzle input.

## Methods

Authenticators are expected to have the following methods in order to be dynamically loaded into the solver.

| Name    | Description                                                                             | Arguments                           | Returns                                        | Raises                               |
| ------- | --------------------------------------------------------------------------------------- | ----------------------------------- | ---------------------------------------------- | ------------------------------------ |
| `login` | Creates a requests Session logged into Advent of Code using GitHub as an OAuth provider | - `username`: GitHub login/username | Advent of Code-authentication requests Session | - `HTTPError` for any request errors |
