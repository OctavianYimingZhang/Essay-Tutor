# DOCX Output

Use this reference when the user asks for a Word document, DOCX file, PDF-from-DOCX, or formatted academic file.

## Output Contract

Create document files when the user asks for a file output or when Word/DOCX/PDF formatting is part of the task. Use the latest draft and verified reference list as the document source.

## Default Academic DOCX Format

Apply these settings unless the assignment, local style guide, or user request gives a different instruction:

```yaml
DOCXFormat:
  page:
    margins: 2.5 cm on all sides
  font:
    family: Arial
    size: Word default unless specified
  paragraph:
    line_spacing: 1.5
    body_alignment: justified
    title_alignment: centered
    subheading_alignment: left
  headings:
    main_title: centered
    subheadings: left_aligned
  references:
    style: requested citation style
  figures:
    caption_position: below figure
  tables:
    caption_position: above table
  other_settings: default
```

## Document Structure

Build the structure that fits the assignment type:

- title page or title block where expected;
- abstract or summary where requested by the brief or discipline;
- for essay tasks: Abstract, Introduction, Main Body with named subsections, Discussion, Conclusion, and References where sources are used;
- for report tasks: introduction, methods, results, discussion, conclusion, or other sections requested by the brief;
- references or bibliography;
- figures, tables, captions, notes, and appendices where useful or requested.

Use headings that help the reader navigate the argument or report. Number headings when the assignment, discipline, or document length makes numbering useful.

## Implementation Guidance

Use a DOCX library, document tool, or existing office application workflow that can set:

- section margins;
- paragraph alignment;
- line spacing;
- font family;
- heading styles;
- captions;
- table borders;
- page breaks where they improve document structure.

For generated tables, prefer clean academic rules: top rule, header rule, bottom rule, caption above, and notes below when needed.

For figures, include a caption and source, authorship, permission, or data note when relevant.

## DOCX QA

Before delivery, check:

```yaml
DOCXQA:
  latest_text_used:
  requested_format_applied:
  citations_and_references_match:
  figures_and_tables_have_captions:
  captions_near_items:
  headings_consistent:
  body_text_readable:
  exported_pdf_matches_docx_when_pdf_requested:
```

Inspect the generated file or exported PDF when possible, especially after adding figures, tables, page breaks, or references.
