# Intake And Planning

Use this reference when starting an academic writing task, interpreting an assignment brief, extracting rubric requirements, or preparing a structure plan.

## AssignmentBrief

Build a compact `AssignmentBrief` from the prompt and supplied material:

```yaml
AssignmentBrief:
  task_type:
  exact_question_or_title:
  essay_purpose:
  academic_context:
  intended_reader_or_marker:
  word_limit_or_expected_scope:
  output_form:
  final_language:
  citation_style:
  source_base:
  rubric_or_marking_evidence:
  user_preferences:
  useful_constraints:
  evidence_gaps:
```

Use the smallest brief that supports the current task. A quick revision may need only question, source base, output form, and citation style; a new essay usually benefits from academic level, word limit or expected scope, source base, citation style, output format, final language, and target quality.

## Readiness States

Classify each material item before planning:

```yaml
ReadinessState:
  verified_from_materials:
  inferred_from_context:
  user_confirmed:
  user_preference_needed:
  evidence_gap:
```

Use these states to decide the next action:

- `verified_from_materials`: use directly and cite the source of the requirement when useful.
- `inferred_from_context`: use as a working assumption and make it visible in the Brief Check.
- `user_confirmed`: use as the planning basis.
- `user_preference_needed`: ask a concise question because the answer changes structure, evidence, citation style, or output.
- `evidence_gap`: record the gap and shape the plan around what can be supported.

## Intake Sources

Use assignment evidence in this order:

1. Exact prompt, brief, rubric, learning outcomes, and marking descriptors.
2. User-provided files, teacher feedback, examples, datasets, and analysis outputs.
3. Course slides, handbooks, required readings, and local style guides.
4. User preferences for target grade, output form, language, and workflow.
5. External academic sources when the assignment benefits from more evidence.

## Interaction Depth

Scale the interaction to the clarity of the assignment:

- **Sparse prompt**: ask foundational questions about academic level, word limit or expected scope, citation style, final language, output format, source base, and target quality before planning.
- **Partial prompt**: ask only the missing items that change structure, evidence depth, citation strategy, or output form.
- **Complete prompt**: summarise the brief and ask the user to confirm or correct it before presenting the plan.

Use interaction to make the plan reliable, not to collect cosmetic preferences.

## Brief Check

Present a Brief Check before the first full essay plan:

```yaml
BriefCheck:
  confirmed_requirements:
  inferred_requirements:
  evidence_gaps:
  plan_changing_questions:
  next_step:
```

Keep the Brief Check concise. It should help the user double-check the task, especially when the original request provides only a title or broad topic.

## User Questions

Ask user questions when the answer materially changes the plan and cannot be verified from local material. Good questions choose between meaningful academic or workflow tradeoffs, such as:

- final output form;
- citation style or local style guide;
- intended target standard;
- word limit or expected scope;
- academic level;
- final language;
- whether to prioritise course material, external literature, or user-provided data;
- how to handle conflicting teacher feedback, rubric criteria, or examples.

When native ask-user UI is available, use it for material decisions. In normal chat, ask the same decision as a short direct question.

## Density Calibration

Set section density by judgement rather than fixed ratios. Give more space to content that has:

- higher rubric value or examiner emphasis;
- greater conceptual difficulty;
- more evidence to compare;
- more analysis, uncertainty, or limitation to explain;
- a stronger role in answering the question;
- a higher need for reader context;
- data, figure, or method details that affect interpretation.

Compress content that mainly repeats context already established, lists facts without changing the argument, or can be handled by a citation, table, figure, or short linking phrase.

## Structure Planning

A useful plan states what each section will do, what evidence it uses, and why the section deserves its density:

```yaml
StructurePlan:
  working_title:
  interpreted_task:
  thesis_or_central_answer:
  user_confirmed_brief:
  section_plan:
    - heading:
      function:
      key_claims:
      evidence_sources:
      expected_depth:
      figure_table_or_data_role:
      critical_move:
  citation_strategy:
  output_strategy:
  open_items:
```

Prefer section functions over generic headings. For example, "compare mechanisms that explain the result" is more useful than "Discussion".

## Planning With Exemplars

Use exemplars, teacher reports, and feedback to identify transferable features:

- section order and proportional emphasis;
- paragraph function and density;
- figure, table, and caption pattern;
- style of result reporting;
- level of citation detail;
- tone, precision, and critical stance.

Treat topic-specific claims from exemplars as leads. Use them in the final work only when the claim is supported by course material, user data, or verified sources.

## Approval Flow

For new essay creation, present a Brief Check first, then a decision-complete plan for user double-check. In Codex Plan Mode, use the required `<proposed_plan>` format. Outside Plan Mode, use a concise plan in normal chat.

Draft from the confirmed plan. If the user changes requirements, update the brief and plan before drafting.
