---
name: coursework-killer-final-qa
description: Final academic quality-assurance workflow for CourseWork Killer. Use when the user asks to check, audit, validate, compare, mark up, or quality-control an essay, lab report, poster, presentation, website, figure, figure legend, citation list, DOCX file, or academic coursework package before submission.
---

# CourseWork Killer Final QA

Use this focused skill to verify academic work before delivery or submission.

## Shared Resource Rule

Read shared resources from the first existing CourseWork Killer root:

- packaged path: `../../`
- local copied-skill path: `../coursework-killer/`
- default local path: `~/.codex/skills/coursework-killer/`

## Workflow

1. Read `references/qa-and-validation.md`.
2. Read task-specific references only as needed: intake and planning, research and citation, drafting and critical analysis, visuals/tables/data, or DOCX output.
3. Check requirement fit, task type, locked brief, citation quantity, format requirements, source support, critical-analysis placement, section or task-specific structure, visual/data accuracy, and output formatting.
4. Check that subagents, if used, started only after the brief was locked and respected dependency order.
5. For lab reports, verify that Results and Discussion were written after the data-analysis output they depend on.
6. For drafts, lead with concrete issues and file or section references when available.
7. For citations, check support, metadata, style consistency, and reference-list alignment.
8. For data and visuals, verify analysis tool, method, sample basis, statistics, figure legends, labels, units, source notes, and permissions.
9. For DOCX outputs, inspect rendered pages when possible.

Do not rewrite the work unless the user asks for revision after the QA findings.
