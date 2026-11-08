import json

from codeproof.analyzer import succeeded
from codeproof.reporter import to_json, to_markdown


def sample(lint=0, tests=None):
    return {"schema_version": "1.0", "project": "/tmp/example", "lint": {
        "returncode": lint, "timed_out": False, "findings": [], "stderr": ""}, "tests": tests}


def test_pass_without_tests():
    assert succeeded(sample())
    assert "**PASS**" in to_markdown(sample())


def test_lint_failure():
    assert not succeeded(sample(lint=1))


def test_test_failure():
    assert not succeeded(sample(tests={"returncode": 1, "stdout": "failed", "stderr": ""}))


def test_json_roundtrip():
    assert json.loads(to_json(sample())) == sample()


def test_markdown_escapes_fences():
    data = sample(tests={"returncode": 0, "stdout": "```", "stderr": ""})
    assert "'''" in to_markdown(data)
