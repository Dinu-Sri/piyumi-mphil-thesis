# Decision Record

## 2026-08-02 - Markdown-first thesis workflow

Decision: Use `chapters/*.md` as the working source for thesis writing and editing.

Reason: Markdown is easier for multiple agents to review, diff, version, and convert into formatted Word outputs when needed.

## 2026-08-02 - Preserve raw source files

Decision: Keep original Word, PDF, and image files under source folders and avoid overwriting them.

Reason: The thesis needs traceable source evidence and recoverable originals throughout review and formatting.

## 2026-08-02 - Use Git plus logs

Decision: Use Git for file-level versioning and `logs/work_log.md` / `logs/decisions.md` for human-readable continuity.

Reason: Future agents may need both exact diffs and concise project memory.

## 2026-08-02 - Versioned Word builds

Decision: Generate Word thesis drafts with `tools/build_thesis_docx.py` and save each build as a new versioned file in `output/word/`.

Reason: Final thesis formatting needs reproducible outputs without overwriting previous Word builds.

## 2026-08-02 - Word source extraction remains conservative

Decision: Use `tools/extract_docx_to_md.py` only to transfer existing Word draft content into Markdown, not to improve or rewrite it.

Reason: Scientific editing should happen in the Markdown layer where changes can be reviewed and versioned.
