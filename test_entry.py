import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def test_entry_contract():
    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
        result = subprocess.run(
            [sys.executable, os.path.join(HERE, "main.py")],
            env=env,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, result.stderr
        path = os.path.join(tmp, "entry.txt")
        assert os.path.isfile(path), "entry.txt was not written"
        with open(path, encoding="utf-8") as f:
            text = f.read()
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be exactly one line"
    assert 1 <= len(text) <= 160, f"entry must be 1-160 characters, got {len(text)}"
    print(f"OK: one line, {len(text)} characters: {text}")


if __name__ == "__main__":
    test_entry_contract()
