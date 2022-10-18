"""pyproject.toml handling"""

from json import tool
from pathlib import Path
from typing import Any

import tomlkit
import tomlkit.container
import tomlkit.items

from sphinxcli.defaults import PYPROJECT_TABLE_NAME
from sphinxcli.types import Setting
from sphinxcli.toml import write_document, read_document


def sphinxcli_default_table() -> tomlkit.items.Table:
    """Create the default sphinxcli table definition"""
    table = tomlkit.table()
    table.name = "tool.sphinxcli"

    buidlers = tomlkit.array()
    buidlers.extend(["html"])
    table.append("buidlers", buidlers)

    base_path = Path("src") / "docs"

    source = tomlkit.string(str(base_path / "source"))
    table.append("source", source)
    table.append("config", source)

    target = tomlkit.string(str(base_path / "build"))
    table.append("target", target)

    doctree = tomlkit.string(str(base_path / "build" / "doctree"))
    table.append("doctree", doctree)

    languages = tomlkit.array()
    languages.extend(["en"])
    table.append("languages", languages)

    return table


def ensure_sphinxcli_table(pyproject: Path):
    """Create the sphinxcli table within pyproject.toml"""
    data = read_document(pyproject)

    tool_table = data["tool"]
    if isinstance(tool_table, tomlkit.items.Table):
        if PYPROJECT_TABLE_NAME not in tool_table:
            tool_config = sphinxcli_default_table()
            tool_table[PYPROJECT_TABLE_NAME] = tool_config
            write_document(pyproject, data)


def set_value(pyproject: Path, setting: Setting):
    """Set a value in the sphinxcli table"""
    data = read_document(pyproject)
    tool_table = data["tool"]
    if isinstance(tool_table, tomlkit.items.Table):
        sphinxcli_table = tool_table[PYPROJECT_TABLE_NAME]

        if isinstance(sphinxcli_table, tomlkit.items.Table):
            sphinxcli_table[setting.name] = setting.value
            write_document(pyproject, data)


def get_value(pyproject: Path, setting: Setting):
    """Set a value in the sphinxcli table"""
    data = read_document(pyproject)
    tool_table = data["tool"]
    if isinstance(tool_table, tomlkit.items.Table):
        sphinxcli_table = tool_table[PYPROJECT_TABLE_NAME]

        if (
            isinstance(sphinxcli_table, tomlkit.items.Table)
            and setting.name in sphinxcli_table
        ):
            return setting.value

    return KeyError(f"Unable to get setting {setting.name}")
