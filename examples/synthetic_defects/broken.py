"""Intentionally contains a Ruff F841 issue for demonstration."""


def greet(name: str) -> str:
    unused = 42
    return f"Hello, {name}!"
