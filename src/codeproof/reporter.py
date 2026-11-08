"""Deterministic JSON and Markdown report serialization."""
import json
from typing import Any

from codeproof.analyzer import succeeded


def to_json(report: dict[str, Any]) -> str:
    return json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def to_markdown(report: dict[str, Any]) -> str:
    lint = report["lint"]
    tests = report["tests"]
    lines = ["# CodeProof Lab Report", "", f"Overall: **{'PASS' if succeeded(report) else 'FAIL'}**", "",
             f"Lint exit code: `{lint['returncode']}`", f"Lint findings: {len(lint['findings'])}", ""]
    for item in lint["findings"][:100]:
        code = str(item.get("code", "unknown")).replace("`", "")
        message = str(item.get("message", "")).replace("\n", " ")
        lines.append(f"- `{code}`: {message}")
    if tests is not None:
        lines.extend(["", f"Test exit code: `{tests['returncode']}`", "",
                      "```text", tests["stdout"].replace("```", "'''"), "```"])
    return "\n".join(lines) + "\n"
