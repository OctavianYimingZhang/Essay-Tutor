---
name: coursework-killer-intake-planning
description: Academic coursework intake and planning workflow for CourseWork Killer. Use when the user asks to plan an assessed essay or coursework task, interpret a brief or rubric, diagnose task type, ask required plan-changing questions, lock an assignment brief, create section-by-section plans, or build a CriticalAnalysisPlan before drafting.
---

# CourseWork Killer Intake Planning

Use this focused skill to turn an academic request into a locked brief and a decision-complete plan.

## Shared Resource Rule

Read shared resources from the first existing CourseWork Killer root:

- packaged path: `../../`
- local copied-skill path: `../coursework-killer/`
- default local path: `~/.codex/skills/coursework-killer/`

Load only the listed references unless the task needs another focused skill.

## Workflow

1. Read `references/intake-and-planning.md`.
2. Inspect supplied briefs, rubrics, drafts, examples, data, screenshots, and style guides before asking questions.
3. Build the internal `AssignmentBrief`, including task type, output form, source base, citation quantity, format requirements, task-specific open items, and DOCX title font size when relevant.
4. In Plan Mode, display the brief or decision context, generate the relevant payload with `scripts/build_intake_questions.py`, and call `request_user_input`.
5. Do not create a StructurePlan while unresolved plan-changing items remain.
6. Keep requirement/rubric/brief locking, Ask User, user preference confirmation, Planning Approval, and writing gate decisions with the main agent.
7. Do not start subagents until the brief is locked; use them only for non-interactive bounded work whose dependencies are satisfied.
8. Present paragraph-level SectionPlans when the task has prose sections, then present the CriticalAnalysisPlan when evaluative writing is needed.
9. Produce the final integrated plan only after the brief, section decisions, and critical moves are resolved.
10. Run `scripts/build_intake_questions.py planning-approval` after the final integrated plan is visible; approval leads directly to writing without a redundant start-writing question.

Use the root `coursework-killer` skill only for routing or system-wide maintenance context.
