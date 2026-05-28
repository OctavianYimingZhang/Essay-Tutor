#!/usr/bin/env python3
"""Validate the essay-tutor skill package."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "agents/openai.yaml",
    "skill_manifest.json",
    "references/intake-and-planning.md",
    "references/research-and-citation.md",
    "references/drafting-and-critical-analysis.md",
    "references/visuals-tables-data.md",
    "references/docx-output.md",
    "references/subagents.md",
    "references/qa-and-validation.md",
    "scripts/skill_maintenance.py",
    "scripts/validate_essay_tutor.py",
]

CJK_RE = re.compile(r"[\u3400-\u9fff\uf900-\ufaff]")
PLACEHOLDER_WORD = "".join(chr(code) for code in (84, 79, 68, 79))
PLACEHOLDER_MARKERS = ("[" + PLACEHOLDER_WORD, PLACEHOLDER_WORD + ":")


def iter_text_files() -> list[pathlib.Path]:
    paths: list[pathlib.Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        if path.suffix.lower() in {".md", ".yaml", ".yml", ".json", ".py", ".txt"} or path.name in {
            "LICENSE",
            "README.md",
            "SKILL.md",
        }:
            paths.append(path)
    return sorted(paths)


def check_required_files(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"Missing required file: {rel}")


def check_skill_frontmatter(errors: list[str]) -> None:
    path = ROOT / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter.")
        return
    try:
        _, frontmatter, _ = text.split("---", 2)
    except ValueError:
        errors.append("SKILL.md frontmatter is not closed.")
        return
    if "name: essay-tutor" not in frontmatter:
        errors.append("SKILL.md frontmatter must contain name: essay-tutor.")
    if "description:" not in frontmatter:
        errors.append("SKILL.md frontmatter must contain description.")
    if any(marker in frontmatter for marker in PLACEHOLDER_MARKERS):
        errors.append("SKILL.md frontmatter still contains template placeholder text.")


def check_english_only(errors: list[str], strict: bool) -> None:
    for path in iter_text_files():
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        if CJK_RE.search(text):
            errors.append(f"Non-English CJK character detected in {rel}")
        if strict and any(marker in text for marker in PLACEHOLDER_MARKERS):
            errors.append(f"template placeholder detected in {rel}")


def check_readme_and_license(errors: list[str]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8") if (ROOT / "LICENSE").exists() else ""
    if "Essay Tutor" not in readme:
        errors.append("README.md must describe Essay Tutor.")
    if "MIT License" not in license_text:
        errors.append("LICENSE must be MIT License text.")
    if "Octavian Yiming Zhang" not in license_text:
        errors.append("LICENSE must include the copyright holder.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="fail on template placeholders")
    args = parser.parse_args()

    errors: list[str] = []
    check_required_files(errors)
    if (ROOT / "SKILL.md").exists():
        check_skill_frontmatter(errors)
    check_english_only(errors, args.strict)
    check_readme_and_license(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("essay-tutor validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
