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
  submission_mode:
  word_limit_or_expected_scope:
  output_form:
  final_language:
  citation_style:
  citation_quantity:
  format_requirements:
  title_font_size:
  visual_requirements:
  interaction_requirements:
  analysis_tool:
  analysis_method:
  figure_legend_requirements:
  source_base:
  rubric_or_marking_evidence:
  user_preferences:
  useful_constraints:
  task_specific_open_items:
  confirmation_status:
  unresolved_plan_changing_items:
```

Use the smallest brief that supports the current task. A quick revision may need only question, task type, source base, output form, citation style, citation quantity, and format requirements; a new essay usually benefits from word limit or expected scope, source base, citation style, citation quantity, output format, final language, target quality, and any course-stage requirement that changes marking criteria or genre expectations. Posters, presentations, interactive websites, figure generation tasks, figure legends, and lab reports need the task-specific fields that affect structure, visual hierarchy, interaction, analysis, or legend content.

Lock the brief before planning. A locked brief has no unresolved item that could change task type, structure, evidence depth, citation quantity, citation strategy, final language, output form, format requirements, section density, visual hierarchy, interaction design, analysis tool, analysis method, figure legend requirements, critical-analysis stance, or the expected standard. For DOCX, Word, or formatted file output, also resolve title font size before document planning; use `14 pt main title` only when the user accepts the default format or does not provide a custom title-size preference.

Treat academic standard as a writing-quality target, not a routine form field. Unless the assignment material or user states otherwise, aim for the strongest academic depth the task and source base can support. Ask about course stage only when it would materially change evidence selection, theoretical depth, writing identity, or marking fit.

## Material Diagnosis

Before asking questions or planning, inspect the materials the user supplied:

- assignment brief, rubric, learning outcomes, style guide, and lecturer notes;
- user draft, generated draft, prior feedback, user-supplied exemplar, teacher example, sample answer, model essay, feedback example, screenshot, image, figure, table, dataset, and DOCX/PDF file;
- requested output format, custom format instructions, visual examples, page or word limit, citation style, citation quantity, title font size, source base, analysis tool, analysis method, figure legend requirements, interaction requirements, and submission mode.

When both a user draft and a generated result are available, build a comparison diagnosis before planning revision:

```yaml
ComparisonDiagnosis:
  argument_depth:
  body_length_and_limit_fit:
  source_range:
  claim_level_citation_density:
  paragraph_roles:
  critical_stance:
  discussion_quality:
  figure_table_or_data_use:
  visual_docx_format_problems:
  user_draft_strengths_to_preserve:
  generated_result_limitations:
  revision_priorities:
```

Use this diagnosis to decide what to preserve, what to strengthen, and how the revised plan should improve argument depth, paragraph function, evidence density, critical stance, and formatting.

## Readiness States

Classify each material item before planning:

```yaml
ReadinessState:
  verified_from_materials:
  user_confirmed:
  inferred_from_context:
  user_preference_needed:
  evidence_gap:
```

Use these states to decide the next action:

- `verified_from_materials`: use directly and cite the source of the requirement when useful.
- `user_confirmed`: use as the planning basis.
- `inferred_from_context`: record only during intake; resolve it through user confirmation or source verification before planning.
- `user_preference_needed`: ask a concise question because the answer changes task type, structure, evidence, citation style, visual hierarchy, interaction design, analysis, legend content, or output.
- `evidence_gap`: record only during intake; resolve it before planning if it could change task type, structure, evidence, citation style, language, output form, section density, visual hierarchy, interaction design, analysis, legend content, or target standard.

Do not carry `inferred_from_context`, `user_preference_needed`, or plan-changing `evidence_gap` items into a StructurePlan. If they remain, continue asking questions or request the missing material instead of writing the plan.

## Intake Sources

Use assignment evidence in this order:

1. Exact prompt, brief, rubric, learning outcomes, and marking descriptors.
2. User-provided files, teacher feedback, examples, datasets, and analysis outputs.
3. Course slides, handbooks, required readings, and local style guides.
4. User preferences for target grade, output form, language, and workflow.
5. External academic sources when the assignment benefits from more evidence.

## Interaction Depth

Scale the interaction to the clarity of the assignment:

- **Sparse prompt**: use Codex Asking Questions to lock foundational decisions about task type, word limit or expected scope, citation style, citation quantity, final language, output format, format requirements, source base, target quality, and any course-stage requirement that affects marking before planning.
- **Partial prompt**: ask only the missing items that change structure, evidence depth, citation strategy, or output form.
- **Complete prompt**: summarise the brief in natural language and use Codex Asking Questions to confirm it or request corrections before presenting the plan.

Use interaction to make the plan reliable, not to collect cosmetic preferences. Every academic writing task needs a confirmed brief before structure planning, even when the original prompt appears complete. Continue the conversation until the goal, audience, output use, thesis direction, evidence burden, source base, structure tradeoffs, and revision boundaries are clear enough to teach from.

## Question Batch

Use a Question Batch before the first full writing plan unless the user has already supplied a complete confirmed brief. Before every `request_user_input` call, display the relevant plan or decision context in ordinary chat so the user can judge the options against a concrete proposal. Generate the tool payload with `scripts/build_intake_questions.py task-type` when the output genre is unclear, `scripts/build_intake_questions.py sparse` for sparse or partial prompts, or `scripts/build_intake_questions.py complete` when the brief only needs confirmation. Call `request_user_input` with the emitted JSON object.

Keep `AssignmentBrief`, readiness states, material gaps, and planning metadata as internal working models unless the user explicitly asks to inspect them.

Ask at most one to three plan-changing questions in each `request_user_input` call. Each question should choose between meaningful academic or workflow options generated from the current prompt, supplied material, locked brief, displayed plan, and real tradeoffs. When a recommended default is reasonable, make that option first. For standard sparse essay prompts, use the generated sparse payload as the first call, then use `scripts/build_intake_questions.py brief-details` if final language, citation style, or source base remain unresolved. For lab reports with data analysis, use `scripts/build_intake_questions.py lab-analysis` unless the analysis tool, method, and scope are verified from supplied material. For posters, presentations, interactive websites, figure generation, or figure legends, use `scripts/build_intake_questions.py poster-plan`, `scripts/build_intake_questions.py presentation-plan`, `scripts/build_intake_questions.py website-plan`, `scripts/build_intake_questions.py figure-plan`, or `scripts/build_intake_questions.py figure-legend` when those task-specific choices are unresolved. For DOCX, Word, LaTeX, or formatted file output, use `scripts/build_intake_questions.py docx-format` or `scripts/build_intake_questions.py document-format` after the output form is selected to ask about typography, font size, margins, line spacing, title style, and reference formatting. For a complete brief, use the generated complete payload and then adapt follow-up payloads only for remaining plan-changing items. The sparse and complete payloads must ask about citation quantity and format requirements unless those exact requirements are already verified from supplied material.

Ask enough to resolve plan-changing requirements before planning. Common plan-changing requirements include:

- course-stage or marking standard when it changes genre, evidence, or evaluation;
- task type, including Essay, Lab Report, Poster, Presentation, Interactive Website, Figure Generation, or Figure Legend when the prompt is ambiguous;
- word limit or expected scope;
- citation style or local style guide;
- citation quantity or density, expressed as an approximate source or citation count plus a density description when the brief does not set an exact number;
- final language;
- output form, with options generated from context and normally including chat text, DOCX, and LaTeX when no format is specified;
- format requirements, including whether to use the generated default for that output type or custom user instructions;
- typography, font size, margin, line spacing, title style, and reference formatting for DOCX, Word, LaTeX, or formatted file output;
- analysis tool, analysis method, and analysis scope for lab reports and data-supported assignments;
- poster canvas, message hierarchy, and required visual or data assets;
- presentation timing, audience, and speaker notes or script expectation;
- website output mode, interaction model, and platform or technology constraints;
- figure purpose, source or data basis, and generation or editing tool;
- figure legend depth, statistical details, and source or permission note;
- source base, including whether to use course material, external literature, user files, or data;
- target quality or marking standard;
- rubric, brief, learning outcomes, or required readings.

When asking about format requirements, generate options from the user's prompt and output context. If the user selects DOCX, Word, LaTeX, or another formatted file output, ask a follow-up formatting batch before document planning. If the user does not select a generated default, require explicit custom format instructions through the user's free-form answer or supplied style guide before planning.

## User Questions

Ask user questions when the answer materially changes the plan and cannot be verified from local material. Good questions choose between meaningful academic or workflow tradeoffs, such as:

- final output form;
- task type and submission mode when the assignment could be an essay, lab report, poster, presentation, interactive website, figure generation task, or figure legend;
- citation style or local style guide;
- citation quantity or density, including an approximate source or citation count when useful;
- intended target standard;
- word limit or expected scope;
- course-stage or marking standard when it changes genre, evidence, or evaluation;
- final language;
- chat text versus DOCX versus LaTeX versus user-specified custom format;
- typography, font size, margins, line spacing, title style, and reference formatting for DOCX, Word, LaTeX, or formatted file output;
- whether to prioritise course material, external literature, or user-provided data;
- which analysis tool and statistical or model method to use for lab-report data analysis;
- which poster, presentation, website, figure, or figure legend workflow decisions control the output;
- how to handle conflicting teacher feedback, rubric criteria, or examples.

Use `request_user_input` for material decisions, including during Plan Mode. Provide meaningful choices and require an explicit user selection for plan-changing items. Build custom follow-up payloads by matching the same schema emitted by `scripts/build_intake_questions.py`; use the script's context JSON support when generating dynamic labels, paragraph titles, critical moves, or task-specific options.

Use assumptions only for non-plan-changing details, and make them visible in the plan.

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

When an assignment gives an upper page or word limit, plan to use the available space for relevant evidence, mechanism explanation, comparison between sources, critical interpretation, and limitations until the argument is appropriately developed near the limit. When the prompt gives a minimum, range, or expected scope, calibrate length by task purpose, knowledge density, source complexity, and the depth needed to satisfy the brief.

## Structure Planning

A useful plan explains the argument in natural language rather than mechanically filling labels. It should show the user's confirmed choices, why the section order works, what each section needs to prove, what each paragraph will output, what conclusion or result will support the claim, where critical evaluation belongs, and how the final output will be formatted.

```yaml
StructurePlan:
  working_title:
  interpreted_task:
  task_type:
  submission_mode:
  audience_or_marker:
  thesis_or_central_answer:
  user_confirmed_brief:
  citation_quantity:
  format_requirements:
  title_font_size:
  task_specific_workflow:
  analysis_tool:
  analysis_method:
  visual_requirements:
  interaction_requirements:
  figure_legend_requirements:
  critical_analysis_plan:
    evaluative_questions:
    source_quality_limits:
    theory_or_mechanism_limits:
    comparison_points:
    uncertainty_or_boundary_claims:
    thesis_link:
  section_plan:
    - heading:
      section_function:
      rationale:
      paragraph_level_plan:
        - paragraph_id:
          write_what:
          how_to_write:
          paragraph_function:
          key_terms_or_concepts:
          proof_logic:
          conclusion_or_result_used_to_support_claim:
          critical_or_comparative_work:
          transition_role:
          user_decision:
      paragraph_level_claim_path:
      key_terms_or_concepts:
      conclusions_to_verify:
      citation_strategy_for_claims:
      citation_density_target:
      critical_or_comparative_work:
      expected_length_or_density:
      formatting_or_visual_role:
      transition_role:
  citation_strategy:
  comparison_diagnosis:
  output_strategy:
  task_specific_open_items:
  open_items:
```

Only create a StructurePlan after the brief is locked. `open_items` may contain only non-plan-changing notes, such as optional refinements that do not affect structure, evidence depth, citation quantity, citation strategy, language, output form, format requirements, critical-analysis stance, section density, or target standard.

Prefer argument-facing section rationales over generic headings. For example, "compare the two mechanisms that explain the result and identify the stronger causal evidence" is more useful than "Discussion".

## Task-Specific Workflows

Use the task type to select the planning workflow. Do not force essay-only sections onto posters, presentations, interactive websites, standalone figures, or figure legends. Keep the same locked-brief rule: unresolved task-specific items stay in `task_specific_open_items` during intake and block the final integrated plan when they could change structure, evidence, analysis, visual hierarchy, interaction, legend content, or output format.

### Lab Report Workflow

For lab reports and data-supported coursework, ask for the analysis tool, analysis method, and analysis scope with `scripts/build_intake_questions.py lab-analysis` unless those details are verified from the brief, supplied data, or analysis output. Acceptable analysis tools include GraphPad Prism, R Studio, Python, MatLab, spreadsheet tools, SPSS, Jamovi, or another user-specified tool.

Do not infer a statistical test, model, post hoc correction, or repeated-measures structure from topic wording alone. A method such as two-way repeated-measures ANOVA is usable only when it is verified from assignment instructions, supplied analysis output, the dataset design after explicit user discussion, or the user's direct answer.

Plan lab reports around:

- research aim, hypothesis, or question;
- method and data basis;
- verified analysis tool and statistical or descriptive method;
- result sequence and figure/table destinations;
- interpretation, limitations, and relation to the aim;
- figure legends and result text that preserve sample sizes, units, tests, estimates, p values, uncertainty, and exclusions exactly as supported.

### Poster Workflow

For posters, ask for canvas, message hierarchy, and required visual/data assets with `scripts/build_intake_questions.py poster-plan` unless the brief already specifies them. Build a poster-story plan rather than an essay outline.

Plan posters around:

- title and one-sentence take-home message;
- intended marker or audience;
- panel hierarchy and reading order;
- methods, results, interpretation, and conclusion density;
- figures, tables, diagrams, legends, and source notes;
- readability, alignment with rubric, and submission format.

### Presentation Workflow

For presentations, ask for timing, audience, and speaker notes or script expectation with `scripts/build_intake_questions.py presentation-plan` unless those requirements are verified. Build a storyboard rather than a prose outline.

Plan presentations around:

- slide count or timing constraint;
- audience and assessment mode;
- slide-by-slide purpose and transition;
- visual assets, figure/table placement, and citation placement;
- speaker notes, full script, or slide-text-only output;
- opening, evidence sequence, critical interpretation, and closing answer.

### Interactive Website Workflow

For interactive websites, ask for output mode, interaction model, and platform constraints with `scripts/build_intake_questions.py website-plan` unless those requirements are verified. Build an academic-content and interaction plan, then use any relevant web-app Skill only for implementation details if the user asks to build files.

Plan interactive websites around:

- target user and assessment fit;
- page, section, or route structure;
- user journey and interaction model;
- data, media, figure, or citation assets;
- accessibility, navigation, and platform or technology constraints;
- how interaction helps the academic argument rather than decorating it.

### Figure Generation Workflow

For figure generation, ask for figure purpose, source or data basis, and generation or editing tool with `scripts/build_intake_questions.py figure-plan` unless those decisions are verified. Build an evidence-bound figure specification before creating or editing visuals.

Plan figures around:

- purpose in the argument or assignment;
- claims represented and source/data basis;
- panel structure and reading order;
- labels, units, scales, legends, abbreviations, and visual style;
- tool choice, editable output needs, and file format;
- citation, authorship, and permission status.

### Figure Legend Workflow

For standalone figure legends or figures inside larger tasks, ask for legend depth, statistics/detail requirements, and source or permission note with `scripts/build_intake_questions.py figure-legend` unless those requirements are verified. A complete figure legend contract covers what is shown, sample or data basis, groups and conditions, statistics, error bars, units, scale bars, abbreviations, source or permission, and the reader takeaway.

Write legends so the reader can interpret the figure without guessing the experimental basis. Include only statistics, sample sizes, methods, or permissions that are supported by the supplied analysis output, figure source, assignment material, or user-confirmed information.

## Section-By-Section Planning

Before presenting the final integrated plan, present each planned section as a standalone `SectionPlan` and ask the user for paragraph-level decisions with `scripts/build_intake_questions.py section-review` or a matching `request_user_input` payload. Display the paragraph plan first, then ask. Do not move to the final integrated plan until every planned paragraph has a user decision or a revision based on the user's free-form answer.

Each `SectionPlan` must include:

- heading and section function;
- detailed argument role and reason for its position in the work;
- paragraph-level plan labelled with the real paragraph role, such as `Abstract`, `Introduction`, `Main Body Paragraph 1: mechanism`, `Discussion Paragraph 1: limitation synthesis`, or `Conclusion`;
- for each paragraph: what to write, how to write it, paragraph function, transition role, and how it supports the section;
- proof logic for each paragraph: what conclusion, relationship, mechanism, result, limitation, or comparison will be used to prove the paragraph's claim;
- key concepts that need definition or explanation;
- conclusions or results to verify before drafting;
- citation-density target based on the user's selected citation quantity;
- critical or comparative work for that section;
- expected length or density based on assignment space and evidence complexity;
- formatting, figure, table, or visual role where relevant;
- transition role into the next section.

For SectionPlan feedback, show the paragraph-level plan first, then call `request_user_input` with one question per paragraph. Ask at most three paragraph questions at a time; if a section has more than three planned paragraphs, ask about the next three named paragraphs first, revise or record those decisions, then ask about the remaining paragraphs in another batch. Each paragraph question must use the real paragraph title and task-specific options that expose actual choices in the displayed plan, such as changing the opening logic, compressing low-value background, shifting evidence emphasis, splitting a dense mechanism paragraph, moving a limitation, or changing the transition.

In a SectionPlan, describe the paragraph as output logic rather than citation routing. Show what the paragraph will say, how it will develop the point, and what conclusion, mechanism, result, limitation, or comparison will be used to support the paragraph's claim. Detailed source names and reference choices are handled in the evidence map and citation planning, while the user-facing paragraph prompt focuses on the content and argumentative effect.

## Critical Analysis Plan

After all paragraph-level plans have been discussed, read `references/critical-writing-bank.md` and use it with `references/drafting-and-critical-analysis.md` to create a direct `CriticalAnalysisPlan`. During the first Discussion section plan, reserve space for synthesis, limitations, evidence boundaries, or methodological appraisal when the essay needs critical analysis. Present specific critical moves and ask the user where and how to include them with `scripts/build_intake_questions.py critical-analysis` or a matching `request_user_input` payload.

The `CriticalAnalysisPlan` must cover:

- evaluative questions the essay or report will answer;
- source-quality limits, including method, sample, date, measurement, or bias concerns where relevant;
- theory, mechanism, or model limits;
- comparisons between sources, explanations, methods, datasets, or interpretations;
- uncertainty and boundary claims that prevent overstatement;
- how each critical move links back to the thesis or research question.

Break the `CriticalAnalysisPlan` into concrete critical moves such as field inadequacy, single-study weakness, theory or model limit, method or practice limit, source disagreement, and constructive suggestion. For each move, state what to criticise, how to write it, where it belongs in the body paragraphs or Discussion, and how it links back to the thesis. Ask about at most three critical moves at a time. Each move question must name the move directly and offer concrete placement or replacement choices rather than generic approval options.

## Planning With Exemplars

Use user-supplied exemplars, teacher examples, sample answers, model essays, feedback examples, visual examples, teacher reports, and feedback to identify transferable features:

- section order and proportional emphasis;
- paragraph function and density;
- figure, table, and caption pattern;
- style of result reporting;
- level of citation detail;
- tone, precision, critical stance, and formatting discipline.

Treat topic-specific claims from exemplars as leads. Bring them into the final work when the claim is supported by current assignment material, user data, course material, or verified sources.

## Approval Flow

For academic writing tasks, run a `request_user_input` Question Batch first, lock the brief, ask the task-specific workflow questions needed for lab reports, posters, presentations, interactive websites, figure generation, or figure legends, ask the DOCX title-font-size question when formatted file output is selected, present and resolve each paragraph-level SectionPlan when the task has prose sections, present and resolve the critical-move-level CriticalAnalysisPlan when evaluative writing is needed, then present the final integrated decision-complete plan for user double-check. In Codex Plan Mode, use the required `<proposed_plan>` format only for the final integrated plan unless the active system instructions require otherwise. Outside Plan Mode, use the same structure in normal chat.

Draft from the confirmed plan. If the user changes requirements, update and relock the brief before revising the plan or drafting.
