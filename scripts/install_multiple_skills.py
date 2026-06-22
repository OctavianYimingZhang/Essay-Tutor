#!/usr/bin/env python3
"""Install CourseWork Killer focused skills as top-level local Codex skills."""

from __future__ import annotations

import argparse
import filecmp
import pathlib
import shutil
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "skills"
DEFAULT_INSTALL_ROOT = ROOT.parent
MARKER = ".coursework_killer_generated"
LEGACY_MARKER = ".essay_tutor_generated"

FOCUSED_SKILLS = (
    "coursework-killer-intake-planning",
    "coursework-killer-research-citation",
    "coursework-killer-draft-revise",
    "coursework-killer-critical-analysis",
    "coursework-killer-lab-data",
    "coursework-killer-figures-legends",
    "coursework-killer-posters-presentations",
    "coursework-killer-website-coursework",
    "coursework-killer-docx-formatting",
    "coursework-killer-final-qa",
)

LEGACY_FOCUSED_SKILLS = (
    "essay-tutor-intake-planning",
    "essay-tutor-research-citation",
    "essay-tutor-draft-revise",
    "essay-tutor-critical-analysis",
    "essay-tutor-lab-data",
    "essay-tutor-figures-legends",
    "essay-tutor-posters-presentations",
    "essay-tutor-website-coursework",
    "essay-tutor-docx-formatting",
    "essay-tutor-final-qa",
)


def compare_dirs(source: pathlib.Path, target: pathlib.Path) -> list[str]:
    mismatches: list[str] = []
    comparison = filecmp.dircmp(source, target)
    for name in comparison.left_only:
        mismatches.append(f"missing in target: {target / name}")
    for name in comparison.diff_files:
        mismatches.append(f"different file: {target / name}")
    for subdir in comparison.common_dirs:
        mismatches.extend(compare_dirs(source / subdir, target / subdir))
    return mismatches


def install(install_root: pathlib.Path, check: bool, dry_run: bool) -> int:
    errors: list[str] = []
    if not check:
        for skill in LEGACY_FOCUSED_SKILLS:
            target = install_root / skill
            if not target.exists():
                continue
            if not (target / LEGACY_MARKER).is_file():
                errors.append(f"refusing to remove unmanaged legacy skill: {target}")
                continue
            if dry_run:
                print(f"would remove legacy skill {target}")
                continue
            shutil.rmtree(target)
            print(f"removed legacy skill {target}")
    for skill in FOCUSED_SKILLS:
        source = SOURCE_ROOT / skill
        target = install_root / skill
        if not (source / "SKILL.md").is_file():
            errors.append(f"missing source skill: {source}")
            continue
        if check:
            if not (target / "SKILL.md").is_file():
                errors.append(f"missing installed skill: {target}")
                continue
            errors.extend(compare_dirs(source, target))
            continue
        if target.exists() and not (target / MARKER).is_file():
            errors.append(f"refusing to overwrite unmanaged skill: {target}")
            continue
        if dry_run:
            print(f"would install {source} -> {target}")
            continue
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target)
        (target / MARKER).write_text(
            f"Generated from {source}\nRun {ROOT / 'scripts/install_multiple_skills.py'} to refresh.\n",
            encoding="utf-8",
        )
        print(f"installed {target}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", type=pathlib.Path, default=DEFAULT_INSTALL_ROOT, help="top-level Codex skills directory")
    parser.add_argument("--check", action="store_true", help="verify installed focused skills match the packaged sources")
    parser.add_argument("--dry-run", action="store_true", help="show actions without writing files")
    args = parser.parse_args()
    return install(args.path.expanduser().resolve(), args.check, args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
