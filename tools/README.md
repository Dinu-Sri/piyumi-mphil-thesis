# Thesis Tools

Use the bundled Codex Python runtime when running these tools.

## Extract Word Drafts To Markdown

```powershell
& "C:\Users\User\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" tools/extract_docx_to_md.py --all --force
```

Purpose:

- Read preserved `.docx` drafts from `source_documents/`.
- Extract paragraph text, headings, simple tables, inline citation text, and reference paragraphs.
- Write editable Markdown drafts under `chapters/`.

## Build Versioned Word Thesis

```powershell
& "C:\Users\User\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" tools/build_thesis_docx.py --stage final
```

Purpose:

- Combine chapter Markdown files listed in `tools/thesis_build_config.json`.
- Apply WUSL-oriented Word defaults.
- Save a new versioned `.docx` under `output/word/`.
- Append build metadata to `output/word/build_manifest.jsonl`.

Use `--stage initial` for double-spaced initial-submission drafts.

## Render DOCX For Visual QA

Install LibreOffice first if needed:

```powershell
winget install --id TheDocumentFoundation.LibreOffice --source winget --accept-package-agreements --accept-source-agreements
```

Then render:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\render_docx_for_qa.ps1 -InputDocx ".\output\word\piyumi_mphil_thesis_v001_20260802_1745.docx" -EmitPdf
```

Inspect every generated `page-<N>.png` before delivery.
