import os
import tempfile
import tomlkit

toml_text = """
[tool.sphinxcli]
name = "value"
[tool.sphinxcli.subtable]
name = "value"
"""


def test_tomlkit_roundtrip():
    out_data = tomlkit.parse(toml_text)
    print(type(out_data))

    tmp = tempfile.mkstemp()
    with open(tmp[1], "w") as tomlfp:
        tomlkit.dump(out_data, tomlfp)

    with open(tmp[1], "r") as tomlfp:
        in_data = tomlkit.load(tomlfp)

        assert in_data == out_data

    os.unlink(tmp[1])
