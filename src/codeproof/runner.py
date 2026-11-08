"""Run trusted installed tooling without invoking a shell."""
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CommandResult:
    command: list[str]
    returncode: int
    stdout: str
    stderr: str
    timed_out: bool = False


def run_module(module: str, args: list[str], cwd: Path, timeout: int = 120) -> CommandResult:
    command = [sys.executable, "-m", module, *args]
    try:
        result = subprocess.run(
            command, cwd=cwd, capture_output=True, text=True, timeout=timeout, check=False
        )
        return CommandResult(command, result.returncode, result.stdout, result.stderr)
    except subprocess.TimeoutExpired as exc:
        return CommandResult(command, 124, _decode(exc.stdout), _decode(exc.stderr), True)


def _decode(value: bytes | str | None) -> str:
    if value is None:
        return ""
    return value.decode(errors="replace") if isinstance(value, bytes) else value
