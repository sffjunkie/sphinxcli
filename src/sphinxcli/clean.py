from os.path import commonpath
from pathlib import Path
from shutil import rmtree

import rich


def clean_docs(target: Path, clean_all: bool = False) -> None:
    if not clean_all:
        rich.print(f"[green]Removing documents in {target}...[/]")

    target = target.resolve()
    for item in target.glob("*"):
        if item.is_dir():
            rmtree(item)
        else:
            item.unlink()


def clean_doctrees(doctrees: Path, clean_all: bool = False) -> None:
    if doctrees.exists():
        if not clean_all:
            rich.print(f"[green]Removing doctrees in {doctrees}...[/]")
        rmtree(doctrees)


def clean_all(target: Path, doctrees: Path):
    rich.print("[green]Cleaning all generated files[/]")
    if commonpath([doctrees, target]) != target:
        clean_doctrees(doctrees)

    clean_docs(target)
