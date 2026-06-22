---
name: coursework-killer-docx-formatting
description: Academic Word and DOCX formatting workflow for CourseWork Killer. Use when the user asks to create, edit, format, inspect, or export Word documents, DOCX files, PDF-from-DOCX outputs, title style, Arial formatting, margins, line spacing, justified body text, references, tables, or submit-ready academic document layout.
---

# CourseWork Killer DOCX Formatting

Use this focused skill for Word/DOCX academic document output and inspection.

## Shared Resource Rule

Read shared resources from the first existing CourseWork Killer root:

- packaged path: `../../`
- local copied-skill path: `../coursework-killer/`
- default local path: `~/.codex/skills/coursework-killer/`

## Workflow

1. Read `references/docx-output.md`.
2. Read `references/intake-and-planning.md` if output form, format requirements, or title font size is unresolved.
3. In Plan Mode, use `python3 scripts/build_intake_questions.py docx-format` or `python3 scripts/build_intake_questions.py document-format` before applying uncertain formatting choices.
4. Default essay-style Word documents to Arial, 2.5 cm margins, justified body text, left-aligned subheadings, centred main titles, 1.5 line spacing, and otherwise default settings unless the brief or user specifies another rule.
5. Preserve academic black text and assignment-facing content unless the supplied style guide requires another design.
6. Render DOCX outputs to page images and inspect layout when tools are available.
7. Read `references/qa-and-validation.md` before delivery.

Do not silently change academic content while performing formatting-only work.
