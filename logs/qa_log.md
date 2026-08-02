# QA Log

## 2026-08-02 - Word build v004 visual QA

File: `output/word/piyumi_mphil_thesis_v004_20260802_1833.docx`

Rendered output: `tmp/render_v004/` (QA intermediate, not committed)

Checks completed:

- LibreOffice installed and used for DOCX to PDF conversion.
- Poppler `pdftoppm` used for PDF to PNG page rendering.
- Rendered 21 pages.
- Title page has no visible page number.
- Introduction starts at page 1.
- A4 page size verified structurally.
- WUSL margins verified structurally: left 3.7 cm, right 2.5 cm, top 3.5 cm, bottom 3.5 cm.
- DOCX XML font-color audit: zero non-black `w:color` font tags.
- Rendered-page color scan: zero saturated or dark colored pixels across all pages.
- Contact-sheet visual inspection: no obvious clipping, overlap, or missing page render.

Notes:

- LibreOffice emitted `Could not find platform independent libraries <prefix>` after conversion, but the PDF and PNG outputs were created successfully.
- The Word file is a toolchain QA build from currently available chapter drafts, not a scientific/content-final thesis.

