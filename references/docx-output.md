# DOCX Output

Use this reference only when the user asks for a Word document, DOCX file, or formatted essay file.

## File Creation Rule

Do not create files unless the user asks for a file output or a Word document.

When the user requests DOCX, generate a document that does not require manual reformatting.

## Default Essay DOCX Format

Apply these settings unless the user specifies otherwise:

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

## Structure

Default structure:

```text
Title
Optional essay question
Introduction
Main body sections and subtitles
Discussion when appropriate
Conclusion
References
Figure legends if figures are included
Tables where requested or useful
```

Number headings only when useful or required.

## Implementation Guidance

Use a DOCX library or existing document tool that can set:

- section margins;
- paragraph alignment;
- line spacing;
- font family;
- heading styles;
- captions;
- table borders.

For generated tables:

- avoid vertical borders;
- use top, header, and bottom horizontal rules;
- place caption above;
- place notes below.

For figures:

- include only licensed, permitted, user-owned, or generated original figures;
- include a caption and source/permission note where needed.

## DOCX QA

Before delivery, check:

```yaml
DOCXQA:
  file_opens:
  margins_are_2_5_cm:
  font_is_arial:
  line_spacing_is_1_5:
  body_text_is_justified:
  title_is_centered:
  subheadings_are_left_aligned:
  references_present_when_citations_used:
  figures_have_captions:
  tables_have_academic_rules:
```

If any formatting check fails, fix the document before final response.
