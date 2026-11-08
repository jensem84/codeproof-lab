"""CodeProof CLI. Only run on code you trust."""
import argparse
import sys
from pathlib import Path

from codeproof.analyzer import analyze, succeeded
from codeproof.reporter import to_json, to_markdown


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Analyze a trusted local Python project")
    parser.add_argument("project", type=Path, help="Local project directory")
    parser.add_argument("--tests", action="store_true", help="Execute pytest (trusted code only)")
    parser.add_argument("--format", choices=["json", "markdown"], default="markdown")
    parser.add_argument("--output", type=Path, help="Write report to this path")
    parser.add_argument("--timeout", type=int, default=120, help="Timeout per tool, seconds")
    args = parser.parse_args(argv)
    if args.timeout < 1 or args.timeout > 600:
        parser.error("--timeout must be between 1 and 600 seconds")
    try:
        report = analyze(args.project, run_tests=args.tests, timeout=args.timeout)
    except (OSError, ValueError) as exc:
        print(f"codeproof: {exc}", file=sys.stderr)
        return 2
    output = to_json(report) if args.format == "json" else to_markdown(report)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0 if succeeded(report) else 1


if __name__ == "__main__":
    sys.exit(main())
