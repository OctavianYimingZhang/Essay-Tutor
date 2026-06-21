# QA And Validation

Use this reference before showing a plan, delivering a draft, creating DOCX output, or publishing the Skill package.

## Plan QA

Check that the plan answers these questions:

```yaml
PlanQA:
  exact_task_understood:
  task_type_confirmed:
  submission_mode_confirmed:
  audience_or_marker_confirmed:
  assignment_brief_built:
  asking_questions_batch_presented:
  plan_mode_used_for_native_question_flow:
  intake_payload_generated_with_script:
  request_user_input_called_with_generated_payload:
  plan_or_decision_context_displayed_before_questions:
  locked_brief_present:
  user_double_check_captured:
  readiness_states_recorded:
  no_plan_changing_inferred_requirements:
  no_plan_changing_evidence_gaps:
  no_plan_changing_open_items:
  evidence_map_started:
  comparison_diagnosis_used_when_available:
  structure_matches_rubric_or_brief:
  citation_quantity_confirmed:
  format_requirements_confirmed:
  title_font_size_confirmed:
  section_by_section_plans_presented:
  each_section_plan_user_feedback_captured:
  paragraph_level_section_feedback_captured:
  section_questions_use_real_paragraph_labels:
  section_options_are_task_specific:
  critical_analysis_plan_presented:
  critical_analysis_plan_user_feedback_captured:
  critical_move_selection_captured:
  critical_moves_have_body_or_discussion_insertion_points:
  essay_structure_present_when_task_is_essay:
  main_body_subsections_named_when_task_is_essay:
  non_essay_structure_matches_task_type:
  lab_analysis_tool_confirmed:
  lab_analysis_method_confirmed:
  lab_analysis_scope_confirmed:
  poster_story_plan_present:
  presentation_storyboard_present:
  website_interaction_plan_present:
  figure_generation_spec_present:
  figure_legend_requirements_confirmed:
  section_rationales_explain_argument_flow:
  section_plans_have_paragraph_level_claim_paths:
  section_density_justified_by_evidence_and_purpose:
  citation_strategy_clear:
  figure_table_data_strategy_clear:
  task_specific_workflow_clear:
  output_format_clear:
  user_preferences_handled:
```

A strong plan explains the task type, argument or communication flow, evidence burden, confirmed citation quantity, section or panel rationale, paragraph-level output path where relevant, proof logic, citation strategy, critical-analysis placement, task-specific workflow, format requirements, title font size for DOCX output, and revision boundaries in natural language. It should read as a coherent academic work plan rather than a mechanical field-by-field worksheet. Every Asking Questions batch should follow a displayed plan or decision context.

Do not show a final integrated plan if any unresolved item could change task type, structure, evidence depth, citation quantity, citation strategy, final language, output form, format requirements, critical-analysis stance, section density, analysis tool, analysis method, visual hierarchy, interaction design, figure legend content, or target standard. Ask another question, request the missing material, present the relevant section or task-specific plan for revision, or obtain an explicit user selection instead.

## Draft QA

Check that the draft has:

```yaml
DraftQA:
  confirmed_plan_reflected:
  confirmed_task_type_reflected:
  confirmed_citation_quantity_reflected:
  confirmed_format_requirements_reflected:
  selected_paragraph_level_section_plans_reflected:
  selected_critical_moves_reflected:
  essay_structure_followed_when_task_is_essay:
  main_body_subsections_used_when_task_is_essay:
  non_essay_output_structure_matches_task_type:
  claims_supported_by_sources_or_data:
  evidence_strength_calibrated:
  paragraph_functions_clear:
  interpretation_close_to_evidence:
  boundaries_or_uncertainty_integrated:
  critical_moves_fit_evidence:
  non_obvious_claims_have_nearby_citations:
  section_density_matches_value_and_complexity:
  citation_style_consistent:
  results_match_authoritative_analysis:
  analysis_tool_and_method_match_verified_output:
  figure_legends_match_verified_details:
  interaction_or_visual_copy_matches_story_plan:
  conclusion_answers_task:
```

Use the check to guide revision. Strengthen support, qualify claims, reorganise paragraphs, or adjust density where the draft needs it.

## Pre-Draft QA

Before drafting a new academic writing task, check:

- a Codex Asking Questions batch has been used for plan-changing requirements, or the user has supplied equivalent confirmed requirements;
- Plan Mode was used for the native Asking Questions flow;
- the intake payload was generated with `scripts/build_intake_questions.py` or matched its schema;
- the relevant brief, paragraph plan, format plan, or critical-analysis plan was displayed before `request_user_input`;
- `request_user_input` was called with that generated payload before plan-changing requirements were treated as confirmed;
- the brief is locked before any StructurePlan is shown;
- every plan-changing requirement is verified from materials or explicitly selected by the user;
- task type and submission mode are confirmed when the assignment could be an Essay, Lab Report, Poster, Presentation, Interactive Website, Figure Generation, or Figure Legend;
- citation quantity or density is confirmed by user selection or assignment material, with an approximate count plus density when useful;
- format requirements are confirmed by generated context-specific options, supplied style guide, or explicit custom user instructions;
- typography, font size, margins, line spacing, title style, and reference formatting are confirmed for DOCX, Word, LaTeX, or formatted file output;
- lab reports with data analysis have confirmed analysis tool, analysis method, and analysis scope before Results writing;
- posters have confirmed canvas, message hierarchy, and required visual or data assets before layout planning;
- presentations have confirmed timing, audience or assessment mode, and speaker notes or script expectation before storyboard planning;
- interactive websites have confirmed output mode, interaction model, and platform or technology constraints before website planning;
- figure generation tasks have confirmed figure purpose, source or data basis, and generation or editing tool before figure specification;
- figure legends have confirmed legend depth, statistical details, and source or permission note before final legend writing;
- no `inferred_requirements`, `evidence_gaps`, `task_specific_open_items`, or `open_items` remain if they could change task type, structure, evidence depth, citation quantity, citation strategy, final language, output form, format requirements, critical-analysis stance, section density, analysis tool, analysis method, visual hierarchy, interaction design, legend content, or target standard;
- each paragraph-level SectionPlan has been presented with real paragraph labels and task-specific options when the task has prose sections, and user feedback has been captured before the final integrated plan;
- a direct CriticalAnalysisPlan has been presented after paragraph planning as specific critical moves with body-paragraph or Discussion insertion points when evaluative writing is needed, and user move-level feedback has been captured before the final integrated plan;
- the plan includes Abstract, Introduction, Main Body subsections, Discussion, Conclusion, and References only when the task is an essay or the brief requires that structure;
- the user has confirmed the plan or provided corrections that have been integrated;
- word limit or expected scope, citation style, citation quantity, final language, output format, format requirements, title font size when needed, source base, task-specific workflow, critical-analysis stance, and target quality are handled in the plan.

## Comparison QA

When both a user draft and a generated result are available, check:

```yaml
ComparisonQA:
  argument_depth:
  body_length_and_limit_fit:
  source_range:
  claim_level_citation_density:
  paragraph_roles:
  critical_stance:
  discussion_quality:
  figure_table_or_data_use:
  visual_docx_format_problems:
  user_draft_strengths_preserved:
  generated_result_limitations_addressed:
  transferable_strengths_preserved:
  revision_priorities_reflected_in_plan:
```

Use this comparison before planning revision. Preserve useful structure, evidence density, and critical stance from the stronger draft while correcting weak formatting, unsupported claims, low-density sections, and generated-result weaknesses.

## Citation QA

Check:

- every in-text citation has a matching reference entry;
- every reference entry has a clear role in the work;
- each cited source supports the sentence or paragraph where it appears;
- non-obvious factual, mechanistic, theoretical, clinical, methodological, comparative, and evaluative claims have nearby citation support;
- critical claims about study weakness, theory limits, method limits, inconsistency, or generalisability are supported by the evaluated source or a source that demonstrates the contrast;
- low citation density has been resolved by adding verified support, narrowing claims, or removing unsupported statements rather than by treating citation density as a cosmetic issue;
- metadata is verified where identifiers, dates, or publication details matter;
- citation style is consistent with the assignment or local guide.

## Visual, Table, And Data QA

Check:

```yaml
VisualDataQA:
  communication_purpose_clear:
  source_or_data_basis_clear:
  analysis_tool_confirmed_when_relevant:
  analysis_method_confirmed_when_relevant:
  labels_units_and_abbreviations_clear:
  figure_legend_requirements_clear:
  caption_explains_reader_takeaway:
  statistics_match_analysis_output:
  permission_or_authorship_recorded:
  text_interprets_the_item:
```

Use this check for figures, tables, diagrams, statistical summaries, GraphPad Prism outputs, R Studio outputs, Python outputs, MatLab outputs, spreadsheets, generated visuals, poster panels, presentation visuals, interactive website media, and figure legends.

## Task-Specific QA

Use these checks in addition to the general plan and draft checks:

- Lab report: analysis tool, analysis method, analysis scope, sample basis, exclusions, statistics, figure/table destinations, and result interpretation are verified before Results writing.
- Poster: title, take-home message, panel hierarchy, visual/data assets, figure legends, readability, citation placement, and submission format match the brief.
- Presentation: slide timing, slide purpose, transition logic, audience fit, visual placement, citation placement, speaker notes or script, and final output mode match the brief.
- Interactive website: target user, pages or sections, interaction model, data/media assets, accessibility, navigation, citations, and platform constraints support the academic argument.
- Figure generation: purpose, claims represented, source or data basis, panel structure, labels, style, tool choice, output format, citation, and permission status are traceable.
- Figure legend: what is shown, reader takeaway, panel descriptions, sample or data basis, groups or conditions, statistics, error bars, units, scale bars, abbreviations, source, authorship, and permission are included when verified and omitted or queried when not verified.

## DOCX QA

Check:

- the DOCX was visually checked through rendered page images when rendering tools are available;
- format problems found in render review were fixed and re-rendered;
- requested or default academic formatting is applied;
- user-confirmed or default title font size is applied to the main title;
- headings, body text, captions, tables, and references are readable and consistent;
- academic text and headings are black unless the assignment material explicitly requires colour;
- the document body presents submit-ready assignment-facing academic content, with workflow state and planning metadata kept in the conversation or internal planning record;
- spacing is visually coherent and does not create excessive line gaps;
- final pages contain meaningful content rather than accidental blanks;
- page breaks support reading flow;
- figures and tables are near the relevant discussion where practical;
- figure scale and caption placement work in the rendered page image;
- reference entries wrap cleanly and remain readable;
- the document uses the available page or word budget for evidence, explanation, comparison, and critical analysis when the assignment sets an upper limit;
- exported PDF reflects the latest DOCX when PDF is requested;
- document structure supports the assignment rather than adding formatting clutter.

## Evidence Gap Handling

When a claim, statistic, method detail, citation, or figure element lacks support:

1. Look for support in the supplied assignment material or authoritative source base.
2. Reword the claim to match the available evidence.
3. Move the point into a limitation, uncertainty, or future-work statement if that better fits the evidence.
4. Keep the final work focused on points that help answer the task.

## Package QA

Before publishing Skill changes, run:

```bash
python3 scripts/skill_maintenance.py doctor
python3 scripts/validate_essay_tutor.py --strict
```

Review that `SKILL.md` links to existing references, repository content remains English, and guidance is organised by function.
