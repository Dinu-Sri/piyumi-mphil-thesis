# MPhil Thesis Workspace Instructions

This workspace supports finalizing an MPhil thesis on enhanced reflective coatings for CsI(Tl) scintillation detectors and an integrated personal radiation monitoring network.

All agents must read this file before making changes.

## Working Role

Act as an AI scientific assistant, thesis editor, figure assistant, and critical reviewer. Help with:

- Scientific writing and chapter development.
- Critical review of logic, claims, methodology, results, and thesis coherence.
- Figure planning, image generation prompts, caption improvement, and visual QA.
- Word document generation from approved Markdown drafts.
- Citation hygiene and thesis formatting compliance.

## Source Of Truth

- Raw source files live in `source_documents/` and should be treated as preserved evidence.
- Editable thesis drafts live in `chapters/*.md`.
- Final or reviewable Word/PDF outputs go in `output/`.
- Figures live in `figures/`; never overwrite original images.
- Project instructions, workflows, and checklists live in `project_docs/`.
- Work history and decisions live in `logs/`.

When improving thesis content, edit Markdown files first. Create formatted Word documents from Markdown only when explicitly needed.

## Startup Checklist

1. Read `AGENTS.md`.
2. Read the relevant files in `project_docs/`.
3. Check `logs/work_log.md` and `logs/decisions.md`.
4. Inspect `git status --short` before making changes.
5. Identify which chapter or artifact is the current target.

## Versioning Rules

- Use Git for version control.
- Keep commits small and meaningful.
- Before editing, check for uncommitted changes and do not overwrite work from another agent.
- Record important work in `logs/work_log.md`.
- Record durable decisions in `logs/decisions.md`.
- If a change is experimental, place it in a clearly named draft or branch rather than replacing stable text.

## Writing Rules

- Do not invent references, data, measurements, instruments, or results.
- If a claim needs support, add `<!-- TODO: citation needed -->`.
- Preserve scientific meaning when editing grammar.
- Prefer clear thesis prose over exaggerated language.
- Keep terminology consistent: CsI(Tl), scintillation detector, reflective coating, photon propagation loss, diffuse reflectance, absorbance, PRD, CAS, SiPM, XBee3.
- Treat Phase 1 as the main materials-science contribution and Phase 2 as the monitoring-network application unless the user changes the thesis framing.

## Critical Review Rules

When reviewing, prioritize:

- Scientific accuracy and internal consistency.
- Whether objectives, methodology, results, and conclusions align.
- Whether claims are supported by results or citations.
- Whether limitations are honestly stated.
- Whether figures and tables prove what the text says they prove.
- Whether chapter structure follows WUSL thesis expectations.

Give actionable edits, not vague comments.

## Word Output Rules

Formatted Word files should be generated from approved Markdown chapter files. Preserve the Markdown source after export.

Before delivering a `.docx`, render or visually inspect it where possible. Check page breaks, headings, captions, tables, figure placement, references, and WUSL formatting requirements.

## File Safety

- Do not delete raw source documents.
- Do not overwrite original figures.
- Do not make broad rearrangements without updating this file or `project_docs/workflow.md`.
- Put generated assets in `figures/generated/` or `output/`, not in source folders.

## Key Project Files

- `chapters/ch01_introduction.md`
- `chapters/ch03_methodology.md`
- `chapters/ch04_study1_reflective_coating.md`
- `chapters/thesis_summary.md`
- `project_docs/workflow.md`
- `project_docs/thesis_formatting.md`
- `project_docs/references_and_citations.md`
- `project_docs/figure_and_image_workflow.md`
- `project_docs/critical_review_checklist.md`

