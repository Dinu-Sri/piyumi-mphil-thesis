# Thesis Workflow

## Default Workflow

1. Read the relevant chapter Markdown file.
2. Compare it with source material in `source_documents/` when needed.
3. Improve content in Markdown.
4. Add reviewer notes as Markdown comments when an issue is unresolved.
5. Update `logs/work_log.md`.
6. Commit a focused version when a meaningful unit is complete.

## Source DOCX Extraction

Use this when the user asks to import, refresh, or re-sync content from existing Word drafts:

```powershell
& "C:\Users\User\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" tools/extract_docx_to_md.py --all --force
```

This command updates the mapped Markdown files from the preserved Word files. It preserves source wording and citation text; it does not improve prose.

For one file:

```powershell
& "C:\Users\User\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" tools/extract_docx_to_md.py --source "source_documents/word_drafts/Ch1 - Introduction.docx" --out "chapters/ch01_introduction.md" --force
```

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
2. Generate a versioned `.docx` into `output/word/`.
3. Verify formatting against `project_docs/thesis_formatting.md`.
4. Render or visually inspect the `.docx` when possible.
5. Save any derived PDF in `output/pdf/`.
6. Record the output in `logs/work_log.md`.

Default Word build:

```powershell
& "C:\Users\User\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" tools/build_thesis_docx.py --stage final
```

Initial submission draft with double spacing:

```powershell
& "C:\Users\User\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" tools/build_thesis_docx.py --stage initial
```

To include placeholder chapters in the build:

```powershell
& "C:\Users\User\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" tools/build_thesis_docx.py --stage final --include-placeholders
```

Every build writes a new file named like `output/word/piyumi_mphil_thesis_v001_YYYYMMDD_HHMM.docx` and appends metadata to `output/word/build_manifest.jsonl`.

## Review Cycle

Scientific review should produce direct edits where confidence is high and comments where evidence is missing. Avoid rewriting around missing data.

Use `project_docs/scientific_writing_style.md` to remove AI-like wording and preserve a clear human scientific voice.

