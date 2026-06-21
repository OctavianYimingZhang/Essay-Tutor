---
name: essay-tutor-intake-planning
description: Academic coursework intake and planning workflow for Essay Tutor. Use when the user asks to plan an assessed essay or coursework task, interpret a brief or rubric, diagnose task type, ask required plan-changing questions, lock an assignment brief, create section-by-section plans, or build a CriticalAnalysisPlan before drafting.
---

# Essay Tutor Intake Planning

Use this focused skill to turn an academic request into a locked brief and a decision-complete plan.

## Shared Resource Rule

Read shared resources from the first existing Essay Tutor root:

- packaged path: `../../`
- local copied-skill path: `../essay-tutor/`
- default local path: `~/.codex/skills/essay-tutor/`

Load only the listed references unless the task needs another focused skill.

## Workflow

1. Read `references/intake-and-planning.md`.
2. Inspect supplied briefs, rubrics, drafts, examples, data, screenshots, and style guides before asking questions.
3. Build the internal `AssignmentBrief`, including task type, output form, source base, citation quantity, format requirements, task-specific open items, and DOCX title font size when relevant.
4. In Plan Mode, display the brief or decision context, generate the relevant payload with `scripts/build_intake_questions.py`, and call `request_user_input`.
5. Do not create a StructurePlan while unresolved plan-changing items remain.
6. Present paragraph-level SectionPlans when the task has prose sections, then present the CriticalAnalysisPlan when evaluative writing is needed.
7. Produce the final integrated plan only after the brief, section decisions, and critical moves are resolved.

Use the root `essay-tutor` skill only for routing or system-wide maintenance context.
