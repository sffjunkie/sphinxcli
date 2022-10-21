"""pyproject.toml handling"""

from pathlib import Path
from typing import Any

import tomlkit
import tomlkit.container
import tomlkit.items

from sphinxcli.defaults import PYPROJECT_TABLE_NAME
from sphinxcli.findfile import rfindfile
from sphinxcli.toml import get_tool_table, read_document, write_document
from sphinxcli.types import Setting


def sphinxcli_default_table() -> tomlkit.items.Table:
    """Create the default sphinxcli table definition"""
    root = tomlkit.table()
    table = tomlkit.table()

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

    root["tool.sphinxcli"] = table
    return root


def find(path: Path | None = None) -> Path | None:
    """Find the pyproject.toml file ion the path specified
    or the current working directory if not specified.
    """
    if path is None:
        path = Path.cwd()
    pyproject = rfindfile("pyproject.toml", path)
    return pyproject


def load(path: Path | None = None) -> tuple[Path | None, tomlkit.TOMLDocument | None]:
    """Load the pyproject.toml file"""
    if (pyproject := find(path)) is not None:
        document = read_document(pyproject)
        return pyproject, document

    return None, None


def get_value(pyproject: Path, setting: Setting) -> Any:
    """Read a value from the sphinxcli table"""
    document = read_document(pyproject)
    if document is None:
        return None

    pyproject_table = get_tool_table(document, PYPROJECT_TABLE_NAME)
    if pyproject_table is None:
        return None

    if setting.name not in pyproject_table:
        raise KeyError(f"Unknown setting {setting.name}")

    return pyproject_table[setting.name]


def set_value(pyproject: Path, setting: Setting) -> Any:
    """Set a value in the sphinxcli table and write to disk"""
    document = read_document(pyproject)
    if document is None:
        return None

    pyproject_table = get_tool_table(document, PYPROJECT_TABLE_NAME)
    if pyproject_table is None:
        return None

    if setting.name not in pyproject_table:
        raise KeyError(f"Unknown setting {setting.name}")

    if (
        setting.name in pyproject_table
        and setting.value != pyproject_table[setting.name]
    ):
        pyproject_table[setting.name] = setting.value
        write_document(pyproject, document)
        return setting.value
