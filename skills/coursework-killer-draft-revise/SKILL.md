---
name: coursework-killer-draft-revise
description: Academic drafting and revision workflow for CourseWork Killer. Use when the user asks to draft, rewrite, improve, compare, condense, expand, or revise essay prose, lab-report prose, literature review sections, proposals, case studies, discussion sections, poster text, slide notes, website copy, or other assessed academic writing from a confirmed plan.
---

# CourseWork Killer Draft Revise

Use this focused skill to draft or revise academic prose from a confirmed plan and evidence map.

## Shared Resource Rule

Read shared resources from the first existing CourseWork Killer root:

- packaged path: `../../`
- local copied-skill path: `../coursework-killer/`
- default local path: `~/.codex/skills/coursework-killer/`

## Workflow

1. If there is no confirmed plan, route through `coursework-killer-intake-planning` first.
2. Read `references/drafting-and-critical-analysis.md`.
3. Read `references/research-and-citation.md` when substantive claims, citations, or source-backed corrections are needed.
4. Compare user drafts and generated drafts before planning revision when both are supplied.
5. Preserve confirmed requirements: task type, source base, citation quantity, format requirements, paragraph-level SectionPlan decisions, and selected critical moves.
6. After Planning Approval, draft directly from the approved plan without a redundant start-writing question.
7. Use section-drafting subagents only after each section contract is locked; do not let subagents change thesis, structure, citation strategy, format contract, or method decisions.
8. For lab reports, Results and Discussion drafting must wait for verified data-analysis output.
9. If a plan-breaking issue appears after approval, return it to the main agent and use `scripts/build_intake_questions.py writing-gate` only when user input is required.
10. Draft with claim, evidence, interpretation, boundary, and link-back close together.
11. For posters, presentations, websites, figures, and legends, draft task-specific text blocks instead of forcing essay paragraphs.
12. Read `references/qa-and-validation.md` for the final draft check.

Do not draft around unresolved plan-changing requirements.
