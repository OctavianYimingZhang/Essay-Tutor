# QA And Validation

Use this reference before showing a plan, drafting an essay, creating DOCX output, or publishing the Skill package.

## Plan QA

A plan passes only when:

```yaml
PlanQA:
  exact_question_addressed: true
  ask_user_used_for_material_decisions_when_available: true
  tutor_planning_loop_used_before_final_plan: true
  no_plain_text_bulk_questionnaire_when_ask_user_available: true
  no_unconfirmed_plan_assumptions: true
  open_user_decisions_empty: true
  plan_mode_proposed_plan_only_when_decision_complete: true
  interpreted_scope_present: true
  thesis_present: true
  word_limit_strategy_present: true
  main_body_has_subtitles: true
  each_subtitle_has_specific_content: true
  discussion_has_synthesis_limitation_future: true
  citation_strategy_present: true
  figure_table_strategy_present: true
  critical_thinking_strategy_present: true
  confirmed_requirements_visible: true
```

Fail or revise the plan when it contains only generic headings. Do not output a detailed plan when citation style, academic level, word or page limit, output format, source base, final language, or rubric status is still unconfirmed.

## Interaction QA

Check:

- native `request_user_input` / ask-user UI was preferred for material requirement and plan decisions when available;
- ask-user prompts contained one to three meaningful decisions, not a long questionnaire;
- each ask-user decision included a brief explanation of the academic or workflow tradeoff;
- normal chat fallback was used only when ask-user UI or Plan Mode was unavailable;
- the agent did not claim the Skill can force Codex into Plan Mode;
- in Plan Mode, the final essay plan was wrapped in `<proposed_plan>` only after open decisions were empty;
- outside Plan Mode, the same planning contract was followed and explicit approval was required before drafting.

## Draft QA

A draft passes only when:

```yaml
DraftQA:
  no_unsupported_claims: true
  no_fake_citations: true
  no_unverified_identifier_metadata: true
  no_overclaiming: true
  parenthetical_citation_style_used_by_default: true
  avoidable_author_led_citations_removed: true
  critical_analysis_tasks_present: true
  main_body_at_least_30_percent_analytic: true
  discussion_mostly_analytic: true
  paragraph_logic_visible: true
  citation_density_appropriate: true
  word_limit_met_or_variance_reported: true
  deleted_capacity_reallocated_to_argument: true
  no_true_but_unneeded_detail_catalogues: true
  alternative_explanations_and_scope_checked: true
  data_model_fit_or_regression_quality_reported_when_relevant: true
  no_first_person_process_or_button_click_method_narration: true
  notation_units_and_parameter_names_consistent: true
  no_graph_based_mechanism_inference_without_design_support: true
  conclusion_contains_no_new_evidence: true
  figure_permissions_checked: true
  bibliography_complete: true
```

## Citation QA

Check:

- every in-text citation has a matching reference-list entry;
- every reference-list entry is cited unless it is explicitly further reading;
- claim-led parenthetical citation is used by default;
- author-led citation wording remains only when authorship, method, disagreement, theory history, or source comparison is the sentence function;
- DOI, PMID, arXiv, ISBN, or publisher metadata is verified where possible;
- claim strength matches the evidence;
- a review is not cited as primary evidence;
- an unread source is not cited for a specific claim.

## Visual QA

Check:

- direct figure reuse has license or permission;
- generated figures are original schematics;
- every label is source-backed;
- no generated figure introduces new factual claims;
- figure legends state source or generated status;
- tables are used by the argument and formatted academically.

## DOCX QA

Check:

- file opens;
- margins are 2.5 cm;
- font is Arial;
- line spacing is 1.5;
- body is justified;
- main title is centered;
- subheadings are left aligned;
- references are present when citations are used;
- figure captions and table captions are present where needed.

## Failure Conditions

Rewrite, block, or mark unresolved when any item appears:

- invented citation;
- unverified DOI/PMID used as if verified;
- fake statistic;
- unsupported mechanism;
- plain-text bulk requirement questioning when native ask-user UI was available;
- skipping the tutor planning loop before a decision-complete plan;
- using `<proposed_plan>` before all material decisions are resolved;
- claiming the Skill can force Codex into Plan Mode;
- pre-plan defaulting of citation style, academic level, word limit, page limit, or output format;
- a detailed plan with unresolved user decisions;
- source-route narration inside essay prose;
- avoidable author-led citation wording;
- mainly descriptive discussion;
- discussion that repeats the main body without synthesis, evidence evaluation, claim scope, or specific future direction;
- large deletions that remove content without improving mechanism, interpretation, limitation, evidence strength, scope, or link-back;
- revision that saves words but then spends them on extra background, citation volume, or named-detail catalogues;
- lab-report methods written as chronological button clicks rather than reproducible scientific configuration and controls;
- results sections that list calculations or trendlines without fit quality, model choice, or interpretation;
- graph or trendline language that implies mechanism not tested by the design;
- inconsistent notation, units, variable names, or parameter names;
- conclusions that simplify nonlinear, saturating, or model-based data into unsupported proportional claims;
- paper figure reused without license or permission;
- mechanism figure introduces unsupported biology or theory;
- decorative table not used by the argument;
- conclusion adds new evidence;
- word count exceeded without warning;
- copied third-party Skill code without license review.

## Skill Package QA

Before publishing this repository:

```bash
python3 scripts/skill_maintenance.py doctor
python3 scripts/validate_essay_tutor.py --strict
```

The package fails if:

- `SKILL.md` frontmatter is invalid;
- required reference files are missing;
- template placeholders remain;
- non-English repository content is detected;
- license or README is missing;
- health commands fail.
