#!/usr/bin/env python
"""Refresh static TOC entries from a rendered thesis PDF.

Run this after building and rendering a proof DOCX. It reads the configured
Markdown chapters, finds their level 1-3 headings in the rendered PDF, and
writes thesis page numbers for the static TOC used by build_thesis_docx.py.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "tools" / "thesis_build_config.json"


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def collect_heading_entries(config: dict) -> list[dict]:
    entries: list[dict] = []
    for chapter_rel in config["chapter_order"]:
        path = ROOT / chapter_rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "placeholder - to be drafted" in text:
            continue
        for line in text.splitlines():
            match = re.match(r"^(#{1,3})\s+(.+)$", line.strip())
            if match:
                entries.append({"level": len(match.group(1)), "text": match.group(2).strip()})
    return entries


def add_page_numbers(entries: list[dict], pdf_path: Path, body_start_pdf_page: int) -> list[dict]:
    reader = PdfReader(str(pdf_path))
    pages = [page.extract_text() or "" for page in reader.pages]
    normalized_pages = [normalize(page) for page in pages]
    last_index = max(body_start_pdf_page - 1, 0)

    for entry in entries:
        target = normalize(entry["text"])
        found_pdf_page = None
        for index in range(last_index, len(normalized_pages)):
            if target and target in normalized_pages[index]:
                found_pdf_page = index + 1
                last_index = index
                break
        entry["thesis_page"] = found_pdf_page - body_start_pdf_page + 1 if found_pdf_page else None
    return entries


def main() -> int:
    parser = argparse.ArgumentParser(description="Refresh static thesis TOC entries from a rendered PDF.")
    parser.add_argument("pdf", help="Rendered thesis PDF path.")
    parser.add_argument("--config", default=str(CONFIG_PATH), help="Build config JSON path.")
    parser.add_argument("--output", default="tools/toc_entries_current.json", help="TOC entries JSON output path.")
    parser.add_argument("--body-start-pdf-page", type=int, default=3, help="PDF page where Arabic thesis page 1 starts.")
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = ROOT / config_path
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = ROOT / output_path
    pdf_path = Path(args.pdf)
    if not pdf_path.is_absolute():
        pdf_path = ROOT / pdf_path

    config = json.loads(config_path.read_text(encoding="utf-8"))
    entries = add_page_numbers(collect_heading_entries(config), pdf_path, args.body_start_pdf_page)
    missing = [entry["text"] for entry in entries if entry.get("thesis_page") is None]
    if missing:
        raise RuntimeError(f"Could not locate headings in rendered PDF: {missing}")

    output_path.write_text(json.dumps(entries, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {output_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
