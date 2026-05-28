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
| AI-use policy | Whether AI-assisted drafting is permitted and whether process disclosure is needed | Prevents academic-integrity conflicts |

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

## Blocking Question Rule

Ask one concise clarification question only when the missing field blocks the next useful output.

Continue without asking when a conservative assumption is possible. Label the item:

```yaml
Assumption:
  field:
  assumed_value:
  reason:
  risk_if_wrong:
OpenRequirement:
  field:
  why_it_matters:
  when_to_resolve:
```

Examples:

- Missing exact citation style does not block planning; use "style pending" and plan citation placement.
- Missing word limit blocks final draft density; ask for it before drafting unless the user requested a generic plan.
- Missing rubric does not block research; mark rubric fit as provisional.

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
  ai_use_policy:
  output_requested:
```

## InputReadinessReport

Before planning or drafting, produce internally or visibly when useful:

```yaml
InputReadinessReport:
  ready_for:
    - plan
    - research
    - draft
    - docx
  blockers:
  assumptions:
  open_requirements:
  evidence_available:
  evidence_missing:
  next_action:
```

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
  open_questions:
  assumptions:
```

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
