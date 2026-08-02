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

