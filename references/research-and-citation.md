# Research And Citation

Use this reference for literature search, source validation, citation placement, and bibliography formatting.

## Evidence Hierarchy

Use this source order:

1. Essay question, rubric, and learning outcomes.
2. Official lecture slides, official notes, and official handouts.
3. Required readings and reading-list papers.
4. Primary peer-reviewed papers.
5. Systematic reviews, meta-analyses, major reviews, and clinical guidelines.
6. Textbook chapters and publisher or official academic pages.
7. Extra peer-reviewed papers found by academic search.
8. Student notes, AI notes, informal summaries, and exemplars only as clues until verified.

Rules:

- Do not use unverified source metadata.
- Do not cite a review as primary experimental evidence.
- Do not convert associative evidence into causal proof.
- Do not use source-route narration in the essay body.
- Omit unsupported claims rather than inventing support.

## Source Exclusions

Do not rely on:

- unproven traditional medicine claims;
- influencer content;
- corporate PR or marketing claims unless the assignment is specifically about corporate communication and the claim is identified as corporate self-description;
- Q&A platforms, social media, content farms, or unsourced blogs;
- Wikipedia except for basic orientation before independent verification.

## DeepResearch Workflow

For each topic, build:

```yaml
ResearchMap:
  topic_deconstruction:
  key_terms:
  search_queries:
  seminal_sources:
  recent_sources:
  primary_evidence:
  reviews_for_orientation:
  competing_models:
  contradictory_findings:
  methodological_limits:
  theory_or_clinical_implications:
  visual_or_table_opportunities:
  excluded_sources:
```

Prefer PubMed, Google Scholar, Crossref, DOI.org, publisher pages, official guidelines, and university library-accessible sources where available.

Plan-stage citation rule:

- Use exact author-year, DOI, PMID, title, journal, or "recent review" claims only after verification.
- If a source has not been verified, label it as `candidate_source` and state what it is expected to support.
- Do not let candidate sources appear in the final draft, reference list, or DOCX until metadata and claim relevance are checked.

## Citation Modes

Use both modes when the assignment needs literature-backed writing.

### Intensive-reading citation

Use when one paper needs close interpretation:

```text
one sentence, several sentences, or one paragraph cite one core paper
```

Suitable for:

- primary experiments;
- landmark models;
- clinical trials;
- mechanism papers;
- paper-specific methodological limitations;
- evidence strength evaluation.

Write the source's function, not just its finding:

```text
This study supports X because its design isolates Y, but it does not establish Z because...
```

### Broad-support citation

Use when several papers support the same synthesis claim:

```text
one summary sentence cites several sources
```

Suitable for:

- field consensus;
- converging findings;
- prevalence or treatment evidence;
- broad model support.

Limitations:

- Avoid citation stacking.
- Every cited source must support the same sentence-level claim.
- Do not use several weakly connected papers to decorate a vague sentence.

## Citation Metadata

For each source used in the essay, maintain:

```yaml
CitationRecord:
  citation_key:
  source_type:
  title:
  authors:
  year:
  journal_or_publisher:
  DOI:
  PMID:
  URL:
  identifier_verified:
  metadata_matches_claim:
  claim_supported:
  citation_mode:
    - intensive_reading
    - broad_support
    - review_context
    - primary_evidence
  essay_location:
  bibliography_entry:
```

## Citation Tooling

Do not scrape or copy MyBib. Treat it only as a manual style reference when useful.

Preferred implementation pattern:

```yaml
CitationSubsystem:
  metadata_discovery:
    - PubMed
    - Crossref
    - DOI.org
    - publisher pages
    - Google Scholar for discovery only
  metadata_validation:
    - DOI resolves
    - PMID matches
    - title-author-year match
    - source supports the claim
  formatting_engine:
    - CSL-compatible formatter
    - Citation.js when available
    - Zotero-compatible CSL style files when available
  optional_external_tools:
    - Scholar Sidekick MCP for DOI/PMID/arXiv/ISBN resolution and CSL-style formatting when configured
    - citation-management Skill for discovery, metadata extraction, BibTeX cleanup, and validation when installed and license-compatible
```

Before vendoring any third-party script, check its license. If license status is unclear, invoke it externally or document the integration instead of copying code.

## Citation QA

Every citation must pass:

```yaml
CitationQA:
  source_exists: true
  identifier_verified: true
  metadata_matches_source: true
  metadata_matches_claim: true
  claim_strength_calibrated: true
  in_text_and_reference_list_match: true
  no_unread_source_cited_as_primary: true
```

Allowed verbs depend on evidence strength:

```yaml
EvidenceVerbCalibration:
  direct_experimental_causal_evidence:
    - demonstrates
    - shows
  consistent_or_partial_evidence:
    - supports
    - implicates
    - is consistent with
  associative_or_observational_evidence:
    - is associated with
    - suggests
    - is compatible with
  review_or_theory_evidence:
    - proposes
    - synthesises
    - frames
```

Use stronger verbs only when the verified source warrants them.

## Reference List Rules

- Match the user's requested citation style.
- If no style is specified, ask only when final drafting or DOCX output depends on it; otherwise mark it as pending.
- Include every in-text citation in the reference list.
- Remove uncited reference-list entries unless the user asks for a bibliography of further reading.
- For journal-specific styles, use official author instructions or CSL styles where available.
