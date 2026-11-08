# CodeProof Lab

Local-first Python code-quality evidence reports for **trusted, personally owned code**.

> Independent portfolio prototype. Not affiliated with Alignerr or RAAA. No claim of Alignerr approval or paid engagement.

## Features

- Run Ruff and optionally pytest against a trusted local Python project.
- Emit JSON or Markdown evidence reports.
- Deterministic exit codes: `0` all checks pass; `1` checks fail; `2` invalid input.
- Tool timeouts and subprocess execution without a shell.

## Windows setup (PowerShell)

Install Python 3.11+ and Git. In the repository directory:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pytest -q
python -m ruff check src tests
codeproof . --format json --output reports/self.json
codeproof examples/synthetic_defects --format markdown
```

The synthetic defect example intentionally returns exit code 1.

## Safety

**Do not run this on untrusted repositories.** Ruff reads source; `--tests` executes pytest and potentially arbitrary project code, including plugins and test configuration. This is not a sandbox. Never pass startup-owned source, secrets, personal data, or customer code. Output paths may overwrite files; review paths first.

## Limitations

This is an MVP. It does not sandbox execution, audit dependencies, prove security, verify correctness of AI-generated code, or guarantee eligibility for any external program. Ruff/pytest installation is required. Reports are evidence of local tool outcomes, not security certifications.

## Development

See `docs/architecture.md`, `docs/development-journal.md`, and `docs/publication.md`.
