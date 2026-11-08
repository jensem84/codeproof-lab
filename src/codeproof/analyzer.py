"""Analyze a locally trusted project with Ruff and optionally pytest."""
import json
from pathlib import Path
from typing import Any

from codeproof.runner import run_module


def analyze(project: Path, *, run_tests: bool = False, timeout: int = 120) -> dict[str, Any]:
    root = project.resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Project must be a directory")
    lint = run_module("ruff", ["check", ".", "--output-format", "json"], root, timeout)
    try:
        findings = json.loads(lint.stdout)
        if not isinstance(findings, list):
            findings = []
    except json.JSONDecodeError:
        findings = []
    result: dict[str, Any] = {
        "schema_version": "1.0", "project": str(root),
        "lint": {"returncode": lint.returncode, "timed_out": lint.timed_out,
                 "findings": findings, "stderr": lint.stderr},
        "tests": None,
    }
    if run_tests:
        tests = run_module("pytest", ["-q", "-p", "no:cacheprovider"], root, timeout)
        result["tests"] = {"returncode": tests.returncode, "timed_out": tests.timed_out,
                           "stdout": tests.stdout, "stderr": tests.stderr}
    return result


def succeeded(report: dict[str, Any]) -> bool:
    return report["lint"]["returncode"] == 0 and (
        report["tests"] is None or report["tests"]["returncode"] == 0
    )
