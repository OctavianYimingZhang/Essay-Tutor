# Visuals, Tables, And Data

Use this reference when an essay may include a figure, table, mechanism schematic, or data analysis.

## Decision Rule

Include a visual, table, or data figure only when it improves the argument.

Valid uses:

- mechanism schematic;
- model comparison;
- evidence summary;
- treatment comparison;
- method workflow;
- data result;
- limitation matrix.

Invalid uses:

- decoration;
- unsupported mechanism;
- copied lecture or paper layout;
- image used as evidence without source support;
- table that repeats prose without improving comparison.

## Academic Paper Figure Reuse

Citation alone is not permission to reproduce a figure.

Use a published figure only when at least one condition is met:

1. The article or figure has a compatible license such as CC BY.
2. The publisher's reuse terms permit the intended use.
3. Permission has been obtained.
4. The use is clearly limited to private study and not submitted or redistributed.
5. The user provided the image and confirms they have reuse rights.

Maintain:

```yaml
FigureReuseGate:
  source_paper:
  figure_number:
  licence:
    - CC_BY
    - CC_BY_NC
    - publisher_permission
    - user_provided_rights
    - unknown
  permission_status:
  can_reuse_directly:
  required_attribution:
  caption:
  bibliography_entry:
```

If the licence is unknown, do not reproduce the image. Create an original schematic instead.

## Generated Mechanism Figures

Use image generation or a BioRender-style schematic only after the written mechanism is source-backed.

Rules:

- Represent only claims already supported by accepted sources.
- Do not copy a paper, lecture, textbook, or private figure's layout.
- Do not introduce new labels, mechanisms, quantities, dates, or pathways.
- Keep labels traceable to sources.
- Include a figure legend.
- State that the figure is a generated schematic, not an official or reproduced figure.

Legend template:

```text
Figure 1. Generated schematic of [mechanism]. The figure summarises source-backed relationships between [A], [B], and [C]. It is an original schematic for writing support and is not reproduced from any published article or course material.
```

Internal spec:

```yaml
GeneratedFigureSpec:
  figure_id:
  type:
    - mechanism_pathway
    - process_sequence
    - comparison_framework
    - method_workflow
  source_backed_claims:
  labels:
  forbidden_elements:
  generation_prompt:
  legend:
  alt_text:
  qa_flags:
```

## Data Figures

When the user provides data or the essay requires original analysis, use a transparent data workflow.

```yaml
DataFigureWorkflow:
  input:
    - raw_data
    - variable_description
    - groups
    - statistical_question
    - required_graph_type
  preprocessing:
    - check missing values
    - identify exclusion rules before analysis
    - avoid post-hoc outlier removal unless method is specified
  analysis:
    - choose statistical test
    - justify assumptions
    - report effect size when possible
    - report confidence interval when possible
  graphing:
    - use GraphPad Prism when available and appropriate
    - otherwise use a reproducible statistical or plotting environment
  output:
    - figure
    - figure legend
    - statistical note
    - methods sentence
```

GraphPad Prism integration rules:

- Use Prism for final data figures when it is available and the graph type suits Prism.
- Use Prism scripts, templates, or PZFX workflows only through official Prism functionality or license-compatible automation.
- Do not copy third-party GraphPad automation Skill code into this Skill unless its license permits reuse.
- If Prism is unavailable, use an auditable local analysis workflow and state that Prism output was not generated.

## Academic Tables

Use table formatting suitable for an academic paper:

```yaml
TableRules:
  style:
    - no_vertical_lines
    - top_rule
    - header_rule
    - bottom_rule
    - concise_caption_above
    - abbreviation_note_below
  content:
    - include only information used in the argument
    - cite sources in table body or caption
    - use comparable categories across rows
```

Useful table types:

- competing models comparison;
- evidence strength summary;
- treatment comparison;
- mechanism versus evidence matrix;
- clinical intervention summary;
- limitations matrix.

Before final output, verify that the prose refers to the table and interprets it. A table not used by the argument should be removed.
