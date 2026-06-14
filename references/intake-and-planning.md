# Intake And Planning

Use this reference when starting an essay task, diagnosing missing information, or generating a detailed plan.

## Intake Fields

Collect the minimum information needed for the current step.

Required when available:

| Field | What to capture | Why it matters |
| --- | --- | --- |
| Essay topic or exact question | Exact wording, whether the title can be changed, and whether it is an assessed prompt | Defines scope and command verb |
| Word limit | Upper limit, lower limit, tolerance, and whether title, references, captions, figures, and tables count | Controls density and section budget |
| Academic level | High school, undergraduate, master's, doctoral, professional, or journal level | Sets depth and citation density |
| Course/module/faculty | Official course context and learning outcomes | Prevents off-scope research drift |
| Required format | Chat draft, Markdown, DOCX, PDF, headings, abstract, numbered sections, figures, tables | Controls output shape |
| Citation style | APA 7, Harvard, Vancouver, AMA, IEEE, Chicago, MLA, journal style, or university style | Controls in-text and reference format |
| Source base | Lecture slides, notes, reading list, required papers, uploaded papers, textbooks, datasets | Sets evidence hierarchy |
| Rubric | Marking criteria, learning outcomes, feedback, grade descriptors | Sets examiner fit |
| Deadline/stage | Planning only, first draft, revision, final polish, file generation | Controls workflow depth |
| Language | Final language and whether notes can be bilingual | Controls prose output |

Strongly recommended:

| Field | Use |
| --- | --- |
| Target grade or standard | Calibrate depth, originality, and QA threshold |
| Required source count/type | Enforce primary papers, reviews, textbooks, guidelines, or recent papers |
| Recency rule | Include recent literature without deleting classic evidence |
| User's intended argument | Improve thesis alignment |
| Forbidden sources/content | Avoid prohibited sources or theories |
| Figure/table/data needs | Route to visual or data workflow |
| Previous feedback | Correct recurring weaknesses |
| Preferred essay examples | Extract transferable style rules only, not factual claims |

## Ask User Tool Gate

Detailed planning requires confirmed requirements. Do not guess, default, preselect, or predict missing essay requirements before the plan.

Use native `request_user_input` / ask-user UI for material user decisions when that capability is available. If it is unavailable, ask the same questions in normal chat and keep them concise.

Ask one to three concise questions per turn when any required field is missing, ambiguous, contradictory, or not directly verifiable from the prompt, uploaded files, official course material, or local files. Use concrete options when useful, but do not choose on the user's behalf.

Ask-user turns should:

- contain only decisions that affect the essay plan, evidence strategy, citation style, or final format;
- offer meaningful mutually exclusive choices when the answer can be structured;
- put the recommended option first only when the academic or workflow rationale is clear;
- include a one-sentence explanation of why the decision matters;
- avoid long plain-text questionnaires when ask-user UI is available.

Use ask-user for these requirement decisions when they are not already verified:

- academic level;
- final language;
- output form, including chat draft, Markdown, DOCX, PDF, headings, figures, tables, or appendices;
- word or page limit and whether title, reference list, captions, figures, and tables count;
- citation style and local style guide;
- source base, including lecture slides, required readings, uploaded files, textbooks, or external literature;
- rubric, marking standard, learning outcomes, and target grade;
- reference-list inclusion and minimum or maximum source count;
- figure, table, data, or appendix expectations.

Before planning, classify every missing or unclear item as:

```yaml
UserDecisionNeeded:
  field:
  question_to_user:
  why_it_matters:
  acceptable_answers:
  source_checked:
```

Examples:

- Missing citation style: ask the user which style or course guide to follow before planning citation strategy.
- Missing academic level: ask the user whether the essay is high school, undergraduate, master's, doctoral, professional, or journal level before calibrating depth.
- Missing word or page limit: ask for the limit and what counts toward it before planning section density.
- Missing rubric or marking standard: ask whether the user has one. If the user confirms none exists, record `confirmed_none` and continue.

Only verified facts may enter `confirmed_requirements`. A requirement is verified when it is stated by the user or present in reliable source material inspected for this task.

## EssaySkillConfig

Create or conceptually maintain:

```yaml
EssaySkillConfig:
  essay_question:
  topic:
  command_verb:
  academic_level:
  course_context:
  word_limit:
    minimum:
    maximum:
    tolerance:
    included_items:
  format:
  citation_style:
  source_base:
  rubric:
  required_sources:
  forbidden_sources:
  figure_table_data_needs:
  target_standard:
  language:
  output_requested:
```

## InputReadinessReport

Before planning or drafting, produce internally or visibly when useful:

```yaml
InputReadinessReport:
  ready_for:
    - research
    - detailed_plan
    - draft
    - docx
  confirmed_requirements:
  open_user_decisions:
  evidence_available:
  evidence_missing:
  next_action:
```

Readiness rules:

- `ready_for.detailed_plan` is false while `open_user_decisions` is non-empty.
- `ready_for.research` may be true before all user decisions are complete only for source discovery that does not depend on unresolved requirements.
- `ready_for.draft` is false until the plan is approved.
- `ready_for.docx` is false until file output and formatting requirements are confirmed.

## Tutor Planning Loop

After intake and source discovery, co-design the plan before presenting it as final.

The loop is:

```text
Summarize confirmed requirements
-> Explain the next planning choice and why it matters
-> Ask the user to choose or confirm
-> Update the working plan state
-> Repeat until the plan is decision-complete
-> Present the final plan for approval
```

Use this loop for high-impact planning decisions such as:

- thesis direction or argumentative stance;
- scope boundary and excluded material;
- section architecture and order;
- level of mechanism detail versus critical discussion;
- source strategy, including classic papers, recent papers, official course material, or reviews;
- figure, table, and data inclusion;
- target standard, density, and risk tolerance for ambitious analysis.

Tutor-style planning rules:

- Teach the tradeoff before asking. Example: explain that a mechanism-heavy plan may score well for technical depth but can crowd out critical evaluation in a short essay.
- Ask targeted decisions instead of dumping a complete plan for passive approval.
- Keep a concise working-plan summary after important decisions so the user can correct direction early.
- Do not emit the formal detailed plan while major plan preferences are unresolved.
- Do not use ask-user for cosmetic preferences that will not change the essay plan.

Plan Mode handling:

- If native Codex Plan Mode is active, follow its rules for conversational planning and produce the final decision-complete essay plan inside a `<proposed_plan>` block.
- If Plan Mode is not active, run the same tutor loop in normal chat and label the final plan clearly before requesting approval.
- Never state or imply that this Skill can switch Codex into Plan Mode by itself.

## DeepResearch Before Plan

Before a detailed plan, perform enough source work to avoid generic structure:

```text
Topic Deconstruction
-> Key Concepts
-> Competing Models or Mechanisms
-> Seminal Papers
-> Recent Evidence
-> Methodological Limits
-> Clinical, Translational, or Theoretical Implications
-> Critical Debates
-> Figure/Table Opportunities
-> Citation Map
```

Do not turn orientation sources into final evidence. Verify paper metadata and claim relevance before adding citations to the plan.

## Plan Depth Standard

A valid plan must go below heading level. The main body must specify subtitles and what each subtitle will argue.

Minimum plan shape:

```yaml
EssayPlan:
  confirmed_requirements:
    essay_question:
    academic_level:
    word_or_page_limit:
    citation_style:
    output_format:
    final_language:
    source_base:
    rubric_or_marking_standard:
  open_user_decisions: []
  essay_question:
  interpreted_scope:
  working_thesis:
  word_limit_strategy:
  proposed_title:
  section_plan:
    introduction:
      function:
      content_sequence:
      key_terms_to_define:
      thesis_move:
    main_body:
      - heading:
        section_function:
        subheadings:
          - subtitle:
            specific_content:
            key_claim:
            evidence_needed:
            analytic_angle:
            possible_citations:
        transition_to_next_section:
    discussion:
      synthesis_paragraph:
      limitations_paragraph:
      future_direction_paragraph:
    conclusion:
      final_answer:
      no_new_evidence_rule:
  citation_strategy:
    intensive_reading_citations:
    broad_support_citations:
    classic_papers:
    recent_papers:
  figure_table_strategy:
    figures:
    tables:
    data_analysis:
  critical_thinking_strategy:
    main_body_analytic_targets:
    discussion_analytic_targets:
```

Do not output a formal detailed plan if `open_user_decisions` contains any item. Ask the next required user question instead.

## Section Logic

Introduction:

- define only terms needed for the question;
- establish why the topic matters;
- set the scope boundary;
- state the thesis;
- preview organising logic, not a list of every later subsection.

Main body:

- divide the argument into subtitles and, when needed, sub-subtitles;
- assign each subsection a claim, evidence need, and analytic function;
- prevent mechanism catalogues by explaining what each mechanism proves or distinguishes.

Discussion:

- first paragraph synthesises the main body without repeating it as a list;
- second paragraph evaluates limitations, evidence strength, uncertainty, methods, translation, or model boundaries;
- third paragraph gives future direction or unresolved questions when appropriate.

Conclusion:

- answer the question directly;
- synthesise the thesis;
- add no new evidence.

## Approval Loop

Workflow:

```text
Generate Plan v0.1
-> User modifies
-> Generate Plan v0.2 with change log
-> User modifies again
-> Repeat until user approves
-> Draft from approved plan
```

Rules:

- Do not draft the final essay before approval unless the user explicitly requests it.
- Revise only the requested parts unless a requested change creates a dependency elsewhere.
- Preserve stable approved components.
- Keep thesis, section hierarchy, paragraph logic, citation strategy, critical-thinking points, and visual/data strategy visible in each major plan revision.
- Treat "Approve Plan", "approved", "go ahead", or equivalent wording as the drafting trigger.
