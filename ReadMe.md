# SphinxCLI

A CLI tool to ease the generation Sphinx documents by allowing for multiple builders and multiple languages to be built using a single command.

There are 2 ways of using the tool. As a REPL or as individual commands.

```sh
sphinxcli build
sphinxcli build html
sphinxcli build html:latex
sphinxcli build html en
sphinxcli build html en:fr
```

## Commands

### commands

### build

To run all builders and all languages defined in the config file use

```sh
sphinxcli build
```

To run a specific builder specify it after the build command

```sh
sphinxcli build html
```

To run multiple builders add them after the build command separated by `:` characters.

```sh
sphinxcli build "html:latex"
```

To generate documents for specific languages specify them after the builders.

```sh
sphinxcli build html "en:fr"
```

### clean

Removes any built files (documents and doctrees)

### get

Get a setting's value

### set

Set a setting's value and update the `pyproject.toml` file.

### settings

Display a list of the current settings

```text
SphinxCLI Settings
  source       = src/docs/source
  target       = docs
  builders     = ['html']
  languages    = ['en']
  config       = src/docs/source
  doctree      = src/docs/build/doctree
  target_order = builder
```

### version

## Configuration

The tool is configured within the `pyproject.toml` file.

The `builders` item defines which builders are run by default and can be specified as

- a string with one builder e.g. `html`
- a string with multiple builders separated by a `:` character e.g. `html:latex`
- a list of builders e.g. `["html", "latex"]`

The `source` item defines the folder where the Sphinx source files (`.rst`/`.md`) can be found.

The `target` item specifies where the built files will be written

The `languages` specifies the default languages to be built and can be specified like the `builders` item.

The `config` item specifies the directory where the Sphinx `conf.py` can be found.

The `doctree` item specifies where the Sphinx environment files will be stored.

The `target_order` item specifies how the built files will be structured.
It can be either

- `builder` which means the files will be written to the folder structure `target/builder/language`
- `language` which means the files will be written to the folder structure `target/language/builder`

```toml
[tool.sphinxcli]
builders = ["html"]
source = "src/docs/source"
target = "docs"
languages = ["en"]
config = "src/docs/source"
doctree = "src/docs/build/doctree"
target_order = "builder"
```
