# Visual QA Setup For Word Thesis Builds

Final or reviewable `.docx` files must be rendered to page images before delivery whenever possible. Text extraction is not enough, because Word layout defects can appear only after rendering.

## Required Tools

1. LibreOffice, for headless DOCX to PDF conversion.
2. Poppler `pdftoppm`, for PDF to PNG rasterization.
3. Bundled Codex Python runtime and document renderer.

In this workspace, `pdftoppm` is available through the Codex runtime. LibreOffice must be installed on each new Windows computer.

## Windows Install

Install LibreOffice:

```powershell
winget install --id TheDocumentFoundation.LibreOffice --source winget --accept-package-agreements --accept-source-agreements
```

Expected Windows path after installation:

```text
C:\Program Files\LibreOffice\program\soffice.exe
```

If `soffice` is not found in a new terminal, the project render helper adds the LibreOffice program folder to `PATH` for that command.

In Codex on Windows, LibreOffice rendering may need to run outside the filesystem sandbox because LibreOffice writes profile/cache files. If a render hangs in sandboxed execution, rerun the render command with approval/escalation instead of starting multiple LibreOffice processes.

## Render Command

Use the helper:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\render_docx_for_qa.ps1 -InputDocx ".\output\word\piyumi_mphil_thesis_v001_20260802_1745.docx" -EmitPdf
```

Or specify an output directory:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\render_docx_for_qa.ps1 -InputDocx ".\output\word\file.docx" -OutputDir ".\tmp\render_file" -EmitPdf
```

Rendered PNG pages are QA intermediates and normally belong under `tmp/`, which is ignored by Git.

## QA Checklist

Inspect every rendered page before considering a Word file review-ready:

- Page size is A4.
- Margins match WUSL requirements.
- All visible text is black.
- Table of Contents is visible, contains chapter/section titles, and page numbers match rendered heading pages.
- Page numbers appear at bottom center.
- Chapter headings are centered and formatted consistently.
- Body text is Times New Roman, 12 pt, justified.
- No overlapping text.
- No clipped headings, paragraphs, tables, captions, or footer text.
- No missing glyphs or unreadable symbols.
- Page breaks are acceptable.
- Figures and tables are close to their related text.

Record each QA pass in `logs/work_log.md`.

For static TOC builds, refresh `tools/toc_entries_current.json` after pagination-changing edits:

```powershell
python .\tools\update_static_toc_entries.py ".\tmp\render_file\file.pdf"
python .\tools\build_thesis_docx.py --stage final
```

Then render the rebuilt DOCX and visually inspect the TOC again.

If a render process hangs, check for `soffice`, `soffice.bin`, or Python renderer processes and stop only the stuck render processes before retrying.
