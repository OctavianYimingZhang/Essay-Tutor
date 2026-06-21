# Visuals, Tables, And Data

Use this reference when a task may include figures, tables, raw data, statistical output, GraphPad Prism files, R Studio, Python, MatLab, spreadsheets, diagrams, figure generation, figure legends, posters, presentations, interactive websites, or visual explanation.

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
  claims_represented:
  panel_structure:
  visual_style:
  labels_needed:
  units_scales_or_abbreviations:
  generation_or_editing_tool:
  output_format:
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
  panel_structure:
  labels:
  visual_style:
  generation_or_editing_tool:
  caption:
  legend_requirements:
```

Keep labels and relationships tied to accepted sources or user-provided data.

## Data Analysis Workflow

For data-supported assignments, use `scripts/build_intake_questions.py lab-analysis` before writing results unless the analysis tool, analysis method, and analysis scope are already verified. Use the authoritative analysis source available for the task:

- supplied statistical output;
- GraphPad Prism project or exported results;
- R Studio scripts, console output, knitted reports, or exported tables;
- Python scripts, notebooks, logs, or exported tables;
- MatLab scripts, live scripts, command-window output, or exported tables;
- spreadsheet calculations;
- SPSS, Jamovi, JASP, or other user-specified software output;
- scripts run in the current workspace;
- course-provided analysis instructions.

Before writing results, extract:

```yaml
AnalysisRecord:
  analysis_name:
  analysis_tool:
  data_source:
  sample_or_row_basis:
  exclusions_or_cleaning_applied:
  test_or_model:
  analysis_method_verified_from:
  factors_or_variables:
  correction_or_posthoc_method:
  descriptive_statistics:
  inferential_statistics:
  units:
  figure_or_table_destination:
```

Preserve sample sizes, degrees of freedom, test statistics, p values, estimates, uncertainty measures, and units exactly as supported by the authoritative output.

Do not infer the statistical test or model from topic wording alone. Use methods such as two-way repeated-measures ANOVA only when the brief, the supplied output, the dataset design after explicit user discussion, or the user's direct answer verifies that method.

When multiple analysis sources disagree, treat the assignment instructions and authoritative software output as the starting point, then record the discrepancy before drafting final results.

For lab reports, connect each analysis to the research question, method, result text, figure or table destination, and discussion interpretation. If the user wants analysis help before output exists, plan the analysis method separately and mark unverified statistics as open items rather than writing results.

## Data Figures

Design data figures around the reader's comparison task:

- group related conditions visually;
- show uncertainty measures requested by the course or discipline;
- label axes with variable names and units;
- use legends or direct labels for groups;
- show statistical annotations when they help interpret the reported test;
- match caption claims to the analysis output.

For lab reports, cite the figure in the text before or near the interpretation and describe the direction and relevance of the result in prose.

## Figure Generation

Use `scripts/build_intake_questions.py figure-plan` when the figure purpose, source basis, or generation tool is not locked. Figure generation may use BioRender-style diagrams, image generation, image editing, plotting software, presentation tools, or user-specified software, but the scientific claims must remain source-backed.

Before creating or specifying a figure, build:

```yaml
FigureGenerationSpec:
  figure_purpose:
  source_or_data_basis:
  claims_represented:
  panel_structure:
  labels_units_scales_abbreviations:
  visual_style:
  generation_or_editing_tool:
  output_format:
  citation_or_permission_note:
```

Prefer editable, labelled, source-traceable figures for coursework. Use generated imagery only when it improves the assignment and when all represented mechanisms, relationships, conditions, or data patterns are grounded in verified sources or user-provided data.

## Figure Legends

Use `scripts/build_intake_questions.py figure-legend` when the legend depth, statistical detail, or source note is not locked. A complete legend should let the reader understand the figure without guessing the experimental or source basis.

```yaml
FigureLegendSpec:
  figure_number_or_title:
  what_is_shown:
  reader_takeaway:
  panel_descriptions:
  sample_or_data_basis:
  groups_conditions_or_variables:
  statistics_and_error_bars:
  units_scale_bars_and_abbreviations:
  source_authorship_or_permission:
```

Match figure legends to the figure type:

- data figures: include sample basis, test or model, error bars, p values or statistical annotations, units, and exclusions when verified;
- mechanism schematics: explain symbols, arrows, relationships, and source-backed claims;
- posters and presentations: keep legends readable and concise while preserving the key result, source basis, and abbreviations;
- standalone figure-generation tasks: include panel descriptions, source notes, and any permission or authorship status needed for submission.

Do not invent sample sizes, statistical tests, error bars, scale bars, abbreviations, source status, or permissions. If those details are absent, ask the user or mark the legend requirement as unresolved.

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
