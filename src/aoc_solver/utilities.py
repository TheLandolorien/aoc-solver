import json
import os
import typing

from importlib import util as import_utilities
from types import ModuleType

PACKAGE_NAME = os.path.basename(os.path.dirname(__file__))


def load_module(relative_module_name: str) -> typing.Union[ModuleType, None]:
    module_name = ".".join([PACKAGE_NAME, relative_module_name])
    module_spec = import_utilities.find_spec(name=module_name)

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
