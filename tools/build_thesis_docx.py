#!/usr/bin/env python
"""Build a versioned Word thesis draft from Markdown chapter files."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "tools" / "thesis_build_config.json"
OUTPUT_DIR = ROOT / "output" / "word"
MANIFEST_PATH = OUTPUT_DIR / "build_manifest.jsonl"


def load_config(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def git_commit() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception:
        return "unknown"


def next_version(prefix: str) -> tuple[int, Path]:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    existing = sorted(OUTPUT_DIR.glob(f"{prefix}_v*.docx"))
    max_version = 0
    for path in existing:
        match = re.search(r"_v(\d+)_", path.name)
        if match:
            max_version = max(max_version, int(match.group(1)))
    version = max_version + 1
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M")
    return version, OUTPUT_DIR / f"{prefix}_v{version:03d}_{stamp}.docx"


def set_font(run, name: str, size_pt: int | float | None = None, bold: bool | None = None, italic: bool | None = None) -> None:
    run.font.name = name
    r_pr = run._element.get_or_add_rPr()
    r_fonts = r_pr.rFonts
    if r_fonts is None:
        r_fonts = OxmlElement("w:rFonts")
        r_pr.append(r_fonts)
    r_fonts.set(qn("w:ascii"), name)
    r_fonts.set(qn("w:hAnsi"), name)
    if size_pt is not None:
        run.font.size = Pt(size_pt)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic


def configure_document(doc: Document, line_spacing: float) -> None:
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.left_margin = Cm(3.7)
    section.right_margin = Cm(2.5)
    section.top_margin = Cm(3.5)
    section.bottom_margin = Cm(3.5)
    section.footer_distance = Cm(1.0)

    styles = doc.styles
    normal = styles["Normal"]
    normal.font.name = "Times New Roman"
    normal_rpr = normal._element.get_or_add_rPr()
    normal_fonts = normal_rpr.rFonts
    if normal_fonts is None:
        normal_fonts = OxmlElement("w:rFonts")
        normal_rpr.append(normal_fonts)
    normal_fonts.set(qn("w:ascii"), "Times New Roman")
    normal_fonts.set(qn("w:hAnsi"), "Times New Roman")
    normal.font.size = Pt(12)
    normal.paragraph_format.line_spacing = line_spacing
    normal.paragraph_format.space_after = Pt(0)

    for name in ["Heading 1", "Heading 2", "Heading 3"]:
        style = styles[name]
        style.font.name = "Times New Roman"
        style_rpr = style._element.get_or_add_rPr()
        style_fonts = style_rpr.rFonts
        if style_fonts is None:
            style_fonts = OxmlElement("w:rFonts")
            style_rpr.append(style_fonts)
        style_fonts.set(qn("w:ascii"), "Times New Roman")
        style_fonts.set(qn("w:hAnsi"), "Times New Roman")
        style.font.bold = True
        style.font.size = Pt(14 if name == "Heading 1" else 12)
        style.paragraph_format.line_spacing = line_spacing
        style.paragraph_format.space_before = Pt(12 if name == "Heading 1" else 6)
        style.paragraph_format.space_after = Pt(6)


def add_page_number(paragraph) -> None:
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run()
    fld_begin = OxmlElement("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = "PAGE"
    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")
    run._r.append(fld_begin)
    run._r.append(instr)
    run._r.append(fld_end)
    set_font(run, "Times New Roman", 12)


def add_title_page(doc: Document, config: dict) -> None:
    title = config.get("title", "THESIS TITLE")
    author = config.get("author", "FULL NAME OF STUDENT")
    degree = config.get("degree", "MASTER OF PHILOSOPHY")
    university = config.get("university", "WAYAMBA UNIVERSITY OF SRI LANKA")
    year = str(dt.date.today().year)

    for text, size, bold in [
        (title.upper(), 14, True),
        ("", 12, False),
        ("By", 12, False),
        (author.upper(), 12, True),
        ("", 12, False),
        (f"Thesis submitted to the {university} in fulfilment of the requirements for the Degree of {degree}", 12, False),
        ("", 12, False),
        (dt.datetime.now().strftime("%B %Y"), 12, False),
    ]:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.5
        if text:
            run = p.add_run(text)
            set_font(run, "Times New Roman", size, bold=bold)

    doc.add_page_break()


def strip_front_matter(markdown: str) -> str:
    text = markdown.lstrip("\ufeff")
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4 :]
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return text.strip()


def add_runs_with_inline_formatting(paragraph, text: str) -> None:
    pattern = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*)")
    pos = 0
    for match in pattern.finditer(text):
        if match.start() > pos:
            run = paragraph.add_run(text[pos : match.start()])
            set_font(run, "Times New Roman", 12)
        token = match.group(0)
        if token.startswith("**"):
            run = paragraph.add_run(token[2:-2])
            set_font(run, "Times New Roman", 12, bold=True)
        else:
            run = paragraph.add_run(token[1:-1])
            set_font(run, "Times New Roman", 12, italic=True)
        pos = match.end()
    if pos < len(text):
        run = paragraph.add_run(text[pos:])
        set_font(run, "Times New Roman", 12)


def add_markdown_table(doc: Document, table_lines: list[str], line_spacing: float) -> None:
    rows = []
    for line in table_lines:
        if re.match(r"^\|\s*[-:]+", line):
            continue
        cells = [cell.strip().replace("\\|", "|") for cell in line.strip().strip("|").split("|")]
        rows.append(cells)
    if not rows:
        return
    width = max(len(row) for row in rows)
    table = doc.add_table(rows=len(rows), cols=width)
    table.style = "Table Grid"
    for r_idx, row in enumerate(rows):
        for c_idx in range(width):
            cell = table.cell(r_idx, c_idx)
            text = row[c_idx] if c_idx < len(row) else ""
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = line_spacing
            add_runs_with_inline_formatting(p, text)
            for run in p.runs:
                set_font(run, "Times New Roman", 11, bold=(r_idx == 0))


def add_image(doc: Document, line: str, source_md: Path) -> bool:
    match = re.match(r"!\[(.*?)\]\((.*?)\)", line.strip())
    if not match:
        return False
    caption, raw_path = match.groups()
    image_path = Path(raw_path.strip())
    if not image_path.is_absolute():
        image_path = (source_md.parent / image_path).resolve()
        if not image_path.exists():
            image_path = (ROOT / raw_path.strip()).resolve()
    if not image_path.exists():
        p = doc.add_paragraph()
        add_runs_with_inline_formatting(p, f"[Missing image: {raw_path}]")
        return True
    doc.add_picture(str(image_path), width=Cm(13))
    if caption:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        run = p.add_run(caption)
        set_font(run, "Times New Roman", 11)
    return True


def add_markdown_file(doc: Document, path: Path, line_spacing: float, first_chapter: bool) -> None:
    markdown = strip_front_matter(path.read_text(encoding="utf-8"))
    lines = markdown.splitlines()
    paragraph_buffer: list[str] = []
    table_buffer: list[str] = []

    def flush_paragraph():
        if paragraph_buffer:
            text = " ".join(part.strip() for part in paragraph_buffer if part.strip())
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.line_spacing = line_spacing
            add_runs_with_inline_formatting(p, text)
            paragraph_buffer.clear()

    def flush_table():
        if table_buffer:
            add_markdown_table(doc, table_buffer, line_spacing)
            table_buffer.clear()

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            flush_paragraph()
            flush_table()
            continue

        if line.startswith("|"):
            flush_paragraph()
            table_buffer.append(line)
            continue
        flush_table()

        if add_image(doc, line, path):
            flush_paragraph()
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            text = heading.group(2).strip()
            if level == 1:
                if not first_chapter:
                    doc.add_section(WD_SECTION.NEW_PAGE)
                p = doc.add_paragraph(style="Heading 1")
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run = p.add_run(text.upper())
                set_font(run, "Times New Roman", 14, bold=True)
            elif level == 2:
                p = doc.add_paragraph(style="Heading 2")
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                run = p.add_run(text)
                set_font(run, "Times New Roman", 12, bold=True)
            else:
                p = doc.add_paragraph(style="Heading 3")
                p.paragraph_format.left_indent = Cm(1.0)
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                run = p.add_run(text)
                set_font(run, "Times New Roman", 12, bold=True)
            continue

        bullet = re.match(r"^[-*]\s+(.+)$", line)
        if bullet:
            flush_paragraph()
            p = doc.add_paragraph(style="List Bullet")
            p.paragraph_format.line_spacing = line_spacing
            add_runs_with_inline_formatting(p, bullet.group(1))
            continue

        numbered = re.match(r"^\d+[.)]\s+(.+)$", line)
        if numbered:
            flush_paragraph()
            p = doc.add_paragraph(style="List Number")
            p.paragraph_format.line_spacing = line_spacing
            add_runs_with_inline_formatting(p, numbered.group(1))
            continue

        paragraph_buffer.append(line)

    flush_paragraph()
    flush_table()


def build_docx(config: dict, stage: str, include_placeholders: bool) -> tuple[Path, dict]:
    line_spacing = 2.0 if stage == "initial" else 1.5
    doc = Document()
    configure_document(doc, line_spacing)

    footer = doc.sections[0].footer
    if footer.paragraphs:
        add_page_number(footer.paragraphs[0])

    if config.get("include_title_page", True):
        add_title_page(doc, config)

    first = True
    included = []
    skipped = []
    for chapter_rel in config["chapter_order"]:
        path = ROOT / chapter_rel
        if not path.exists():
            skipped.append(chapter_rel)
            continue
        text = path.read_text(encoding="utf-8")
        if not include_placeholders and "placeholder - to be drafted" in text:
            skipped.append(chapter_rel)
            continue
        add_markdown_file(doc, path, line_spacing, first_chapter=first)
        included.append(chapter_rel)
        first = False

    prefix = config.get("output_prefix", "thesis")
    version, output_path = next_version(prefix)
    doc.save(output_path)

    manifest = {
        "version": version,
        "created": dt.datetime.now().isoformat(timespec="seconds"),
        "stage": stage,
        "git_commit": git_commit(),
        "output": output_path.relative_to(ROOT).as_posix(),
        "included": included,
        "skipped": skipped,
    }
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    with MANIFEST_PATH.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(manifest) + "\n")

    return output_path, manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a versioned thesis DOCX from Markdown chapters.")
    parser.add_argument("--config", default=str(CONFIG_PATH), help="Build config JSON path.")
    parser.add_argument("--stage", choices=["initial", "final"], default="final", help="Line-spacing mode.")
    parser.add_argument("--include-placeholders", action="store_true", help="Include placeholder chapter files.")
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = ROOT / config_path
    output_path, manifest = build_docx(load_config(config_path), args.stage, args.include_placeholders)
    print(f"created {output_path.relative_to(ROOT)}")
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
