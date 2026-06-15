# Visuals, Tables, And Data

Use this reference when a task may include figures, tables, raw data, statistical output, GraphPad Prism files, spreadsheets, diagrams, or visual explanation.

## Communication Choice

Choose a visual, table, or data display when it improves one of these functions:

- compare evidence, groups, models, conditions, or outcomes;
- show a mechanism, pathway, timeline, workflow, or study design;
- summarise a literature pattern or limitation matrix;
- make data trends, uncertainty, or effect direction easier to inspect;
- present methods or results more clearly than prose alone.

Use prose when the information is simple, linear, or better handled by a short explanation and citation.

## Figure Planning

For any figure, define:

```yaml
FigurePlan:
  purpose:
  source_or_data_basis:
  panel_structure:
  labels_needed:
  caption_claim:
  permission_or_authorship:
  citation_or_data_link:
```

A strong figure caption states what the reader should learn, identifies the source or data basis, and explains symbols, units, sample sizes, or abbreviations needed for interpretation.

## Published Figure Use

Published figures are suitable when reuse rights, assignment context, and attribution are clear. Check:

- licence or permission status;
- whether the user owns or supplied the image;
- whether the intended use is private study, submitted coursework, publication, or redistribution;
- whether an original schematic would communicate the idea more appropriately.

When reuse is uncertain, create an original schematic based on verified claims and cite the sources behind the content.

## Generated Or Original Schematics

Use generated or original figures for mechanisms, conceptual models, workflows, and summaries when the content is source-backed.

Maintain traceability:

```yaml
SchematicSpec:
  concept:
  claims_represented:
  sources:
  labels:
  caption:
```

Keep labels and relationships tied to accepted sources or user-provided data.

## Data Analysis And GraphPad-Style Workflow

For data-supported assignments, use the authoritative analysis source available for the task:

- supplied statistical output;
- GraphPad Prism project or exported results;
- spreadsheet calculations;
- scripts run in the current workspace;
- course-provided analysis instructions.

Before writing results, extract:

```yaml
AnalysisRecord:
  analysis_name:
  data_source:
  sample_or_row_basis:
  exclusions_or_cleaning_applied:
  test_or_model:
  factors_or_variables:
  correction_or_posthoc_method:
  descriptive_statistics:
  inferential_statistics:
  units:
  figure_or_table_destination:
```

Preserve sample sizes, degrees of freedom, test statistics, p values, estimates, uncertainty measures, and units exactly as supported by the authoritative output.

When multiple analysis sources disagree, treat the assignment instructions and authoritative software output as the starting point, then record the discrepancy before drafting final results.

## Data Figures

Design data figures around the reader's comparison task:

- group related conditions visually;
- show uncertainty measures requested by the course or discipline;
- label axes with variable names and units;
- use legends or direct labels for groups;
- show statistical annotations when they help interpret the reported test;
- match caption claims to the analysis output.

For lab reports, cite the figure in the text before or near the interpretation and describe the direction and relevance of the result in prose.

## Tables

Use tables for compact comparison, methods, descriptive statistics, inferential outputs, source summaries, or limitation matrices.

A useful academic table has:

- a specific title;
- clear row and column labels;
- units and abbreviations;
- consistent precision;
- notes for corrections, sample size, or source basis;
- only the rows and columns needed for the reader's task.

Place table captions according to the requested style or document convention.
