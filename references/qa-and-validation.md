# QA And Validation

Use this reference before showing a plan, drafting an essay, creating DOCX output, or publishing the Skill package.

## Plan QA

A plan passes only when:

```yaml
PlanQA:
  exact_question_addressed: true
  interpreted_scope_present: true
  thesis_present: true
  word_limit_strategy_present: true
  main_body_has_subtitles: true
  each_subtitle_has_specific_content: true
  discussion_has_synthesis_limitation_future: true
  citation_strategy_present: true
  figure_table_strategy_present: true
  critical_thinking_strategy_present: true
  assumptions_and_open_questions_visible: true
```

Fail or revise the plan when it contains only generic headings.

## Draft QA

A draft passes only when:

```yaml
DraftQA:
  no_unsupported_claims: true
  no_fake_citations: true
  no_unverified_identifier_metadata: true
  no_overclaiming: true
  main_body_at_least_30_percent_analytic: true
  discussion_mostly_analytic: true
  paragraph_logic_visible: true
  citation_density_appropriate: true
  word_limit_met_or_variance_reported: true
  conclusion_contains_no_new_evidence: true
  figure_permissions_checked: true
  bibliography_complete: true
```

## Citation QA

Check:

- every in-text citation has a matching reference-list entry;
- every reference-list entry is cited unless it is explicitly further reading;
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
- source-route narration inside essay prose;
- mainly descriptive discussion;
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
