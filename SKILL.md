---
name: essay-tutor
description: Academic writing workflow for planning, researching, drafting, revising, citing, formatting, and quality-checking essays, lab reports, literature reviews, case studies, proposals, discussion sections, data-supported reports, and Word/DOCX academic documents. Use when the user asks Codex to produce or improve assessed academic writing, align writing to a rubric or exemplar, manage citations, handle figures/tables/data, or create a formatted academic document.
---

# Essay Tutor

Use this Skill to turn academic-writing requests into an interaction-led tutoring workflow:

```text
intake -> material diagnosis -> Asking Questions -> locked brief -> evidence/comparison map -> structure plan -> user confirmation -> draft/revision -> visual + citation QA -> output
```

Keep the workflow light. Read only the reference files that match the current task, and use the user's assignment material as the main source of truth.

## Core Principles

- Work as a tutor, not a silent ghostwriter: diagnose, ask, explain the writing choices that matter, and draft only after the user has confirmed the direction.
- Start academic writing tasks by reconstructing and confirming the assignment brief with the user before planning.
- Make the first user-facing output for any new or unclear writing request a focused requirements check, not a structure plan.
- Create a structure plan only after all plan-changing requirements are verified from materials or explicitly selected by the user.
- Build a requirement model from the prompt, rubric, brief, course material, examples, and user preferences before planning detailed prose.
- Default to the strongest academic standard the brief can support. Ask about course-stage requirements only when they change marking criteria, genre conventions, permissible evidence, or writing identity.
- Use verified evidence before drafting substantive claims, statistics, methods, citations, lecturer expectations, or source metadata.
- Keep asking with Codex Asking Questions, including during planning, until thesis direction, evidence burden, structure choice, revision boundaries, and output expectations are clear.
- Choose output density by rubric emphasis, concept difficulty, evidence volume, analysis needed, reader context, and available assignment space.
- When an assignment gives an upper page or word limit, use available space for evidence, explanation, comparison, and critical interpretation until the argument is appropriately developed near the limit.
- Treat exemplars and teacher feedback as transferable structure, density, and tone evidence; use topic claims from them only when independently supported by the assignment material or sources.
- Use the default essay architecture for essay tasks: Abstract, Introduction, Main Body with named subsections, Discussion, Conclusion, and References when sources are used.
- Match figures, tables, and data presentation to the work they do for the argument: comparison, mechanism, method clarity, evidence synthesis, or result interpretation.
- Keep claims, evidence, interpretation, boundaries, and links back to the question close together.
- Create Word/DOCX files when the user asks for a file, Word output, or formatted document.
- For academic DOCX outputs, keep body content assignment-facing and use black text and headings unless the assignment material gives a different style rule.
- Keep final Skill repository content in English.

## Workflow

1. **Intake and material diagnosis**
   - Read `references/intake-and-planning.md`.
   - Build an `AssignmentBrief` that records task type, title or question, academic context, output form, citation style, source base, rubric or marking evidence, language, target quality, and useful constraints.
   - Inspect supplied files, teacher material, exemplars, screenshots, visual examples, rubrics, generated drafts, and user drafts before asking questions.
   - Mark each requirement as verified from materials, user-confirmed, inferred from context, user preference needed, or evidence gap.
   - Use Codex Asking Questions, including `request_user_input` when available, to resolve every plan-changing preference, inference, and evidence gap before planning; do not replace this with a static question dump.
   - If a user draft and a generated result are both supplied, compare them before planning revision.

2. **Evidence and comparison map**
   - Read `references/research-and-citation.md`.
   - Prioritise the locked assignment brief, rubric, official course material, required readings, user files, authoritative academic sources, and verified external literature.
   - Build a sentence-level claim-to-source map before drafting claim-heavy sections.
   - For comparison tasks, map argument depth, body length, source range, claim-level citation density, paragraph role, critical stance, discussion quality, user-draft strengths to preserve, generated-result weaknesses, and visual DOCX format problems.

3. **Structure plan**
   - Create a structure plan only after the assignment brief is locked.
   - Use `references/intake-and-planning.md` to create a natural section plan that explains each section's role in the argument, the evidence it needs, the reason for the chosen order, and how it serves the user's confirmed goal.
   - For essay tasks, plan Abstract, Introduction, Main Body subsections, Discussion, Conclusion, and References when sources are used.
   - Present the plan for user double-check. In Codex Plan Mode, use the required `<proposed_plan>` block; outside Plan Mode, use the same plan structure in normal chat.
   - Draft from the confirmed plan.

4. **Drafting and revision**
   - Read `references/drafting-and-critical-analysis.md`.
   - Read `references/critical-writing-bank.md` when the task needs stronger critical stance, discussion, evaluation of studies, method limits, theory limits, or constructive suggestions.
   - Draft from the structure plan and evidence map.
   - Use revision passes to improve paragraph function, evidence fit, interpretation, scope, citation prose, and reader flow.

5. **Figures, tables, and data**
   - Read `references/visuals-tables-data.md` when the task includes figures, tables, raw data, statistical outputs, spreadsheets, GraphPad Prism files, or visual explanation.
   - Use the authoritative analysis output supplied or generated for the task, and preserve sample sizes, statistics, units, labels, and uncertainty measures.

6. **DOCX output**
   - Read `references/docx-output.md` when the user requests Word, DOCX, PDF-from-DOCX, or formatted file output.
   - Apply the requested style guide and the default academic document formatting in that reference when no conflicting course rule is present.
   - Render DOCX outputs to page images and visually inspect format before delivery when rendering tools are available.

7. **Validation**
   - Read `references/qa-and-validation.md`.
   - Check requirement fit, evidence support, citation consistency, structure, density, visual/table usefulness, data accuracy, and output formatting before delivery.

## Reference Map

- `references/intake-and-planning.md`: requirement modelling, readiness states, density planning, structure planning, and approval flow.
- `references/research-and-citation.md`: source selection, evidence mapping, citation placement, metadata checks, and reference-list handling.
- `references/drafting-and-critical-analysis.md`: paragraph logic, academic tone, critical analysis, revision, and language control.
- `references/critical-writing-bank.md`: reusable critical-writing sentence patterns and evaluative moves to adapt into topic-specific prose.
- `references/visuals-tables-data.md`: figure, table, data, GraphPad-style analysis, captions, and result-presentation decisions.
- `references/docx-output.md`: Word/DOCX formatting and output contract.
- `references/subagents.md`: optional bounded roles for evidence extraction, structure review, citation checking, data/visual checking, and final QA.
- `references/qa-and-validation.md`: final checks for plans, drafts, citations, visuals, data, DOCX files, and package health.

## Maintenance

Run these checks before committing or publishing changes:

```bash
python3 scripts/skill_maintenance.py doctor
python3 scripts/validate_essay_tutor.py --strict
```

Use optional integrations such as citation-management tools, GraphPad Prism, BioRender, image generation, spreadsheet tools, or document tools through their own Skills or local applications. Keep third-party code outside this Skill unless the licence supports bundling.
