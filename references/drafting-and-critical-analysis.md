# Drafting And Critical Analysis

Use this reference after the requirement model, evidence map, and structure plan are ready, or when revising academic prose.

## Draft From The Plan

Use the structure plan as the drafting contract:

- thesis or central answer;
- task type, submission mode, and intended audience;
- scope and audience;
- section functions;
- evidence sources;
- citation strategy and confirmed citation quantity;
- figure, table, or data role;
- analysis tool, analysis method, and figure legend requirements when relevant;
- visual hierarchy, interaction requirements, or storyboard decisions for posters, presentations, and websites;
- output format and format requirements;
- approved or selected paragraph-level section plans with real paragraph labels;
- approved or selected critical-analysis moves and their planned insertion points.

Before drafting, confirm that the tutoring conversation has resolved:

- thesis direction or competing thesis options;
- evidence burden and expected citation density;
- citation quantity and citation style;
- format requirements, including default format or custom user instructions;
- critical stance and limits of the argument;
- lab-report analysis tool, statistical or model method, and analysis scope when results are involved;
- poster, presentation, website, figure, or figure legend task decisions when those formats are requested;
- section-by-section plan approval;
- critical-move-level CriticalAnalysisPlan selection after the paragraph plan has been reviewed;
- Planning Approval from the user after the final integrated plan is displayed;
- whether user-draft structure, paragraphs, phrasing patterns, or source choices should be preserved, revised, or replaced;
- output use, such as submission draft, revision notes, model answer, or DOCX file.

When new evidence changes the best answer, update the plan visibly before changing the direction of the draft.

When drafting or revising, make the writing choices traceable to the confirmed plan. Explain consequential structure, evidence, or revision decisions briefly when they affect the user's learning or approval; keep internal workflow metadata out of the final essay body.

## Approved Plan Writing

After the user approves the final integrated plan, the main agent proceeds directly into writing. Do not ask a second confirmation such as whether to start writing.

Before parallel writing, lock each section contract: heading, section function, paragraph role, evidence scope, citation density, critical-analysis move, transition role, output format, and any task-specific method, data, visual, interaction, or legend requirement. A subagent may draft only inside that locked section contract.

For lab reports, DataAnalysisAgent may run in parallel with IntroductionDraftAgent and MethodDraftAgent after the brief and section contracts are locked. ResultsDraftAgent and DiscussionDraftAgent must wait for DataAnalysisAgent output because those sections depend on verified result values, uncertainty, figures, tables, exclusions, and method notes.

Subagents must not change thesis, structure, citation strategy, evidence scope, analysis method, figure or table contract, format contract, or final language. If a subagent finds a plan-breaking issue after approval, it returns the issue to the main agent. The main agent then decides whether to continue within the approved plan, revise the plan, or use `scripts/build_intake_questions.py writing-gate` to ask the user for the required decision.

## Paragraph Logic

Use simple paragraph functions. A paragraph can follow one of these patterns:

```text
Claim -> Evidence -> Interpretation -> Boundary -> Link back
Evidence -> What it tests -> Result -> Meaning -> Boundary
Problem -> Comparison axis -> Evidence A -> Evidence B -> Evaluation
Method or data -> Why it matters -> Result -> Interpretation -> Caveat
```

Each paragraph should have a clear job. Choose the job before writing.

## Critical Analysis

Critical analysis means showing how evidence answers the question and how far the answer can be taken. Useful moves include:

- evidence strength: explain what the evidence supports most directly;
- boundary: state the population, method, context, period, or concept range;
- alternative explanation: identify a plausible competing interpretation and compare fit;
- causal calibration: match causal language to study design or data structure;
- mechanism comparison: compare mechanisms or explain why one mechanism is more relevant;
- method appraisal: explain how measurement, sampling, modelling, or task design affects interpretation;
- implication: state the theoretical, clinical, social, or methodological consequence.

Choose the move that best fits the paragraph's evidence and the assignment question.

Read `critical-writing-bank.md` when the task needs more critical stance, discussion depth, study evaluation, theory limits, method limits, or constructive suggestions. Use that bank as a set of reusable reasoning and language patterns. Adapt phrases to the topic rather than inserting generic templates.

Use this sequence for critical-writing sentences:

```text
evidence problem -> critical move -> source support -> interpretation -> thesis link
```

Examples of evidence problems include limited measurement, inconsistent results, weak causal inference, narrow population, dated evidence, untested mechanism, construct ambiguity, and a gap between theory and clinical practice.

Draft critical analysis from the user-selected critical moves in the approved `CriticalAnalysisPlan`, or from newly verified evidence that changes the best academic interpretation. Treat critical analysis as inserted evaluation inside the relevant body paragraphs and Discussion synthesis, with each evaluative move attached to a specific paragraph function, source, method, theory, mechanism, dataset, or interpretation.

## Density And Detail

Match detail to academic value:

- Define terms when the reader needs them to follow the argument.
- Explain mechanisms when they carry the reasoning.
- Summarise background when it only orients the reader.
- Expand evidence when its design, result, or limitation affects interpretation.
- Use tables or figures when comparison or structure becomes clearer visually.
- Use concise prose when a citation can support familiar context.

Effective density usually increases where the rubric rewards analysis, where evidence conflicts, where methods shape interpretation, or where data require careful explanation.

When a page or word limit is an upper bound, use remaining space for relevant detail that improves the answer: stronger mechanism explanation, closer source comparison, clearer evidence boundaries, more explicit critical interpretation, and better links back to the question.

## Section Guidance

## Non-Essay Text Blocks

For posters, presentations, interactive websites, figure generation tasks, and figure legends, draft from the task-specific workflow rather than forcing essay paragraphs into the output.

Use these text-block functions:

```text
Poster panel -> message -> evidence or visual -> interpretation -> link to takeaway
Slide -> single purpose -> visual or claim -> spoken explanation -> transition
Speaker note -> context -> explanation -> evidence boundary -> next slide cue
Website section -> user question -> interaction or content -> evidence -> next action
Figure legend -> what is shown -> data/source basis -> details for interpretation -> takeaway
Results text -> analysis purpose -> verified method -> result -> uncertainty -> meaning
```

Poster panels should use compact headings, readable text blocks, and captions or legends that carry interpretation without overcrowding the canvas. Slide text should be sparse and visual-led, with evidence and nuance moved into speaker notes or script when requested. Website copy should guide the user through the academic argument and make interactions explain evidence, comparison, or decisions. Figure legends should state what is shown, sample or source basis, groups or conditions, statistics and error bars when verified, units, scale bars, abbreviations, source or permission status, and the reader takeaway.

For lab-report results, write only from verified analysis output or a user-confirmed analysis plan. Keep the analysis tool and method visible in the result plan, and do not name a test, model, post hoc correction, or repeated-measures design unless it is supported by the brief, data analysis output, or the user's answer.

## Essay Structure

For essay tasks, use this default architecture unless the assignment brief gives a different structure:

```text
Abstract
Introduction
Main Body
  - named subsection based on argument function
  - named subsection based on argument function
  - named subsection based on argument function
Discussion
Conclusion
References
```

Use the abstract to summarise the final argument, evidence base, and conclusion. It can be drafted after the main argument is stable.

Use Main Body subsections to organise the central explanation, evidence, comparison, mechanism, or case analysis. Each subsection should have:

- a clear argument function;
- key claims;
- evidence basis;
- link to the central answer;
- citation-density target matched to the confirmed citation quantity;
- critical-analysis role matched to the approved paragraph-level SectionPlan;
- density matched to concept difficulty and evidence complexity.

### Introduction

Move from field context to the exact problem. Establish:

- relevant background;
- key concepts and definitions;
- gap, debate, uncertainty, or practical problem;
- why the question matters;
- thesis, aim, or central answer.

### Main Body

Organise by argumentative function rather than source order. Each subsection should advance the answer through mechanism, evidence, comparison, method, result, or implication.

### Results Or Data Sections

For data-supported reports, state:

- the analysis purpose;
- the sample or data basis;
- the statistical or descriptive output;
- direction and size of the result where available;
- uncertainty, correction, or model basis;
- figure or table link;
- what the result means for the research question.

### Discussion

Use the discussion to integrate the main body with the essay aim, literature, theory, limitations, alternatives, and future work. Prioritise interpretation over repetition of earlier sections.

In discussion-heavy essays, include critical moves that fit the evidence base:

- highlight inadequacies in previous studies when the field leaves a question unresolved;
- identify weaknesses in a single study or paper when a key source carries too much argumentative weight;
- evaluate theory or argument limits when the model explains some findings better than others;
- evaluate method or practice limits when design, measurement, sampling, timing, or intervention delivery affects interpretation;
- offer constructive suggestions when the next research or practice step follows from the limitation.

### Conclusion

Close by answering the question directly. Connect the strongest supported findings to the assignment aim and broader significance.

## Language Control

Use precise academic prose:

- Prefer concrete nouns and verbs over general prestige words.
- Use cautious verbs such as suggests, supports, is consistent with, indicates, or demonstrates according to evidence strength.
- Keep method, result, interpretation, and implication distinct.
- Use active, direct sentences when they improve clarity.
- Use parenthetical citations for claim-led prose unless author contrast matters.
- Keep source-route narration for places where the identity or design of the study matters.

## Revision Discipline

Use revision passes with a defined purpose:

1. **Question fit**: each section helps answer the prompt.
2. **Evidence fit**: each claim has suitable support.
3. **Analysis fit**: interpretation and boundaries are close to the evidence.
4. **Density fit**: detail matches rubric emphasis, evidence complexity, and reader need.
5. **Citation fit**: citations support the exact claims beside them.
6. **Language fit**: sentences are specific, coherent, and academically controlled.
7. **Tutor fit**: the revision reflects the agreed learning goal, preserves appropriate user ownership, and makes major changes explainable to the user.

When shortening, preserve the reasoning chain and compress lower-value orientation, repetition, or source-route prose first. Reallocate saved space to interpretation, comparison, evidence strength, scope, or link-back when the assignment benefits from it.

## Exemplar And Feedback Use

Use teacher edits and user-supplied exemplars to extract transferable behaviours:

- how directly the answer is stated;
- how much context is used before analysis;
- how sources are grouped;
- how figures and tables are introduced;
- how limitations are integrated;
- how conclusions close the argument.

Translate those behaviours into the new assignment while grounding topic claims in the current source base and using original phrasing.
