from pathlib import Path

from codeproof.cli import main


def test_missing_directory(tmp_path: Path):
    assert main([str(tmp_path / "missing")]) == 2


def test_invalid_timeout(tmp_path: Path):
    import pytest
    with pytest.raises(SystemExit) as exc:
        main([str(tmp_path), "--timeout", "0"])
    assert exc.value.code == 2
