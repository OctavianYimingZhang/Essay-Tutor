---
name: essay-tutor-lab-data
description: Lab report and data-supported coursework workflow for Essay Tutor. Use when the user asks for lab reports, Results sections, statistical reporting, data analysis planning, GraphPad Prism, R Studio, Python, MatLab, spreadsheets, figures, tables, uncertainty, sample sizes, p values, or method-linked result interpretation.
---

# Essay Tutor Lab Data

Use this focused skill for lab reports and data-supported academic writing.

## Shared Resource Rule

Read shared resources from the first existing Essay Tutor root:

- packaged path: `../../`
- local copied-skill path: `../essay-tutor/`
- default local path: `~/.codex/skills/essay-tutor/`

## Workflow

1. Read `references/intake-and-planning.md` and `references/visuals-tables-data.md`.
2. If the analysis tool, method, or scope is unresolved, display the decision context, run `python3 scripts/build_intake_questions.py lab-analysis`, and ask the user in Plan Mode.
3. Use supplied analysis output, scripts, notebooks, exported tables, Prism files, spreadsheets, or course instructions as the authoritative source.
4. Do not infer a statistical test, model, post hoc correction, repeated-measures structure, sample size, exclusion, or p value from topic wording alone.
5. Preserve analysis tool, analysis method, sample basis, exclusions, tests, estimates, units, uncertainty, and figure/table destinations exactly as supported.
6. Read `references/drafting-and-critical-analysis.md` before writing Results, Discussion, or figure-linked prose.
7. Read `references/qa-and-validation.md` before final delivery.

Mark unverified statistics or method choices as open items instead of writing them as facts.
