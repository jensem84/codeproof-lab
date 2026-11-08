from pathlib import Path

from codeproof.runner import run_module


def test_python_module_runner(tmp_path: Path):
    result = run_module("json.tool", ["--help"], tmp_path)
    assert result.returncode == 0
    assert not result.timed_out
