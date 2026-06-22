---
name: coursework-killer
description: Index and router for the CourseWork Killer multiple-skill academic coursework system covering intake and planning, research and citation, drafting and revision, critical analysis, lab reports and data, figures and legends, posters and presentations, interactive websites, DOCX formatting, and final QA. Use when the user asks broadly for CourseWork Killer, needs assessed academic writing or coursework support, or needs multiple focused CourseWork Killer skills coordinated.
---

# CourseWork Killer

Use this Skill as the Index for the CourseWork Killer multiple-skill system. Route broad or mixed academic-writing requests to the right focused skill, then use the shared tutoring workflow:

```text
intake -> material diagnosis -> requirement/rubric/brief gate -> Asking Questions -> locked brief -> optional non-interactive subagents -> evidence/comparison map -> structure plan -> Planning Approval -> writing -> QA/revision -> output
```

Keep the workflow light. Read only the reference files that match the current task, and use the user's assignment material as the main source of truth.

Plan Mode is required for the native Asking Questions flow because `request_user_input` is a Plan Mode tool. A Skill cannot switch Codex collaboration mode by itself; when Plan Mode is active, use the script-backed payload workflow below to call `request_user_input` directly.

## Multiple Skill System

Treat `coursework-killer` as the router. If a request clearly maps to one focused workflow, read and follow that focused skill before continuing. If a request spans multiple workflows, sequence the focused skills in the order that locks requirements first and validates output last.

Requirement, rubric, brief locking, Ask User, Planning Approval, writing gate decisions, and user preference confirmation stay with the main agent. Use subagents only after the brief is locked and only for non-interactive bounded tasks whose dependencies are satisfied.

Focused skills:

- `coursework-killer-intake-planning`: brief reconstruction, task-type diagnosis, Asking Questions, locked brief, section plans, and CriticalAnalysisPlan.
- `coursework-killer-research-citation`: source discovery, evidence maps, claim-level citation support, citation quantity, and references.
- `coursework-killer-draft-revise`: drafting, rewriting, user-draft comparison, prose quality, paragraph logic, and revision boundaries.
- `coursework-killer-critical-analysis`: evaluative stance, critical moves, limitations, synthesis, and Discussion-level critique.
- `coursework-killer-lab-data`: lab reports, data-supported coursework, analysis tools, statistical methods, Results, figures, and tables.
- `coursework-killer-figures-legends`: source-backed figure specifications, figure generation plans, captions, and submit-ready legends.
- `coursework-killer-posters-presentations`: academic posters, slide decks, storyboards, message hierarchy, speaker notes, and visual planning.
- `coursework-killer-website-coursework`: interactive academic websites, user journeys, interaction models, and content architecture.
- `coursework-killer-docx-formatting`: Word/DOCX formatting, document style, title size, layout, references, and visual inspection.
- `coursework-killer-final-qa`: final requirement fit, citations, structure, data, visuals, formatting, and delivery checks.

Shared resources live in this root package. When maintaining the local installation, run `python3 scripts/install_multiple_skills.py` to copy the focused skill folders into the top-level Codex skills directory so they appear as separate skill chips.

## Core Principles

- Work as a tutor, not a silent ghostwriter: diagnose, ask, explain the writing choices that matter, and draft only after the user has confirmed the direction.
- Start academic writing tasks by reconstructing and confirming the assignment brief with the user before planning.
- Make the first user-facing output for any new or unclear writing request a displayed brief or decision plan followed by a Codex Asking Questions decision batch generated from the intake payload script.
- Create a structure plan only after all plan-changing requirements are verified from materials or explicitly selected by the user, including task type, citation quantity, format requirements, analysis tool and method for lab reports, visual or interaction requirements for non-essay outputs, figure legend requirements, and DOCX title font size when formatted output is requested.
- Do not start evidence, planning, writing, data, citation, visual, or QA subagents before the requirement/rubric/brief gate is complete and the brief is locked.
- Build a requirement model from the prompt, rubric, brief, course material, examples, and user preferences before planning detailed prose. Keep that model internal unless the user explicitly asks to see it.
- Default to the strongest academic standard the brief can support. Ask about course-stage requirements only when they change marking criteria, genre conventions, permissible evidence, or writing identity.
- Use verified evidence before drafting substantive claims, statistics, methods, citations, lecturer expectations, or source metadata.
- Keep asking with Codex Asking Questions, including during planning, until task type, thesis direction, evidence burden, citation quantity, format requirements, lab-report analysis tool and method, poster or presentation story decisions, website interaction constraints, figure generation requirements, figure legend requirements, title font size for DOCX output, structure choice, critical-analysis stance, revision boundaries, and output expectations are clear. Before every Asking Questions call, show the relevant plan or decision context in chat. In Plan Mode, generate the intake payload with `python3 scripts/build_intake_questions.py task-type`, `python3 scripts/build_intake_questions.py sparse`, or `python3 scripts/build_intake_questions.py complete`, then call `request_user_input` with the emitted JSON object.
- Choose output density by rubric emphasis, concept difficulty, evidence volume, analysis needed, reader context, and available assignment space.
- When an assignment gives an upper page or word limit, use available space for evidence, explanation, comparison, and critical interpretation until the argument is appropriately developed near the limit.
- Treat user-supplied exemplars, teacher examples, sample answers, model essays, feedback examples, and visual examples as transferable structure, density, paragraph-function, citation-density, and tone evidence. Treat topic-specific claims from those examples as leads that need support from the current assignment material, user data, course material, or verified sources before they enter the final work.
- Use the default essay architecture for essay tasks: Abstract, Introduction, Main Body with named subsections, Discussion, Conclusion, and References when sources are used.
- Use task-specific workflows for lab reports, posters, presentations, interactive websites, figure generation, and figure legends instead of forcing essay architecture onto non-essay assignments.
- Match figures, tables, and data presentation to the work they do for the argument: comparison, mechanism, method clarity, evidence synthesis, or result interpretation.
- Keep claims, evidence, interpretation, boundaries, and links back to the question close together.
- Create Word/DOCX files when the user asks for a file, Word output, or formatted document.
- For academic DOCX outputs, keep body content assignment-facing and use black text and headings unless the assignment material gives a different style rule.
- Keep final Skill repository content in English.

## Workflow

1. **Intake and material diagnosis**
   - Read `references/intake-and-planning.md`.
   - Build an internal `AssignmentBrief` that records task type, title or question, academic context, output form, citation style, source base, rubric or marking evidence, language, target quality, submission mode, analysis tool, analysis method, visual requirements, interaction requirements, figure legend requirements, title font size for DOCX output, and useful constraints.
   - Inspect supplied files, teacher material, user-supplied exemplars, sample answers, model essays, feedback examples, screenshots, visual examples, rubrics, generated drafts, and user drafts before asking questions.
   - Mark each requirement internally as verified from materials, user-confirmed, inferred from context, user preference needed, or evidence gap.
   - In Plan Mode, show the brief or decision context, generate a `request_user_input` payload with `scripts/build_intake_questions.py`, and call `request_user_input` to resolve plan-changing preferences, task type, citation quantity, format requirements, lab-report analysis tool and method, poster/presentation/website/figure/legend requirements, title font size for DOCX output, inferences, and evidence gaps before planning.
   - If a user draft and a generated result are both supplied, compare them before planning revision.

2. **Evidence and comparison map**
   - Read `references/research-and-citation.md`.
   - Prioritise the locked assignment brief, rubric, official course material, required readings, user files, authoritative academic sources, and verified external literature.
   - Build a sentence-level claim-to-source map before drafting claim-heavy sections.
   - For comparison tasks, map argument depth, body length, source range, claim-level citation density, paragraph role, critical stance, discussion quality, user-draft strengths to preserve, generated-result weaknesses, and visual DOCX format problems.

3. **Structure plan**
   - Create a structure plan only after the assignment brief is locked.
   - Use `references/intake-and-planning.md` to create detailed section-by-section plans that explain each section's role in the argument, paragraph output path, proof logic, citation-density target, critical-analysis placement, order, and fit with the user's confirmed goal.
   - For essay tasks, plan Abstract, Introduction, Main Body subsections, Discussion, Conclusion, and References when sources are used.
   - For lab reports, posters, presentations, interactive websites, figure generation, and figure legends, use the task-specific workflows in `references/intake-and-planning.md` and only use essay sections when the brief requires them.
   - Present each section plan as paragraph-level choices using real labels such as `Abstract`, `Introduction`, `Main Body Paragraph 1: ...`, `Discussion Paragraph 1: ...`, and `Conclusion`; use task-specific options that reflect real tradeoffs in the displayed plan.
   - Present the CriticalAnalysisPlan after the paragraph plan has been discussed; when planning Discussion, reserve space for synthesis and critical analysis so later critical moves have a natural insertion point.
   - In Codex Plan Mode, use the required `<proposed_plan>` block for the final plan when active mode requires it; outside Plan Mode, use the same plan structure in normal chat.
   - Run Planning Approval with `scripts/build_intake_questions.py planning-approval` after the final integrated plan is visible.
   - Draft from the approved plan immediately; do not ask a redundant start-writing question.

4. **Drafting and revision**
   - Read `references/drafting-and-critical-analysis.md`.
   - Read `references/critical-writing-bank.md` when the task needs stronger critical stance, discussion, evaluation of studies, method limits, theory limits, or constructive suggestions.
   - Draft from the structure plan and evidence map.
   - If a plan-breaking issue appears after approval, keep the decision with the main agent and use `scripts/build_intake_questions.py writing-gate` when user input is required.
   - Use revision passes to improve paragraph function, evidence fit, interpretation, scope, citation prose, and reader flow.

5. **Figures, tables, and data**
   - Read `references/visuals-tables-data.md` when the task includes figures, tables, raw data, statistical outputs, spreadsheets, GraphPad Prism, R Studio, Python, MatLab, figure generation, figure legends, poster visuals, presentation visuals, interactive website media, or visual explanation.
   - Use the authoritative analysis output supplied or generated for the task, and preserve analysis tool, analysis method, sample sizes, statistics, units, labels, and uncertainty measures.
   - Do not infer tests, models, or figure legend details; ask the user or mark them unresolved when the brief or supplied output does not verify them.

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
- `references/visuals-tables-data.md`: figure, table, data, analysis-tool, figure-generation, figure-legend, caption, and result-presentation decisions.
- `references/docx-output.md`: Word/DOCX formatting and output contract.
- `references/subagents.md`: optional bounded roles for evidence extraction, structure review, citation checking, data/visual checking, and final QA.
- `references/qa-and-validation.md`: final checks for plans, drafts, citations, visuals, data, DOCX files, and package health.

## Maintenance

Run these checks before committing or publishing changes:

```bash
python3 scripts/install_multiple_skills.py --check
python3 scripts/skill_maintenance.py doctor
python3 scripts/validate_coursework_killer.py --strict
```

Use optional integrations such as citation-management tools, GraphPad Prism, R Studio, Python, MatLab, spreadsheet tools, BioRender, image generation, presentation tools, website-building tools, or document tools through their own Skills or local applications. Keep third-party code outside this Skill unless the licence supports bundling.
