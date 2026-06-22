# Subagents

Use this reference only after the task has a locked brief and the work benefits from independent bounded passes. If real subagents are unavailable, execute the roles sequentially with the same output discipline.

## Main-Agent Gates

Requirement/rubric/brief gate: the main agent must complete material diagnosis, requirement extraction, rubric interpretation, `AssignmentBrief` locking, and plan-changing Ask User decisions before any subagent starts.

Interactive tasks remain with the main agent. Do not delegate Ask User, requirement clarification, rubric clarification, user preference confirmation, Planning Approval, writing gate decisions, approval after a plan change, or any question that changes task type, thesis, structure, citation strategy, format contract, analysis method, visual hierarchy, or output form.

Subagents may run only after the brief is locked. They may not unlock or relock the brief, approve a plan, ask the user, or make independent changes to the approved thesis, structure, citation strategy, section contract, format contract, analysis method, data interpretation, visual contract, or figure legend contract.

If a subagent finds a plan-breaking issue, it returns a short escalation note to the main agent with the affected requirement, evidence, and decision needed. The main agent decides whether to use Ask User or the `writing-gate` payload.

## Delegation Principles

- Assign one bounded role per agent.
- Give each agent the minimum source material and an evidence-bound output shape.
- Ask for findings, maps, checks, section-constrained draft text, or options rather than final ownership of the full coursework.
- Verify outputs before adding claims, citations, figures, statistics, or interpretations to the final work.
- Use subagents only when they improve accuracy, coverage, speed, or reliability for non-interactive work.

## Allowed Roles

### EvidenceRetrievalAgent

```yaml
EvidenceMap:
  claim_or_topic:
  source:
  source_type:
  identifier:
  relevance:
  boundary:
  section_use:
  citation_metadata_status:
```

### EvidenceAppraisalAgent

```yaml
EvidenceAppraisal:
  claim:
  strongest_support:
  evidence_type:
  strength:
  boundary:
  suitable_wording:
  plan_breaking_issue:
```

### DataAnalysisAgent

```yaml
DataAnalysisOutput:
  data_basis:
  analysis_tool:
  analysis_method:
  cleaning_or_exclusion_notes:
  result_values:
  uncertainty_or_statistics:
  figure_or_table_destinations:
  limitations:
  plan_breaking_issue:
```

### IntroductionDraftAgent

```yaml
SectionDraft:
  section: Introduction
  contract_used:
  draft_text:
  claims_requiring_citations:
  unresolved_evidence:
  plan_breaking_issue:
```

### MethodDraftAgent

```yaml
SectionDraft:
  section: Method
  contract_used:
  draft_text:
  verified_method_details:
  unsupported_method_details:
  plan_breaking_issue:
```

### ResultsDraftAgent

```yaml
SectionDraft:
  section: Results
  dependency: DataAnalysisAgent output
  contract_used:
  draft_text:
  result_values_used:
  figure_or_table_links:
  plan_breaking_issue:
```

### DiscussionDraftAgent

```yaml
SectionDraft:
  section: Discussion
  dependency: DataAnalysisAgent output and approved critical-analysis plan
  contract_used:
  draft_text:
  interpretation_boundaries:
  critical_moves_used:
  plan_breaking_issue:
```

### CitationIntegrityAgent

```yaml
CitationCheck:
  citation:
  reference_entry:
  metadata_status:
  claim_supported:
  style_note:
  unsupported_or_missing_source:
```

### VisualDataAgent

```yaml
VisualDataCheck:
  item:
  purpose:
  data_or_source_basis:
  analysis_tool:
  analysis_method:
  labels_units_statistics:
  figure_legend_requirements:
  caption_takeaway:
  source_or_permission_status:
  fit_to_assignment:
  plan_breaking_issue:
```

### FinalQAAgent

```yaml
FinalQA:
  requirement_fit:
  evidence_fit:
  structure_fit:
  citation_fit:
  density_fit:
  formatting_fit:
  priority_revisions:
```

## Dependency Order

Use parallel subagents only for work that is independent under the locked brief and section contract. For a lab report, DataAnalysisAgent may run in parallel with IntroductionDraftAgent and MethodDraftAgent after the brief and section contracts are locked because those sections can use the confirmed aim, source base, and method contract. ResultsDraftAgent and DiscussionDraftAgent must wait for DataAnalysisAgent output because results wording and discussion interpretation depend on verified values, uncertainty, figures, tables, exclusions, and method notes.

For essays and literature reviews, EvidenceRetrievalAgent and EvidenceAppraisalAgent may run in parallel on different source clusters after the brief is locked. Section draft agents may run in parallel only when the main agent has already locked each section's heading, function, paragraph role, evidence scope, citation density, critical move placement, and transition contract.

## Integration

Integrate subagent findings through the main evidence map and structure plan. Prefer the most verifiable, assignment-relevant findings, and resolve conflicts by returning to the rubric, brief, data, and source evidence. The main agent remains responsible for final plan integrity, user interaction, writing approval, citation acceptance, data interpretation, and final delivery.
