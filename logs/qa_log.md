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

## 2026-08-02 - Word build v005 visual QA

File: `output/word/piyumi_mphil_thesis_v005_20260802_2154.docx`

Rendered output: `tmp/render_v005/` (QA intermediate, not committed)

Checks completed:

- Full thesis outline added as `Organization of the Thesis` before Chapter 1.
- Rendered 25 pages.
- Title page has no visible page number.
- Outline section starts at page 1 because it is currently included as thesis body content.
- Chapter 1 begins after the outline section.
- DOCX XML font-color audit: zero non-black `w:color` font tags.
- Rendered-page color scan: zero saturated or dark colored pixels across all pages.
- Contact-sheet visual inspection: no obvious clipping, overlap, or missing page render.

Notes:

- This is a working thesis build. Before final WUSL submission, confirm whether `Organization of the Thesis` should remain as a body section, move into front matter, merge into Chapter 1, or be removed from the final bound version.

## 2026-08-02 - Word build v006 static TOC visual QA

File: `output/word/piyumi_mphil_thesis_v006_20260802_2212.docx`

Rendered output: `tmp/render_v006_static_toc/` (QA intermediate, not committed)

Checks completed:

- Rendered 22 pages.
- Title page has no visible page number.
- Table of Contents appears as front matter on page i.
- TOC includes chapter and section titles with dotted leaders and visible page numbers.
- Chapter 1 starts at thesis page 1; Chapter 3 starts at thesis page 13; Chapter 4 starts at thesis page 14.
- `chapters/ch00_full_thesis_outline.md` is not included in the rendered thesis body.
- DOCX XML font-color audit: zero non-black `w:color` font tags.
- Contact-sheet visual inspection: no obvious clipping, overlap, or missing page render.

Notes:

- The static TOC is generated from `tools/toc_entries_current.json`; refresh it with `tools/update_static_toc_entries.py` after chapter edits that affect pagination.
