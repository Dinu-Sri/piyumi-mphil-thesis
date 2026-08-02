# Thesis Workflow

## Default Workflow

1. Read the relevant chapter Markdown file.
2. Compare it with source material in `source_documents/` when needed.
3. Improve content in Markdown.
4. Add reviewer notes as Markdown comments when an issue is unresolved.
5. Update `logs/work_log.md`.
6. Commit a focused version when a meaningful unit is complete.

## Chapter Development Cycle

Each chapter should move through these states:

- `source-derived draft`
- `structure improved`
- `scientifically reviewed`
- `citation checked`
- `figure/table integrated`
- `supervisor-review ready`
- `Word formatted`
- `final submission ready`

Record the current status in the YAML front matter at the top of each chapter file.

## Export Cycle

When a Word document is needed:

1. Confirm which Markdown files are approved for export.
2. Generate a `.docx` into `output/word/`.
3. Verify formatting against `project_docs/thesis_formatting.md`.
4. Render or visually inspect the `.docx` when possible.
5. Save any derived PDF in `output/pdf/`.
6. Record the output in `logs/work_log.md`.

## Review Cycle

Scientific review should produce direct edits where confidence is high and comments where evidence is missing. Avoid rewriting around missing data.

