---
name: coursework-killer-figures-legends
description: Figure and figure legend workflow for CourseWork Killer. Use when the user asks to create, specify, revise, caption, cite, or validate academic figures, BioRender-style schematics, generated visuals, data figures, figure panels, scale labels, source notes, permissions, or submit-ready figure legends.
---

# CourseWork Killer Figures Legends

Use this focused skill to create evidence-bound figure plans and legends.

## Shared Resource Rule

Read shared resources from the first existing CourseWork Killer root:

- packaged path: `../../`
- local copied-skill path: `../coursework-killer/`
- default local path: `~/.codex/skills/coursework-killer/`

## Workflow

1. Read `references/visuals-tables-data.md`.
2. Read `references/research-and-citation.md` when figure claims, mechanisms, source notes, or permissions depend on literature or external material.
3. If figure purpose, source basis, or tool is unresolved, use `python3 scripts/build_intake_questions.py figure-plan`.
4. If legend depth, statistical detail, or source note is unresolved, use `python3 scripts/build_intake_questions.py figure-legend`.
5. Build a `FigureGenerationSpec` or `FigureLegendSpec` before creating final figure text or instructions.
6. Include only verified labels, units, scale bars, abbreviations, sample sizes, statistics, error bars, source status, and permission notes.
7. Read `references/qa-and-validation.md` before final delivery.

Do not invent figure details to make a legend look complete.
