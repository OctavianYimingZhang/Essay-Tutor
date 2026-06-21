# Subagents

Use this reference after the task has a clear requirement model and the work benefits from independent bounded passes. If real subagents are unavailable, execute the roles sequentially with the same output discipline.

## Delegation Principles

- Assign one bounded role per agent.
- Give each agent the minimum source material and an evidence-bound output shape.
- Ask for findings, maps, checks, or options rather than final ownership of the same prose.
- Verify outputs before adding claims, citations, figures, statistics, or interpretations to the final work.

## Useful Roles

### Requirement And Rubric Agent

```yaml
RequirementMap:
  task_type:
  command_verbs:
  rubric_priorities:
  expected_sections:
  evidence_needed:
  output_requirements:
  examiner_fit_notes:
```

### Evidence Retrieval Agent

```yaml
EvidenceMap:
  claim_or_topic:
  source:
  source_type:
  identifier:
  relevance:
  boundary:
  section_use:
```

### Evidence Appraisal Agent

```yaml
EvidenceAppraisal:
  claim:
  strongest_support:
  evidence_type:
  strength:
  boundary:
  suitable_wording:
```

### Structure Agent

```yaml
StructureReview:
  thesis_or_central_answer:
  section_functions:
  density_choices:
  evidence_distribution:
  missing_reader_context:
  opportunities_to_compress:
```

### Citation Agent

```yaml
CitationCheck:
  citation:
  reference_entry:
  metadata_status:
  claim_supported:
  style_note:
```

### Figure, Table, And Data Agent

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
```

### Final QA Agent

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

## Integration

Integrate subagent findings through the main evidence map and structure plan. Prefer the most verifiable, assignment-relevant findings, and resolve conflicts by returning to the rubric, brief, data, and source evidence.
