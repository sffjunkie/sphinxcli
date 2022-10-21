from os.path import commonpath
from pathlib import Path
from shutil import rmtree

import rich

from sphinxcli.tool_config import ToolConfig


def clean_docs(target: Path) -> bool:
    target = target.resolve()
    targets = list(target.glob("*"))

    if len(targets) == 0:
        return False

    for item in targets:
        if item.is_dir():
            rmtree(item)
        else:
            item.unlink()

    return True


def clean_doctrees(doctrees: Path) -> bool:
    if not doctrees.exists():
        return False
    else:
        rmtree(doctrees)
        return True


def clean_all(tool_config: ToolConfig):
    outdir = Path(tool_config.settings.target or "build")
    doctreedir = Path(tool_config.settings.doctree or outdir)

    rich.print("[green]Cleaning all generated files[/]")

    if clean_docs(outdir):
        rich.print(f"  [green]Removed documents in {outdir}...[/]")

    if commonpath([doctreedir, outdir]) != outdir:
        if clean_doctrees(doctreedir):
            rich.print(f"  [green]Removed doctrees in {doctreedir}...[/]")
