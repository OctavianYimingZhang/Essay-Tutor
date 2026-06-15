# Research And Citation

Use this reference for source selection, evidence mapping, citation placement, metadata checking, and reference-list handling.

## Source Selection

Prefer sources that are reliable, traceable, relevant to the claim, and suitable for the assignment level.

Use this source order as a guide:

1. Assignment question, rubric, learning outcomes, and local style guidance.
2. Official lecture slides, official notes, handouts, and required readings.
3. User-provided papers, datasets, analysis outputs, and teacher feedback.
4. Primary peer-reviewed studies for specific empirical claims.
5. Systematic reviews, meta-analyses, major reviews, textbooks, and guidelines for synthesis or orientation.
6. Additional peer-reviewed literature found through academic search.
7. Informal summaries, student notes, encyclopaedic pages, and exemplars as orientation clues that prompt independent verification.

Select sources by asking:

- Does this source directly support the sentence-level claim?
- Is the source type appropriate for the claim strength?
- Are the author, title, year, venue, DOI, PMID, URL, or edition verifiable?
- Does the source belong in the assignment's expected evidence base?
- Would a stronger primary, review, textbook, guideline, or course source support the point more cleanly?

## Evidence Map

Build a compact evidence map before drafting claim-heavy sections:

```yaml
EvidenceMap:
  claim:
  source:
  source_type:
  evidence_role:
  strength:
  boundary:
  citation_form:
  section:
```

Use `evidence_role` values such as background, method, empirical result, theory, counterpoint, limitation, comparison, definition, or data output.

## Research Workflow

For literature-backed work, deconstruct the topic into:

```yaml
ResearchMap:
  task_terms:
  key_concepts:
  assignment_sources:
  course_sources:
  primary_sources:
  synthesis_sources:
  competing_views:
  evidence_boundaries:
  useful_figures_tables_or_data:
```

Search through academic routes where available: PubMed, Google Scholar, Crossref, DOI.org, publisher pages, official guidelines, library databases, or course-provided links.

## Citation Placement

Use claim-led citation prose by default. Put the claim first and place the citation where it supports that claim.

Preferred:

```text
Hydrogen bonding can stabilise protein folds when buried in favourable structural contexts (Pace et al., 2014).
```

Author-led prose is useful when the study design, disagreement between authors, or historical development is part of the argument.

Use citations for:

- non-obvious factual, mechanistic, theoretical, clinical, methodological, or empirical claims;
- definitions that are discipline-specific;
- data, statistics, and results;
- claims about prior literature, models, or debates;
- course-specific claims when the source is a lecture, handbook, or assigned reading.

## Citation Modes

Use both modes when useful:

- **Close evidence citation**: one source supports one precise claim, result, method, or definition.
- **Synthesis citation**: several sources support a broader pattern, contrast, or state of the field.

For synthesis citations, keep the sentence specific enough that all cited sources genuinely contribute.

## Metadata And Reference List

Before final output, check:

```yaml
CitationRegistry:
  in_text_citation:
  reference_entry:
  source_metadata_verified:
  claim_supported:
  style_matches_assignment:
```

Format references according to the requested style or local style guide. When the assignment uses a named style such as Manchester Harvard, APA, Vancouver, Chicago, MLA, AMA, or IEEE, follow that style consistently across in-text citations and the reference list.

When metadata is incomplete, use a source lookup step before finalising the citation.

## Citation Tooling

Use available tools where they improve accuracy:

- Zotero or another citation manager for library-backed references.
- Crossref, DOI.org, PubMed, publisher pages, or library pages for metadata verification.
- CSL-compatible formatters for style rendering.
- Course materials for local citation or formatting preferences.

Treat generated citation strings as drafts until checked against the assignment style.
