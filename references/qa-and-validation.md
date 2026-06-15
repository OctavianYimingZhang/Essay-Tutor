# QA And Validation

Use this reference before showing a plan, delivering a draft, creating DOCX output, or publishing the Skill package.

## Plan QA

Check that the plan answers these questions:

```yaml
PlanQA:
  exact_task_understood:
  assignment_brief_built:
  brief_check_presented:
  user_double_check_captured:
  readiness_states_recorded:
  evidence_map_started:
  structure_matches_rubric_or_brief:
  essay_structure_present_when_task_is_essay:
  main_body_subsections_named_when_task_is_essay:
  section_density_justified:
  citation_strategy_clear:
  figure_table_data_strategy_clear:
  output_format_clear:
  user_preferences_handled:
```

A strong plan explains what each section does, what evidence it uses, and how it contributes to the assignment.

## Draft QA

Check that the draft has:

```yaml
DraftQA:
  confirmed_plan_reflected:
  essay_structure_followed_when_task_is_essay:
  main_body_subsections_used_when_task_is_essay:
  claims_supported_by_sources_or_data:
  evidence_strength_calibrated:
  paragraph_functions_clear:
  interpretation_close_to_evidence:
  boundaries_or_uncertainty_integrated:
  section_density_matches_value_and_complexity:
  citation_style_consistent:
  results_match_authoritative_analysis:
  conclusion_answers_task:
```

Use the check to guide revision. Strengthen support, qualify claims, reorganise paragraphs, or adjust density where the draft needs it.

## Pre-Draft QA

Before drafting a new essay, check:

- the Brief Check has been presented or the user has supplied equivalent confirmed requirements;
- the plan includes Abstract, Introduction, Main Body subsections, Discussion, Conclusion, and References where sources are used;
- the user has confirmed the plan or provided corrections that have been integrated;
- word limit or expected scope, citation style, final language, output format, source base, and target quality are handled in the plan.

## Citation QA

Check:

- every in-text citation has a matching reference entry;
- every reference entry has a clear role in the work;
- each cited source supports the sentence or paragraph where it appears;
- metadata is verified where identifiers, dates, or publication details matter;
- citation style is consistent with the assignment or local guide.

## Visual, Table, And Data QA

Check:

```yaml
VisualDataQA:
  communication_purpose_clear:
  source_or_data_basis_clear:
  labels_units_and_abbreviations_clear:
  caption_explains_reader_takeaway:
  statistics_match_analysis_output:
  permission_or_authorship_recorded:
  text_interprets_the_item:
```

Use this check for figures, tables, diagrams, statistical summaries, GraphPad outputs, spreadsheets, and generated visuals.

## DOCX QA

Check:

- requested or default academic formatting is applied;
- headings, body text, captions, tables, and references are readable and consistent;
- figures and tables are near the relevant discussion where practical;
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
