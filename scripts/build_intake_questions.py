#!/usr/bin/env python3
"""Build request_user_input payloads for essay-tutor intake."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any


def question(
    *,
    header: str,
    question_id: str,
    prompt: str,
    options: list[tuple[str, str]],
) -> dict[str, Any]:
    return {
        "header": header,
        "id": question_id,
        "question": prompt,
        "options": [{"label": label, "description": description} for label, description in options],
    }


def sparse_payload() -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Scope",
                question_id="scope",
                prompt="What scope should the essay use?",
                options=[
                    ("1500-2000 words (Recommended)", "Allows enough depth for mechanism, evidence, and critical evaluation."),
                    ("About 1200 words", "Keeps the essay concise and compresses evidence discussion."),
                    ("User-specified limit", "Use this if the assignment has a fixed word or page limit."),
                ],
            ),
            question(
                header="Citations",
                question_id="citation_quantity",
                prompt="How dense should the citations be?",
                options=[
                    ("Standard density (Recommended)", "Use close citations for substantive claims while avoiding citation clutter."),
                    ("High density", "Use frequent claim-level citations for source-heavy or high-stakes work."),
                    ("Light density", "Use fewer citations only for short, reflective, or non-assessed work."),
                ],
            ),
            question(
                header="Format",
                question_id="format_requirements",
                prompt="What format should the final output use?",
                options=[
                    ("Default format (Recommended)", "Use the current Skill default for the requested output type."),
                    ("Plain chat text", "Return the work in chat with clean academic headings and references."),
                    ("Default DOCX", "Create a Word document using the Skill's default academic formatting."),
                ],
            ),
        ]
    }


def complete_payload() -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Confirm",
                question_id="brief_confirmation",
                prompt="Is the reconstructed assignment brief correct?",
                options=[
                    ("Correct (Recommended)", "Proceed to structure planning using the reconstructed brief."),
                    ("Needs changes", "Revise the brief before planning."),
                ],
            ),
            question(
                header="Citations",
                question_id="citation_quantity",
                prompt="Is the planned citation density correct?",
                options=[
                    ("Standard density (Recommended)", "Use close citations for substantive claims while avoiding citation clutter."),
                    ("High density", "Use frequent claim-level citations for source-heavy or high-stakes work."),
                    ("Light density", "Use fewer citations only for short, reflective, or non-assessed work."),
                ],
            ),
            question(
                header="Format",
                question_id="format_requirements",
                prompt="Is the planned output format correct?",
                options=[
                    ("Default format (Recommended)", "Use the current Skill default for the requested output type."),
                    ("Plain chat text", "Return the work in chat with clean academic headings and references."),
                    ("Default DOCX", "Create a Word document using the Skill's default academic formatting."),
                ],
            ),
        ]
    }


def brief_details_payload() -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Language",
                question_id="final_language",
                prompt="What language should the final work use?",
                options=[
                    ("English (Recommended)", "Fits most academic source material and English assignment titles."),
                    ("Chinese", "Use Chinese for the final submitted text."),
                    ("Chinese planning", "Use Chinese for planning but draft the final work in English."),
                ],
            ),
            question(
                header="Style",
                question_id="citation_style",
                prompt="What citation style should be used?",
                options=[
                    ("Assignment style (Recommended)", "Use the style named in the brief, rubric, or local guidance."),
                    ("Harvard", "Use Harvard-style in-text citations and reference list."),
                    ("APA 7", "Use APA 7 in-text citations and reference list."),
                ],
            ),
            question(
                header="Sources",
                question_id="source_base",
                prompt="What source base should the work use?",
                options=[
                    ("Course material (Recommended)", "Prioritise supplied readings, lecture material, and rubric evidence."),
                    ("Peer-reviewed literature", "Use academic literature found through reliable scholarly routes."),
                    ("Mixed source base", "Use course material plus external academic literature where needed."),
                ],
            ),
        ]
    }


def section_review_payload() -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Section",
                question_id="section_plan_feedback",
                prompt="What should happen with this section plan?",
                options=[
                    ("Approve section (Recommended)", "Keep this section plan and move to the next section."),
                    ("Revise focus", "Change the section's argument role, order, or emphasis before continuing."),
                    ("Revise evidence", "Change the evidence, citation density, or critical-analysis work for this section."),
                ],
            )
        ]
    }


def critical_analysis_payload() -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Critique",
                question_id="critical_analysis_feedback",
                prompt="What should happen with the critical-analysis plan?",
                options=[
                    ("Approve critique (Recommended)", "Use this critical stance in the final integrated plan."),
                    ("More critical", "Add stronger source, method, theory, or limitation evaluation."),
                    ("More balanced", "Reduce the critical emphasis and foreground explanation or synthesis."),
                ],
            )
        ]
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "scenario",
        choices=("sparse", "complete", "brief-details", "section-review", "critical-analysis"),
        help="Question payload scenario to generate.",
    )
    args = parser.parse_args()

    if args.scenario == "sparse":
        payload = sparse_payload()
    elif args.scenario == "complete":
        payload = complete_payload()
    elif args.scenario == "brief-details":
        payload = brief_details_payload()
    elif args.scenario == "section-review":
        payload = section_review_payload()
    else:
        payload = critical_analysis_payload()
    json.dump(payload, sys.stdout, ensure_ascii=True, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
