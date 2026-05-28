# Subagents

Use this reference after plan approval for multi-source research or high-stakes drafting. If real subagents are not available, execute the roles sequentially and keep the same output discipline.

## Delegation Rules

- Use subagents for independent, bounded tasks.
- Give each subagent an evidence-bound output schema.
- Do not ask subagents to invent facts or draft unsupported prose.
- Do not give two writing agents the same final file ownership.
- Verify subagent outputs before adding claims to the essay.

## Recommended Roles

### Question-and-Rubric Agent

```yaml
QuestionDeconstruction:
  command_verb:
  required_scope:
  excluded_scope:
  required_argument:
  examiner_expectation:
  risk_of_off_topic:
```

### Literature Retrieval Agent

```yaml
LiteratureMap:
  must_read:
  should_read:
  optional:
  excluded:
  reason_for_inclusion:
  claim_supported:
  identifiers:
    DOI:
    PMID:
    URL:
```

### Mechanism/Theory Agent

```yaml
MechanismMap:
  model:
  mechanism:
  source:
  evidence_strength:
  limitation:
  essay_section:
```

### Evidence Appraisal Agent

```yaml
EvidenceAppraisal:
  claim:
  supporting_sources:
  evidence_type:
  strength:
  limitation:
  allowed_verbs:
    - demonstrates
    - supports
    - suggests
    - is consistent with
    - implicates
```

### Citation Agent

```yaml
CitationMap:
  citation_key:
  source:
  DOI_or_PMID:
  used_for_claim:
  citation_mode:
    - intensive_reading
    - broad_support
    - review_context
    - primary_evidence
  in_text_location:
  bibliography_entry:
  verification_status:
```

### Figure/Table/Data Agent

```yaml
VisualPlan:
  figure_needed:
  figure_type:
  source_backed_claims:
  copyright_status:
  table_needed:
  data_analysis_needed:
  figure_legend:
```

### Essay Architect Agent

Tasks:

- draft from the approved plan;
- preserve word-count allocation;
- keep section sequence stable;
- make every paragraph's function visible;
- avoid adding unsupported content.

### Critical Thinking Agent

Tasks:

- check whether the discussion is mostly analytic;
- check whether the main body has at least 30 percent analytic material;
- flag descriptive catalogues;
- add or request limitation, model comparison, evidence boundary, and future-direction material where source-backed.

### Final QA Agent

Tasks:

- citation QA;
- word-count QA;
- hallucination QA;
- figure/table permission QA;
- overclaim QA;
- academic style QA;
- rubric fit QA.

## Integration Rule

Subagent results are inputs, not final truth. Before using them:

```yaml
SubagentAcceptanceCheck:
  sources_exist:
  identifiers_verified:
  claims_match_sources:
  uncertainty_labelled:
  output_matches_assigned_role:
  no_scope_drift:
```
