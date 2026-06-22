#!/usr/bin/env python3
"""Build request_user_input payloads for coursework-killer planning questions."""

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


def task_type_payload(context: dict[str, Any]) -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Task Type",
                question_id="task_type",
                prompt="Based on the displayed brief reconstruction, what task-specific workflow should be used?",
                options=option_list(
                    context.get("task_type_options"),
                    [
                        ("Essay or Lab Report (Recommended)", "Use prose-led planning with evidence, citation, method, result, and discussion controls."),
                        ("Poster or Presentation", "Use visual-story planning for panels, slides, message hierarchy, and speaker or display constraints."),
                        ("Interactive Website or Figure Generation", "Use output-specific planning for interaction, figure generation, legends, and source-backed visual assets."),
                    ],
                ),
            ),
        ]
    }


def lab_analysis_payload(context: dict[str, Any]) -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Tool",
                question_id="analysis_tool",
                prompt="Which software or tool will produce or has produced the analysis output?",
                options=option_list(
                    context.get("analysis_tool_options"),
                    [
                        ("GraphPad Prism (Recommended)", "Use Prism project files, exported results, or Prism screenshots as the authoritative output."),
                        ("R Studio, Python, or MatLab", "Use scripts, notebooks, console output, or exported tables as the authoritative output."),
                        ("Spreadsheet or user-specified tool", "Use Excel, Google Sheets, SPSS, Jamovi, or another tool named by the user."),
                    ],
                ),
            ),
            question(
                header="Method",
                question_id="analysis_method",
                prompt="What statistical test, model, or descriptive method should the lab report use?",
                options=option_list(
                    context.get("analysis_method_options"),
                    [
                        ("Use method from brief/output (Recommended)", "Use only the test or model verified from assignment instructions or supplied analysis output."),
                        ("User-specified method", "Use the exact method the user supplies, such as two-way repeated-measures ANOVA."),
                        ("Need method selection discussion", "Pause result-writing and discuss valid methods from the study design and data structure."),
                    ],
                ),
            ),
            question(
                header="Scope",
                question_id="analysis_scope",
                prompt="How should the analysis be used in the report?",
                options=option_list(
                    context.get("analysis_scope_options"),
                    [
                        ("Report supplied output only (Recommended)", "Interpret the verified analysis without re-running or changing the method."),
                        ("Check and reproduce analysis", "Review data structure, cleaning, assumptions, and reproducibility before writing results."),
                        ("Plan analysis before results", "Build an analysis plan first because the output is not yet available or is incomplete."),
                    ],
                ),
            ),
        ]
    }


def poster_plan_payload(context: dict[str, Any]) -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Canvas",
                question_id="poster_canvas",
                prompt="What poster canvas, orientation, and submission format should the plan target?",
                options=option_list(
                    context.get("poster_canvas_options"),
                    [
                        ("Use assignment format (Recommended)", "Follow the size, orientation, and file type stated in the brief or rubric."),
                        ("Academic A0/A1 poster", "Plan a standard academic poster layout with readable title, panels, and figures."),
                        ("User-specified canvas", "Use the user's exact dimensions, orientation, software, or submission file type."),
                    ],
                ),
            ),
            question(
                header="Message",
                question_id="poster_message_hierarchy",
                prompt="What should control the poster's message hierarchy?",
                options=option_list(
                    context.get("poster_message_options"),
                    [
                        ("Central finding first (Recommended)", "Make title, visual order, and panel emphasis lead to the main take-home message."),
                        ("Methods and results balanced", "Give more space to study design, methods, figures, and result interpretation."),
                        ("Audience-led explanation", "Prioritise context and definitions for a less specialised marker or public audience."),
                    ],
                ),
            ),
            question(
                header="Assets",
                question_id="poster_visual_assets",
                prompt="Which visual or data assets must the poster plan include?",
                options=option_list(
                    context.get("poster_visual_options"),
                    [
                        ("Use supplied figures/data (Recommended)", "Plan around the figures, tables, diagrams, or outputs already provided."),
                        ("Create new source-backed visuals", "Generate or design diagrams, summary figures, or tables from verified evidence."),
                        ("Need asset inventory first", "Pause layout planning until required figures, data, legends, and permissions are identified."),
                    ],
                ),
            ),
        ]
    }


def presentation_plan_payload(context: dict[str, Any]) -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Timing",
                question_id="presentation_timing",
                prompt="What duration, slide count, or timing constraint should the storyboard use?",
                options=option_list(
                    context.get("presentation_timing_options"),
                    [
                        ("Use assignment timing (Recommended)", "Follow the duration, slide count, or time-per-speaker stated in the brief."),
                        ("Concise assessed talk", "Plan a short, tightly paced academic presentation with few high-value slides."),
                        ("User-specified timing", "Use the user's exact duration, slide count, and speaking arrangement."),
                    ],
                ),
            ),
            question(
                header="Audience",
                question_id="presentation_audience",
                prompt="Who is the presentation for, and what assessment mode should it satisfy?",
                options=option_list(
                    context.get("presentation_audience_options"),
                    [
                        ("Academic marker (Recommended)", "Prioritise rubric fit, evidence, method clarity, and scholarly explanation."),
                        ("Mixed or public audience", "Use more context, clearer definitions, and less dense slide text."),
                        ("Panel, seminar, or group role", "Adapt the storyboard to Q&A, seminar discussion, or assigned speaker roles."),
                    ],
                ),
            ),
            question(
                header="Notes",
                question_id="presentation_notes",
                prompt="What speaking support should be produced with the slides or storyboard?",
                options=option_list(
                    context.get("presentation_notes_options"),
                    [
                        ("Speaker notes (Recommended)", "Write concise notes that explain each slide without overcrowding the slide text."),
                        ("Full script", "Prepare a spoken script aligned to timing and slide transitions."),
                        ("Slide text only", "Plan slide content and visual order without notes or a full script."),
                    ],
                ),
            ),
        ]
    }


def website_plan_payload(context: dict[str, Any]) -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Output",
                question_id="website_output_mode",
                prompt="What website output mode should the academic plan target?",
                options=option_list(
                    context.get("website_output_options"),
                    [
                        ("Interactive website (Recommended)", "Plan content, navigation, interactions, citations, and accessible user flow."),
                        ("Static website", "Plan linked pages or sections with academic copy and visuals but minimal interaction."),
                        ("Prototype/spec only", "Produce a storyboard, wireframe text, or implementation brief rather than building files."),
                    ],
                ),
            ),
            question(
                header="Journey",
                question_id="website_interaction_model",
                prompt="What user journey or interaction type should carry the academic argument?",
                options=option_list(
                    context.get("website_interaction_options"),
                    [
                        ("Guided narrative (Recommended)", "Use scrolling, sections, or step-by-step navigation to teach the topic."),
                        ("Explore data or figures", "Use filters, charts, reveal states, or comparisons around supplied data and visuals."),
                        ("Decision or quiz interaction", "Use prompts, checkpoints, or branching to test understanding or choices."),
                    ],
                ),
            ),
            question(
                header="Platform",
                question_id="website_platform_constraints",
                prompt="What platform, technology, or submission constraints must the website follow?",
                options=option_list(
                    context.get("website_platform_options"),
                    [
                        ("Use assignment constraints (Recommended)", "Follow the platform, file type, accessibility, and hosting rules in the brief."),
                        ("Simple HTML/CSS/JS", "Plan a local static implementation that can run without a backend."),
                        ("User-specified stack", "Use the user's required tool, CMS, framework, or institutional platform."),
                    ],
                ),
            ),
        ]
    }


def figure_plan_payload(context: dict[str, Any]) -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Purpose",
                question_id="figure_purpose",
                prompt="What should the figure do for the assignment?",
                options=option_list(
                    context.get("figure_purpose_options"),
                    [
                        ("Explain a mechanism (Recommended)", "Use a source-backed schematic to show a pathway, process, model, or relationship."),
                        ("Present data/results", "Use a data figure that preserves labels, units, sample sizes, uncertainty, and statistics."),
                        ("Summarise or compare evidence", "Use a conceptual, comparison, workflow, or limitation figure."),
                    ],
                ),
            ),
            question(
                header="Basis",
                question_id="figure_source_basis",
                prompt="What source or data basis should constrain the figure content?",
                options=option_list(
                    context.get("figure_source_options"),
                    [
                        ("User data or supplied sources (Recommended)", "Use only supplied data, assignment material, and verified sources."),
                        ("Peer-reviewed source-backed schematic", "Create an original figure from verified literature and cite those sources."),
                        ("Existing figure with permission check", "Use or adapt a supplied or published figure only after authorship and permission are clear."),
                    ],
                ),
            ),
            question(
                header="Tool",
                question_id="figure_generation_tool",
                prompt="What tool or workflow should be used to make or edit the figure?",
                options=option_list(
                    context.get("figure_tool_options"),
                    [
                        ("BioRender or diagram tool (Recommended)", "Use a structured scientific-figure workflow with editable labels and panels."),
                        ("Image generation or editing", "Use generated or edited imagery while keeping scientific claims source-backed."),
                        ("User-specified tool", "Use the user's required software, style guide, file format, or template."),
                    ],
                ),
            ),
        ]
    }


def figure_legend_payload(context: dict[str, Any]) -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Depth",
                question_id="legend_depth",
                prompt="How detailed should the figure legend be?",
                options=option_list(
                    context.get("legend_depth_options"),
                    [
                        ("Complete submit-ready legend (Recommended)", "State what is shown, the reader takeaway, and all details needed for interpretation."),
                        ("Concise caption", "Use a shorter legend suitable for a poster, slide, or word-limited figure."),
                        ("Journal-style full legend", "Include panel-by-panel descriptions, methods, statistics, and abbreviations."),
                    ],
                ),
            ),
            question(
                header="Stats",
                question_id="legend_statistics",
                prompt="What statistical or technical details must the legend include?",
                options=option_list(
                    context.get("legend_statistics_options"),
                    [
                        ("Use verified analysis output (Recommended)", "Report sample sizes, tests, p values, error bars, units, and scale bars only when supplied or verified."),
                        ("Methods-light legend", "Include groups, conditions, units, and abbreviations but keep statistical detail in the Results text."),
                        ("Need details from user", "Pause legend writing until sample basis, statistics, labels, or abbreviations are supplied."),
                    ],
                ),
            ),
            question(
                header="Source",
                question_id="legend_source_note",
                prompt="What source, authorship, or permission note should accompany the legend?",
                options=option_list(
                    context.get("legend_source_options"),
                    [
                        ("Use supplied source note (Recommended)", "Include the citation, data basis, authorship, or permission statement from the brief or user."),
                        ("Original figure from verified sources", "Cite the sources behind the content rather than claiming direct reuse."),
                        ("Permission unclear", "Mark reuse or authorship as unresolved before finalising the figure legend."),
                    ],
                ),
            ),
        ]
    }


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


def planning_approval_payload(context: dict[str, Any]) -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Approval",
                question_id="planning_approval",
                prompt="After reviewing the displayed final integrated plan, what should happen next?",
                options=option_list(
                    context.get("planning_approval_options"),
                    [
                        (
                            "Approve final plan (Recommended)",
                            "Proceed directly to writing from the approved plan without a redundant start-writing confirmation.",
                        ),
                        (
                            "Revise evidence emphasis",
                            "Change the source balance, citation distribution, data emphasis, or critical-analysis weighting before writing.",
                        ),
                        (
                            "Revise structure or scope",
                            "Change the thesis scope, section order, output contract, word budget, or task-specific workflow before writing.",
                        ),
                    ],
                ),
            )
        ]
    }


def writing_gate_payload(context: dict[str, Any]) -> dict[str, Any]:
    return {
        "questions": [
            question(
                header="Writing",
                question_id="writing_gate",
                prompt="A plan-breaking issue appeared after approval. How should the main agent resolve it before continuing?",
                options=option_list(
                    context.get("writing_gate_options"),
                    [
                        (
                            "Resolve with supplied evidence (Recommended)",
                            "Narrow, reword, or omit the affected claim using verified supplied evidence and continue writing.",
                        ),
                        (
                            "Pause and supply missing evidence",
                            "Stop the affected section until the missing source, data, method, rubric, or format detail is supplied.",
                        ),
                        (
                            "Revise approved plan",
                            "Update the thesis, structure, evidence scope, citation strategy, or output contract before continuing.",
                        ),
                    ],
                ),
            )
        ]
    }


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
            "task-type",
            "lab-analysis",
            "poster-plan",
            "presentation-plan",
            "website-plan",
            "figure-plan",
            "figure-legend",
            "section-review",
            "critical-analysis",
            "planning-approval",
            "writing-gate",
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
    elif args.scenario == "task-type":
        payload = task_type_payload(context)
    elif args.scenario == "lab-analysis":
        payload = lab_analysis_payload(context)
    elif args.scenario == "poster-plan":
        payload = poster_plan_payload(context)
    elif args.scenario == "presentation-plan":
        payload = presentation_plan_payload(context)
    elif args.scenario == "website-plan":
        payload = website_plan_payload(context)
    elif args.scenario == "figure-plan":
        payload = figure_plan_payload(context)
    elif args.scenario == "figure-legend":
        payload = figure_legend_payload(context)
    elif args.scenario == "section-review":
        payload = section_review_payload(context)
    elif args.scenario == "critical-analysis":
        payload = critical_analysis_payload(context)
    elif args.scenario == "planning-approval":
        payload = planning_approval_payload(context)
    else:
        payload = writing_gate_payload(context)
    json.dump(payload, sys.stdout, ensure_ascii=True, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
