#!/usr/bin/env python3
"""Maintenance commands for the coursework-killer skill package."""

from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]


def run(command: list[str]) -> int:
    print("$ " + " ".join(command))
    completed = subprocess.run(command, cwd=ROOT)
    return completed.returncode


def doctor() -> int:
    commands = [
        [sys.executable, "-m", "compileall", "-q", "scripts"],
        [
            sys.executable,
            str(pathlib.Path.home() / ".codex/skills/.system/skill-creator/scripts/quick_validate.py"),
            str(ROOT),
        ],
        [sys.executable, "scripts/validate_coursework_killer.py", "--strict"],
    ]
    for command in commands:
        code = run(command)
        if code != 0:
            return code
    print("coursework-killer doctor passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("doctor", help="run package health checks")
    args = parser.parse_args()

    if args.command == "doctor":
        return doctor()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
