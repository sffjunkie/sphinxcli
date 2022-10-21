"""Reading and writing of TOML files"""

from pathlib import Path

import tomlkit
import tomlkit.container
import tomlkit.exceptions
import tomlkit.items
import tomlkit.toml_file


def read_document(tomlfile: Path) -> tomlkit.TOMLDocument:
    """Read a TOMLDocument from a file"""
    tfile = tomlkit.toml_file.TOMLFile(str(tomlfile))
    document = tfile.read()
    return document


def write_document(
    tomlfile: Path,
    document: tomlkit.TOMLDocument,
) -> None:
    """Write a TOMLDocument to a file"""
    tfile = tomlkit.toml_file.TOMLFile(str(tomlfile))
    tfile.write(document)


def get_tool_table(
    document: tomlkit.TOMLDocument, table_name: str
) -> tomlkit.items.Table | None:
    try:
        sphinxcli_table = document["tool"][table_name]  # type: ignore
        if isinstance(sphinxcli_table, tomlkit.items.Table):
            return sphinxcli_table
    except tomlkit.exceptions.NonExistentKey:
        return None
