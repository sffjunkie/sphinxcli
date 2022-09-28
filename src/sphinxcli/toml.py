from pathlib import Path
from typing import Any

import tomlkit


def set_value(pyproject: Path, table: str, setting: str, value: Any):
    data = toml_to_dict(pyproject)

    tool_config = data["tool"].get(table, None)
    if tool_config is None:
        tool_config = {}

    tool_config.update({setting: value})


def toml_to_dict(tomlfile: Path) -> dict[str, Any]:
    with open(tomlfile, "rb") as tomlfp:
        data = tomlkit.load(tomlfp)
        return data


def dict_to_toml(data: dict[str, Any], tomlfile: Path) -> None:
    with open(tomlfile, "wb") as tomlfp:
        tomlkit.dump(data, tomlfp)


def dict_to_sphinxconf(config: dict[str, Any]):
    ...


def toml_to_sphinxconf(tomlfile: Path):
    data = toml_to_dict(tomlfile)
    return dict_to_sphinxconf(data)
