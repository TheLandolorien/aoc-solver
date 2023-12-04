import json
import os
import typing

from importlib import util as import_utilities
from types import ModuleType

SRC_PATH, PACKAGE_NAME = os.path.split(os.path.dirname(__file__))


def load_module(year: int, day: int) -> typing.Union[ModuleType, None]:
    formatted_day = str(day).zfill(2)
    module_name = f"{year}.day_{formatted_day}"
    relative_module_name = ".".join([PACKAGE_NAME, module_name])

    module_spec = None
    try:
        module_spec = import_utilities.find_spec(name=relative_module_name)
    except ModuleNotFoundError:
        os.makedirs(os.path.join(SRC_PATH, PACKAGE_NAME, str(year)))

    if not module_spec:
        return None

    module = import_utilities.module_from_spec(spec=module_spec)
    module_spec.loader.exec_module(module=module)

    return module


def read_file(path: str, type: str = "text") -> typing.Any:
    if type not in ["text", "json"]:
        raise AttributeError(f"Unsupported file type: {type}")

    with open(file=path, mode="r") as stream:
        if type == "text":
            return stream.read().splitlines()
        else:
            return json.load(fp=stream)
