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
- Installed LibreOffice 26.2.5.2 using `winget` for DOCX visual rendering QA.
- Added visual QA setup instructions and a PowerShell render helper for future agents/computers.
- Updated `tools/build_thesis_docx.py` so all generated Word font colors are explicitly black, including an OOXML normalization pass.
- Built and rendered `output/word/piyumi_mphil_thesis_v004_20260802_1833.docx` for visual QA.
- QA result for v004: 21 rendered pages; title page unnumbered; Introduction starts at page 1; A4 page size and WUSL margins retained; XML audit found zero non-black font color tags; rendered image color scan found zero saturated/dark colored pixels; contact-sheet inspection showed no obvious clipping or overlap.
