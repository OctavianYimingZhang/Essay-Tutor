#!/usr/bin/env python3
"""Validate the essay-tutor skill package."""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import subprocess
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
    "references/critical-writing-bank.md",
    "references/visuals-tables-data.md",
    "references/docx-output.md",
    "references/subagents.md",
    "references/qa-and-validation.md",
    "scripts/skill_maintenance.py",
    "scripts/build_intake_questions.py",
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


def validate_question_payload(payload: object, scenario: str, errors: list[str]) -> None:
    if not isinstance(payload, dict):
        errors.append(f"{scenario} intake payload must be a JSON object.")
        return
    questions = payload.get("questions")
    if not isinstance(questions, list) or not 1 <= len(questions) <= 3:
        errors.append(f"{scenario} intake payload must contain 1-3 questions.")
        return
    for index, item in enumerate(questions, start=1):
        if not isinstance(item, dict):
            errors.append(f"{scenario} question {index} must be an object.")
            continue
        for key in ("header", "id", "question", "options"):
            if key not in item:
                errors.append(f"{scenario} question {index} missing {key}.")
        if not isinstance(item.get("header"), str) or len(item.get("header", "")) > 12:
            errors.append(f"{scenario} question {index} header must be a short string.")
        if not isinstance(item.get("id"), str) or not re.fullmatch(r"[a-z][a-z0-9_]*", item.get("id", "")):
            errors.append(f"{scenario} question {index} id must be snake_case.")
        if not isinstance(item.get("question"), str) or not item.get("question", "").strip():
            errors.append(f"{scenario} question {index} must include question text.")
        options = item.get("options")
        if not isinstance(options, list) or not 2 <= len(options) <= 3:
            errors.append(f"{scenario} question {index} must include 2-3 options.")
            continue
        for option_index, option in enumerate(options, start=1):
            if not isinstance(option, dict):
                errors.append(f"{scenario} question {index} option {option_index} must be an object.")
                continue
            if not isinstance(option.get("label"), str) or not option.get("label", "").strip():
                errors.append(f"{scenario} question {index} option {option_index} missing label.")
            if not isinstance(option.get("description"), str) or not option.get("description", "").strip():
                errors.append(f"{scenario} question {index} option {option_index} missing description.")


def check_intake_question_policy(errors: list[str]) -> None:
    """Validate the code-backed request_user_input payload workflow."""
    files = {
        "SKILL.md": ROOT / "SKILL.md",
        "README.md": ROOT / "README.md",
        "agents/openai.yaml": ROOT / "agents/openai.yaml",
        "references/intake-and-planning.md": ROOT / "references/intake-and-planning.md",
        "references/drafting-and-critical-analysis.md": ROOT / "references/drafting-and-critical-analysis.md",
        "references/qa-and-validation.md": ROOT / "references/qa-and-validation.md",
    }
    text_by_rel = {rel: path.read_text(encoding="utf-8") for rel, path in files.items() if path.exists()}

    required_phrases = {
        "SKILL.md": [
            "python3 scripts/build_intake_questions.py sparse",
            "call `request_user_input` with the emitted JSON object",
            "citation quantity and format requirements",
            "CriticalAnalysisPlan",
        ],
        "references/intake-and-planning.md": [
            "scripts/build_intake_questions.py sparse",
            "call `request_user_input` with the emitted JSON object",
            "citation quantity or density",
            "format requirements",
            "free-form answer",
            "scripts/build_intake_questions.py brief-details",
            "SectionPlan",
            "CriticalAnalysisPlan",
            "scripts/build_intake_questions.py section-review",
            "scripts/build_intake_questions.py critical-analysis",
        ],
        "references/drafting-and-critical-analysis.md": [
            "approved section plans",
            "CriticalAnalysisPlan approval",
            "confirmed citation quantity",
            "format requirements",
        ],
        "agents/openai.yaml": [
            "generate request_user_input payloads with scripts/build_intake_questions.py",
            "citation quantity and format requirements",
            "review each detailed section plan and CriticalAnalysisPlan",
        ],
        "references/qa-and-validation.md": [
            "citation_quantity_confirmed",
            "format_requirements_confirmed",
            "section_by_section_plans_presented",
            "critical_analysis_plan_presented",
        ],
    }
    for rel, phrases in required_phrases.items():
        text = text_by_rel.get(rel, "")
        lowered = text.lower()
        for phrase in phrases:
            if phrase.lower() not in lowered:
                errors.append(f"Missing native intake question policy in {rel}: {phrase}")

    script = ROOT / "scripts/build_intake_questions.py"
    payloads: dict[str, object] = {}
    for scenario in ("sparse", "complete", "brief-details", "section-review", "critical-analysis"):
        try:
            completed = subprocess.run(
                [sys.executable, str(script), scenario],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            payload = json.loads(completed.stdout)
        except (subprocess.CalledProcessError, json.JSONDecodeError) as exc:
            errors.append(f"Failed to build {scenario} intake payload: {exc}")
            continue
        payloads[scenario] = payload
        validate_question_payload(payload, scenario, errors)

    for scenario in ("sparse", "complete"):
        payload = payloads.get(scenario)
        if not isinstance(payload, dict):
            continue
        questions = payload.get("questions", [])
        question_ids = {item.get("id") for item in questions if isinstance(item, dict)}
        for question_id in ("citation_quantity", "format_requirements"):
            if question_id not in question_ids:
                errors.append(f"{scenario} payload must ask for {question_id}.")
        labels = [
            option.get("label", "")
            for item in questions
            if isinstance(item, dict)
            for option in item.get("options", [])
            if isinstance(option, dict)
        ]
        if not any(label == "Default format (Recommended)" for label in labels):
            errors.append(f"{scenario} payload must include the default format option.")

    scenario_required_ids = {
        "brief-details": "source_base",
        "section-review": "section_plan_feedback",
        "critical-analysis": "critical_analysis_feedback",
    }
    for scenario, question_id in scenario_required_ids.items():
        payload = payloads.get(scenario)
        if not isinstance(payload, dict):
            continue
        questions = payload.get("questions", [])
        question_ids = {item.get("id") for item in questions if isinstance(item, dict)}
        if question_id not in question_ids:
            errors.append(f"{scenario} payload must include {question_id}.")

    payload = payloads.get("brief-details")
    if isinstance(payload, dict):
        questions = payload.get("questions", [])
        question_ids = {item.get("id") for item in questions if isinstance(item, dict)}
        for question_id in ("final_language", "citation_style", "source_base"):
            if question_id not in question_ids:
                errors.append(f"brief-details payload must include {question_id}.")


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
    check_intake_question_policy(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("essay-tutor validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
