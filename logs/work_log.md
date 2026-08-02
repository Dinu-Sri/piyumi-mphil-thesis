# Work Log

## 2026-08-02

- Organized the thesis workspace into Markdown drafts, source documents, figures, references, project instructions, logs, outputs, and tools.
- Preserved original Word/PDF thesis materials under `source_documents/`.
- Moved Study 1 source images under `figures/source_images/study1/`.
- Generated initial Markdown chapter drafts from available Word documents.
- Added WUSL thesis formatting instructions from the thesis preparation guideline PDF.
- Added scientific writing style instructions for thesis editing and AI-like wording cleanup.
- Added tools for DOCX-to-Markdown extraction and versioned Markdown-to-DOCX thesis builds.
- Ran `tools/extract_docx_to_md.py --all --force` to refresh mapped chapter Markdown from preserved Word drafts.
- Built `output/word/piyumi_mphil_thesis_v001_20260802_1745.docx` with `tools/build_thesis_docx.py --stage final`.
- Verified the generated DOCX structurally with `python-docx`: A4 page size, WUSL margins, 142 paragraphs, 3 sections. Render QA could not be completed because LibreOffice/`soffice` was not available in the current environment.
