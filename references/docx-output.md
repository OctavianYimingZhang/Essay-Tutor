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
    title_font_size: user-selected value; default to 14 pt main title when not otherwise specified
    color: black unless assignment material explicitly requires another colour
  paragraph:
    line_spacing: 1.5
    body_alignment: justified
    title_alignment: centered
    subheading_alignment: left
  headings:
    main_title: centered
    main_title_size: user-selected title_font_size; default 14 pt
    subheadings: left_aligned
    color: black unless assignment material explicitly requires another colour
  references:
    style: requested citation style
  figures:
    caption_position: below figure
  tables:
    caption_position: above table
    style: Nature-style journal table with black text, compact editable cells, minimal horizontal rules, concise title, and symbol or abbreviation notes below
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

Make the document body submit-ready and assignment-facing. The file should open as a polished academic draft the user can revise for content, with body text, headings, figures, tables, citations, and references already in the requested or default format. Workflow notes, planning metadata, and process records belong in the conversation or internal planning record unless the assignment explicitly asks for them.

For DOCX, Word, LaTeX, or formatted file output, first display the planned document format, then ask the user about typography, font size, margins, line spacing, title style, and reference formatting with `scripts/build_intake_questions.py docx-format` or `scripts/build_intake_questions.py document-format` unless the brief or style guide already specifies those details. Use `14 pt main title` as the default title-size choice for DOCX when the user accepts the default academic format or does not provide a custom title-size preference.

## Implementation Guidance

Use a DOCX library, document tool, or existing office application workflow that can set:

- section margins;
- paragraph alignment;
- line spacing;
- font family;
- body font size;
- main title font size;
- title alignment and title style;
- reference-list formatting;
- heading styles;
- captions;
- table borders;
- page breaks where they improve document structure.

Set the default body style and all heading styles to black academic text for essay-style Word outputs unless the assignment explicitly supplies another visual style. Apply the heading colour explicitly so Word's built-in theme colours do not change the academic appearance.

For generated tables, use a Nature-style journal table format: short descriptive title above the table, compact editable rows, black text, restrained horizontal rules such as top rule, header rule, and bottom rule, portrait-friendly width, and explanatory notes below for symbols, abbreviations, statistical notation, units, or source details. Keep colour fills, decorative borders, and oversized typography out of the academic table style.

For figures, include a caption and source, authorship, permission, or data note when relevant.

## DOCX QA

Before delivery, run a visual format check:

1. Inspect document structure and styles: page size, margins, font family, body alignment, line spacing, heading colour, citation/reference formatting, section breaks, and page breaks.
2. Render the DOCX to page images when rendering tools are available.
3. Inspect all pages or representative pages plus the first and last page for clipping, overlap, excessive blank space, unexpected blank pages, heading colour, font substitution, broken reference wrapping, table/figure placement, and page-limit fit.
4. Fix the DOCX and re-render after any formatting correction.

Use this checklist during the same pass:

```yaml
DOCXQA:
  latest_text_used:
  submit_ready_academic_body:
  requested_format_applied:
  title_font_size_applied:
  citations_and_references_match:
  figures_and_tables_have_captions:
  captions_near_items:
  headings_consistent:
  body_text_readable:
  black_academic_text_when_required:
  internal_metadata_kept_in_workflow:
  black_heading_style_applied:
  nature_style_academic_tables:
  no_excessive_spacing_or_blank_final_pages:
  page_or_word_limit_fit:
  exported_pdf_matches_docx_when_pdf_requested:
```

If rendering tools are unavailable, perform structural DOCX checks and state that visual render QA was not completed.
