---
name: essay-tutor
description: Academic essay workflow for interactive ask-user intake, Plan Mode-aware essay planning, deep research, plan approval, subagent research, citation-controlled drafting, critical analysis, figures, tables, data analysis, DOCX formatting, and final QA. Use when the user asks to plan, research, outline, draft, revise, cite, format, or produce an academic essay, model essay, literature-backed argument, discussion section, figure/table plan, or Word essay document.
---

# Essay Tutor

Use this Skill to turn an essay request into a controlled academic-writing workflow:

```text
UserRequest
-> EssaySkillConfig
-> InputReadinessReport
-> DeepResearch
-> TutorPlanningLoop
-> DecisionCompleteEssayPlan
-> UserApproval
-> SubagentResearch
-> EssayDraft
-> CitationFigureTableQA
-> FinalOutput
```

Do not generate a complete final essay before the user approves the plan unless the user explicitly asks to skip planning.

## Operating Rules

- Before a detailed plan, collect every requirement that affects essay scope, evidence, format, citation, language, or output. Do not guess, default, preselect, or predict user intent for missing requirements.
- Ask the user for any information that cannot be verified from the prompt, uploaded material, course material, or local files. Prefer native `request_user_input` / ask-user UI for material requirement and plan decisions when that capability is available.
- Use one to three meaningful choices per ask-user turn when possible. Each choice must represent a real academic or workflow tradeoff, not filler.
- Teach while planning: briefly explain why each user decision affects scope, evidence, citation density, structure, or final output.
- Use native Codex Plan Mode when it is active. In Plan Mode, do not emit the official final essay plan until all open decisions are resolved; wrap the final decision-complete plan in a `<proposed_plan>` block.
- Do not claim that this Skill can force Codex into Plan Mode. If Plan Mode or ask-user UI is unavailable, run the same tutor-style planning loop in normal chat and wait for explicit approval before drafting.
- Do not produce a detailed plan while required user decisions remain open.
- Treat the approved plan as the drafting contract. After approval, do not change the thesis, section logic, or scope unless the user authorizes the change.
- Use source evidence before prose. Do not invent citations, statistics, dates, mechanisms, quotations, source names, lecturer preferences, or rubric expectations.
- Label plan-stage citations as candidate unless their metadata and claim relevance have already been verified. Do not present exact paper claims, dates, or "recent review" assertions as verified from memory.
- Prefer official course material and required readings when supplied. Use external papers to sharpen the argument, not to replace the user's assignment scope.
- Separate descriptive and analytic writing. The main body should contain at least 30 percent analytic material; the discussion should be mostly analytic.
- Use citations for non-obvious factual, mechanistic, theoretical, clinical, quantitative, methodological, or experimental claims.
- Use direct academic paper figures only when reuse is licensed or permitted. Citation alone is not permission.
- Create DOCX files only when the user asks for a file or Word output.
- Keep final Skill/repository content in English.

## Workflow

1. **Intake and readiness**
   - Read `references/intake-and-planning.md`.
   - Build `EssaySkillConfig` and `InputReadinessReport`.
   - Run the Interactive Intake Gate. Confirm the essay question, academic level, word or page limit, citation style, output format, final language, source base, and rubric or marking standard before detailed planning.
   - Use the Ask User Tool Gate when available. Ask one to three concrete user-decision questions per turn until the gate is complete.

2. **Deep research and plan**
   - Read `references/research-and-citation.md`.
   - Search and verify enough source material to support a detailed plan.
   - Run the Tutor Planning Loop before the final plan: explain tradeoffs, ask targeted plan decisions, and progressively lock thesis, scope, structure, citation strategy, figure/table/data strategy, and critical-thinking targets.
   - Produce a decision-complete plan only after open user decisions are empty.

3. **Approval loop**
   - In Plan Mode, present the decision-complete plan in a `<proposed_plan>` block. Outside Plan Mode, present the same final plan in normal chat.
   - Wait for the user to modify or approve the plan.
   - Revise only the requested plan components and include a concise change log.
   - Start full drafting only after the user says "Approve Plan" or an equivalent approval.

4. **Subagent research after approval**
   - Read `references/subagents.md`.
   - Use real subagents when available and appropriate; otherwise execute the roles sequentially.
   - Keep outputs evidence-bound and verify subagent claims before using them.

5. **Drafting and critical analysis**
   - Read `references/drafting-and-critical-analysis.md`.
   - Draft from the approved plan and verified sources.
   - Make every substantive paragraph perform a clear claim, evidence, interpretation, limitation, and link-back function.

6. **Citation, figure, table, and data handling**
   - For citations, use `references/research-and-citation.md`.
   - For figures, tables, and data analysis, use `references/visuals-tables-data.md`.
   - Verify metadata, permission, source relevance, and claim strength before including any item.

7. **DOCX output when requested**
   - Read `references/docx-output.md`.
   - Apply Arial, 2.5 cm margins, 1.5 line spacing, justified body text, centered main titles, and left-aligned subheadings unless the user specifies otherwise.

8. **Final QA**
   - Read `references/qa-and-validation.md`.
   - Apply the language, critical-analysis, citation-prose, and capacity-reallocation checks.
   - Fail or rewrite unsupported claims, fake citations, overclaims, descriptive-only discussion, unpermitted figure reuse, decorative tables, unreallocated low-value content, and conclusions with new evidence.

## Reference Map

- `references/intake-and-planning.md`: intake fields, readiness gate, plan schema, approval loop, and plan-depth standard.
- `references/research-and-citation.md`: evidence hierarchy, DeepResearch workflow, source validation, citation modes, formatting integrations, and citation QA.
- `references/drafting-and-critical-analysis.md`: paragraph logic, analytic/descriptive balance, critical-analysis framework, language rules, revision discipline, and banned patterns.
- `references/visuals-tables-data.md`: paper-figure reuse gate, generated mechanism figures, GraphPad Prism-style data workflow, and academic table rules.
- `references/docx-output.md`: Word document formatting and output contract.
- `references/subagents.md`: recommended subagent roles and output schemas.
- `references/qa-and-validation.md`: plan, draft, citation, visual, DOCX, and final failure gates.
- `skill_manifest.json`: package metadata and health commands.
- `scripts/skill_maintenance.py`: run repository health checks.
- `scripts/validate_essay_tutor.py`: validate package structure and English-only repository content.

## Maintenance

Run these checks before committing or publishing changes:

```bash
python3 scripts/skill_maintenance.py doctor
python3 scripts/validate_essay_tutor.py --strict
```

Do not copy third-party Skill content into this Skill unless its license explicitly allows reuse. Optional integrations such as Citation.js, CSL styles, Scholar Sidekick MCP, citation-management Skills, GraphPad Prism, BioRender, or image generation should be invoked as external tools or documented workflows, not vendored without license review.
