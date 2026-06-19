#!/usr/bin/env python3
"""Build request_user_input payloads for essay-tutor planning questions."""

from __future__ import annotations

import argparse
import json
import re
import sys
from typing import Any


Option = tuple[str, str]


def question(
    *,
    header: str,
    question_id: str,
    prompt: str,
    options: list[Option],
) -> dict[str, Any]:
    return {
        "header": short_header(header),
        "id": question_id,
        "question": prompt,
        "options": [{"label": label, "description": description} for label, description in options],
    }


def short_header(value: str) -> str:
    clean = re.sub(r"\s+", " ", value).strip()
    if len(clean) <= 12:
        return clean
    for separator in (":", "-", "("):
        if separator in clean:
            candidate = clean.split(separator, 1)[0].strip()
            if 1 <= len(candidate) <= 12:
                return candidate
    return clean[:12].rstrip()


def snake(value: str, fallback: str) -> str:
    clean = re.sub(r"[^a-zA-Z0-9]+", "_", value.lower()).strip("_")
    if not clean:
        clean = fallback
    if clean[0].isdigit():
        clean = f"{fallback}_{clean}"
    return clean[:48].rstrip("_")


def read_context(args: argparse.Namespace) -> dict[str, Any]:
    raw = args.context_json
    if args.context_file:
        if args.context_file == "-":
            raw = sys.stdin.read()
        else:
            with open(args.context_file, encoding="utf-8") as handle:
                raw = handle.read()
    if not raw:
        return {}
    parsed = json.loads(raw)
    if not isinstance(parsed, dict):
        raise SystemExit("context must be a JSON object")
    return parsed


def option_list(value: Any, fallback: list[Option]) -> list[Option]:
    if not isinstance(value, list):
        return fallback
    options: list[Option] = []
    for item in value[:3]:
        if isinstance(item, dict):
            label = str(item.get("label", "")).strip()
            description = str(item.get("description", "")).strip()
        elif isinstance(item, (list, tuple)) and len(item) >= 2:
            label = str(item[0]).strip()
            description = str(item[1]).strip()
        else:
            continue
        if label and description:
            options.append((label, description))
    return options if len(options) >= 2 else fallback


def scope_options(context: dict[str, Any]) -> list[Option]:
    fallback = [
        ("Assignment limit (Recommended)", "Use the word or page limit stated or implied by the current prompt."),
        ("Focused shorter scope", "Compress background and prioritise the highest-value evidence and analysis."),
        ("Expanded analytical scope", "Use more space for evidence comparison, limitations, and critical interpretation."),
    ]
    return option_list(context.get("scope_options"), fallback)


def citation_options(context: dict[str, Any]) -> list[Option]:
    fallback = [
        ("8-12 sources, standard density (Recommended)", "Use close citations for substantive claims without citation clutter."),
        ("15-25 sources, high density", "Use frequent claim-level citations for source-heavy assessed work."),
        ("User-specified count and density", "Use this when the brief requires an exact citation or reference count."),
    ]
    return option_list(context.get("citation_options"), fallback)


def format_options(context: dict[str, Any]) -> list[Option]:
    fallback = [
        ("Chat text (Recommended)", "Return the work in chat with academic headings and references."),
        ("DOCX formatted file", "Create a Word document and then ask for document formatting details."),
        ("LaTeX source/PDF", "Prepare LaTeX output and then ask for typography, layout, and reference-format details."),
    ]
    return option_list(context.get("format_options"), fallback)


def language_options(context: dict[str, Any]) -> list[Option]:
    fallback = [
        ("English (Recommended)", "Use English for the final academic text."),
        ("Prompt-language final", "Use the language of the user's prompt for the final submitted text."),
        ("Prompt-language planning + English draft", "Discuss the plan in the prompt language but draft the final work in English."),
    ]
    return option_list(context.get("language_options"), fallback)


def sparse_payload(context: dict[str, Any]) -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Scope",
                question_id="scope",
                prompt="Based on the displayed brief reconstruction, what scope should the work use?",
                options=scope_options(context),
            ),
            question(
                header="Citations",
                question_id="citation_quantity",
                prompt="Based on the displayed evidence plan, what citation count and density should be used?",
                options=citation_options(context),
            ),
            question(
                header="Format",
                question_id="format_requirements",
                prompt="Based on the displayed output plan, what final format should be produced?",
                options=format_options(context),
            ),
        ]
    }


def complete_payload(context: dict[str, Any]) -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Brief",
                question_id="brief_confirmation",
                prompt="After reviewing the displayed reconstructed brief, what should happen next?",
                options=option_list(
                    context.get("brief_confirmation_options"),
                    [
                        ("Use the reconstructed brief (Recommended)", "Proceed with the displayed goal, constraints, and evidence burden."),
                        ("Revise missing requirements", "Correct the brief before any structure or evidence planning continues."),
                    ],
                ),
            ),
            question(
                header="Citations",
                question_id="citation_quantity",
                prompt="Based on the displayed evidence plan, what citation count and density should be used?",
                options=citation_options(context),
            ),
            question(
                header="Format",
                question_id="format_requirements",
                prompt="Based on the displayed output plan, what final format should be produced?",
                options=format_options(context),
            ),
        ]
    }


def brief_details_payload(context: dict[str, Any]) -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Language",
                question_id="final_language",
                prompt="Based on the displayed language plan, what language should the final work use?",
                options=language_options(context),
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


def document_format_payload(context: dict[str, Any]) -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Typography",
                question_id="document_typography",
                prompt="Based on the displayed DOCX or LaTeX output plan, what typography should be used?",
                options=option_list(
                    context.get("typography_options"),
                    [
                        ("Arial or equivalent, 12 pt body (Recommended)", "Use a standard academic body font and readable size."),
                        ("Times-style, 12 pt body", "Use a traditional serif academic style."),
                        ("User-specified typography", "Use the exact font and size supplied by the brief or user."),
                    ],
                ),
            ),
            question(
                header="Layout",
                question_id="document_layout",
                prompt="Based on the displayed DOCX or LaTeX output plan, what layout should be used?",
                options=option_list(
                    context.get("layout_options"),
                    [
                        ("2.5 cm margins, 1.5 spacing (Recommended)", "Use the Skill's standard academic document layout."),
                        ("Compact margins and single spacing", "Best for strict page limits that require compression."),
                        ("User-specified layout", "Use exact margins, spacing, and alignment from the brief or user."),
                    ],
                ),
            ),
            question(
                header="Title/Refs",
                question_id="title_font_size",
                prompt="Based on the displayed DOCX or LaTeX output plan, how should title and references be formatted?",
                options=option_list(
                    context.get("title_reference_options"),
                    [
                        ("14 pt centred title, requested references (Recommended)", "Use a clear title size and the confirmed citation style."),
                        ("Compact title, requested references", "Reduce title size when page limits are tight."),
                        ("User-specified title and references", "Use exact title styling and reference formatting supplied by the user."),
                    ],
                ),
            ),
        ]
    }


def paragraph_options(title: str, plan: str, custom: Any) -> list[Option]:
    fallback = [
        (f"Keep {title}'s planned role (Recommended)", "Use the displayed claim path, evidence role, and transition as the drafting contract."),
        ("Change emphasis before drafting", "Adjust the paragraph's opening logic, evidence weight, or conceptual focus before writing."),
        ("Move, merge, or replace this paragraph", "Change this paragraph's position, combine it with another paragraph, or replace its function."),
    ]
    if plan:
        fallback[1] = (
            "Revise the displayed tradeoff",
            "Change the specific emphasis, evidence choice, or transition identified in the displayed paragraph plan.",
        )
    return option_list(custom, fallback)


def default_paragraphs() -> list[dict[str, Any]]:
    return [
        {
            "title": "Abstract",
            "plan": "Summarise the central answer, evidence route, and limits.",
            "options": [
                ("Keep thesis-led summary (Recommended)", "State the answer, evidence route, and limitation in a compact abstract."),
                ("Foreground method and source base", "Use the abstract to emphasise the evidence base before the answer."),
                ("Make the abstract more concise", "Reduce context and preserve only the answer and scope."),
            ],
        },
        {
            "title": "Introduction",
            "plan": "Move from the broad topic to the exact essay focus and thesis.",
            "options": [
                ("Use broad-to-specific opening (Recommended)", "Start with the broader topic, then narrow to the essay's model or argument."),
                ("Narrow faster to the thesis", "Reduce background and reach the central claim earlier."),
                ("Add more assignment context", "Spend more space defining the problem, key terms, or marking frame."),
            ],
        },
        {
            "title": "Main Body Paragraph 1: Core mechanism",
            "plan": "Explain the first mechanism or evidence route that carries the argument.",
            "options": [
                ("Lead with mechanism (Recommended)", "Make the causal or explanatory pathway the paragraph's first job."),
                ("Lead with evidence comparison", "Open with what the sources show before explaining the mechanism."),
                ("Split mechanism and evidence", "Separate dense mechanism and evidence into two planned paragraphs."),
            ],
        },
    ]


def section_review_payload(context: dict[str, Any]) -> dict[str, Any]:
    paragraphs = context.get("paragraphs")
    if not isinstance(paragraphs, list) or not paragraphs:
        paragraphs = default_paragraphs()
    questions: list[dict[str, Any]] = []
    for index, item in enumerate(paragraphs[:3], start=1):
        if isinstance(item, str):
            title = item
            plan = ""
            custom_options = None
        elif isinstance(item, dict):
            title = str(item.get("title") or item.get("label") or f"Main Body Paragraph {index}").strip()
            plan = str(item.get("plan") or item.get("decision_context") or "").strip()
            custom_options = item.get("options")
        else:
            continue
        questions.append(
            question(
                header=title,
                question_id=snake(f"section_{index}_{title}_feedback", f"section_{index}_feedback"),
                prompt=f"After reviewing the displayed paragraph plan for {title}, what should change before drafting?",
                options=paragraph_options(title, plan, custom_options),
            )
        )
    return {"questions": questions}


def critical_options(title: str, custom: Any) -> list[Option]:
    fallback = [
        ("Integrate in body and Discussion (Recommended)", "Use this evaluative move where the relevant claim is made and return to it in synthesis."),
        ("Place at strongest paragraph", "Use this move where it most improves causal or evidential precision."),
        ("Replace with a different critique", "Swap this move for a more relevant limitation, comparison, or constructive suggestion."),
    ]
    return option_list(custom, fallback)


def default_critical_moves() -> list[dict[str, Any]]:
    return [
        {"title": "Causal calibration", "placement": "Use where intervention or association evidence might otherwise be overstated."},
        {"title": "Model boundary", "placement": "Use where the essay distinguishes explanation from overgeneralisation."},
        {"title": "Method or source limitation", "placement": "Use where measurement, sample, timing, or source quality affects interpretation."},
    ]


def critical_analysis_payload(context: dict[str, Any]) -> dict[str, Any]:
    moves = context.get("critical_moves")
    if not isinstance(moves, list) or not moves:
        moves = default_critical_moves()
    questions: list[dict[str, Any]] = []
    for index, item in enumerate(moves[:3], start=1):
        if isinstance(item, str):
            title = item
            placement = ""
            custom_options = None
        elif isinstance(item, dict):
            title = str(item.get("title") or item.get("name") or f"Critical move {index}").strip()
            placement = str(item.get("placement") or item.get("plan") or "").strip()
            custom_options = item.get("options")
        else:
            continue
        placement_text = f" Placement plan: {placement}" if placement else ""
        questions.append(
            question(
                header=title,
                question_id=snake(f"critical_{index}_{title}_feedback", f"critical_{index}_feedback"),
                prompt=(
                    f"After reviewing the displayed critical-analysis plan for {title}, "
                    f"where should this move be used?{placement_text}"
                ),
                options=critical_options(title, custom_options),
            )
        )
    return {"questions": questions}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "scenario",
        choices=(
            "sparse",
            "complete",
            "brief-details",
            "docx-format",
            "document-format",
            "section-review",
            "critical-analysis",
        ),
        help="Question payload scenario to generate.",
    )
    parser.add_argument("--context-json", help="JSON object with dynamic question labels and options.")
    parser.add_argument("--context-file", help="Path to a JSON object, or '-' to read JSON from stdin.")
    args = parser.parse_args()
    context = read_context(args)

    if args.scenario == "sparse":
        payload = sparse_payload(context)
    elif args.scenario == "complete":
        payload = complete_payload(context)
    elif args.scenario == "brief-details":
        payload = brief_details_payload(context)
    elif args.scenario in {"docx-format", "document-format"}:
        payload = document_format_payload(context)
    elif args.scenario == "section-review":
        payload = section_review_payload(context)
    else:
        payload = critical_analysis_payload(context)
    json.dump(payload, sys.stdout, ensure_ascii=True, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
