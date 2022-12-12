import json
import os
import typing


CONFIG_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), ".env")


def store_session_cookie(session: typing.Optional[str] = None) -> None:
    with open(file=CONFIG_FILE_PATH, mode="r+") as config_file:
        config = json.load(config_file)
        config["AOC_SESSION"] = session
        json.dump(config, config_file)


def load_session_cookie() -> typing.Union[str, None]:
    with open(file=CONFIG_FILE_PATH, mode="r") as config_file:
        config = json.load(config_file)

    return config.get("AOC_SESSION")
