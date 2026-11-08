#!/usr/bin/env python3
"""Typeset the completed Markdown manuscript with ReportLab."""

import argparse
import html
import json
from functools import partial
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (
    BaseDocTemplate, Frame, KeepTogether, PageBreak, PageTemplate, Paragraph, Spacer,
    Table, TableStyle, XPreformatted,
)
from reportlab.platypus.tableofcontents import TableOfContents

from build_review_manuscript import OUTPUT as INPUT, assemble

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/pdf/engineering-with-ai.pdf"
FONT_ROOT = Path("/System/Library/Fonts/Supplemental")
WIDTH, HEIGHT = A4
MARGIN = 54
TEXT_WIDTH = WIDTH - 2 * MARGIN
INK = colors.HexColor("#243746")
MUTED = colors.HexColor("#596675")
LINK_COLOR = "#245A7A"


def inline(text):
    """Convert the inline markup used by the manuscript to Paragraph markup."""
    text = text.replace("—", " - ").replace("–", "-").replace("\u2011", "-")
    text = html.escape(text, quote=False)

    def link(match):
        label, target = match.groups()
        safe_target = html.escape(html.unescape(target), quote=True)
        if target.startswith(("https://", "http://", "#")):
            return f'<a href="{safe_target}" color="{LINK_COLOR}">{label}</a>'
        return label

    text = re.sub(r"\[([^\]]+)\]\(([^\n)]+)\)", link, text)
    text = re.sub(r"`([^`]+)`", r'<font name="BookMono">\1</font>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    return text


def table_cells(line):
    cells, current = [], []
    in_code = False
    escaped = False
    for char in line.strip().strip("|"):
        if char == "`" and not escaped:
            in_code = not in_code
        if char == "|" and not in_code and not escaped:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
        escaped = char == "\\" and not escaped
    cells.append("".join(current).strip())
    return cells


class Book(BaseDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and getattr(flowable, "chapter_anchor", None):
            anchor = flowable.chapter_anchor
            self.canv.bookmarkPage(anchor)
            self.canv.addOutlineEntry(flowable.getPlainText(), anchor, 0)
            self.notify("TOCEntry", (0, flowable.getPlainText(), self.page, anchor))


def page_furniture(canvas, doc):
    if doc.page == 1:
        return
    canvas.saveState()
    canvas.setFont("BookSans", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(MARGIN, HEIGHT - 31, "ENGINEERING WITH AI")
    canvas.drawRightString(WIDTH - MARGIN, HEIGHT - 31, "YUNUS KIRAN / FIRST EDITION")
    canvas.setStrokeColor(MUTED)
    canvas.setLineWidth(0.4)
    canvas.line(MARGIN, HEIGHT - 38, WIDTH - MARGIN, HEIGHT - 38)
    canvas.drawRightString(WIDTH - MARGIN, 30, str(doc.page))
    canvas.restoreState()


def prune_unused_fonts(path):
    """Remove ReportLab's unused base-font registration, retaining every used font."""
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import ContentStream
    reader = PdfReader(path)
    used = set()
    for page in reader.pages:
        resources = page.get("/Resources", {})
        if hasattr(resources, "get_object"):
            resources = resources.get_object()
        # Form XObjects can carry their own font references. Keep those intact.
        if resources.get("/XObject"):
            return
        contents = page.get_contents()
        if contents is not None:
            for operands, operator in ContentStream(contents, reader).operations:
                if operator == b"Tf":
                    used.add(str(operands[0]))
    if not used:
        raise ValueError("No font references found in a non-empty book")
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    for page in writer.pages:
        resources = page.get("/Resources", {})
        if hasattr(resources, "get_object"):
            resources = resources.get_object()
        fonts = resources.get("/Font", {})
        if hasattr(fonts, "get_object"):
            fonts = fonts.get_object()
        for name in list(fonts):
            if str(name) not in used:
                del fonts[name]
    temporary = path.with_suffix(".tmp.pdf")
    with temporary.open("wb") as stream:
        writer.write(stream)
    temporary.replace(path)


def main():
    global WIDTH, HEIGHT, MARGIN, TEXT_WIDTH, OUTPUT, INK, MUTED, LINK_COLOR
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--print", action="store_true", dest="print_edition",
                        help="Build the 6 x 9 inch, no-bleed paperback interior")
    args = parser.parse_args()
    metadata = json.loads((ROOT / "publication/metadata.json").read_text())
    if args.print_edition:
        WIDTH, HEIGHT = 432, 648
        MARGIN = 45
        TEXT_WIDTH = WIDTH - 2 * MARGIN
        OUTPUT = ROOT / "output/pdf/engineering-with-ai-print.pdf"
        INK, MUTED = colors.black, colors.Color(0.32, 0.32, 0.32)
        LINK_COLOR = "#000000"
    if not INPUT.exists() or INPUT.read_text() != assemble():
        raise SystemExit("Rebuild the consolidated manuscript before typesetting")
    for name, filename in [
        ("BookBody", "Georgia.ttf"), ("BookBold", "Georgia Bold.ttf"),
        ("BookItalic", "Georgia Italic.ttf"), ("BookBoldItalic", "Georgia Bold Italic.ttf"),
        ("BookSans", "Arial.ttf"), ("BookSansBold", "Arial Bold.ttf"),
        ("BookMono", "Andale Mono.ttf"),
    ]:
        pdfmetrics.registerFont(TTFont(name, str(FONT_ROOT / filename)))
    pdfmetrics.registerFontFamily("BookBody", normal="BookBody", bold="BookBold",
                                  italic="BookItalic", boldItalic="BookBoldItalic")
    pdfmetrics.registerFontFamily("BookSans", normal="BookSans", bold="BookSansBold")
    styles = getSampleStyleSheet()
    body = ParagraphStyle("BookParagraph", fontName="BookBody", fontSize=10 if args.print_edition else 10.3,
                          leading=14 if args.print_edition else 15,
                          spaceAfter=7, textColor=INK,
                          allowWidows=0, allowOrphans=0, splitLongWords=1)
    heading = ParagraphStyle("Chapter", parent=body, fontName="BookSansBold",
                             fontSize=20 if args.print_edition else 24,
                             leading=25 if args.print_edition else 30,
                             spaceAfter=23, keepWithNext=True)
    section = ParagraphStyle("Section", parent=body, fontName="BookSansBold",
                             fontSize=14, leading=19, spaceBefore=16,
                             spaceAfter=9, keepWithNext=True)
    subheading = ParagraphStyle("Subsection", parent=section, fontSize=11,
                                leading=15, spaceBefore=12, spaceAfter=7)
    cell = ParagraphStyle("Cell", parent=body, fontName="BookSans", fontSize=8,
                          leading=11, spaceAfter=0, allowWidows=1, allowOrphans=1)
    bullet = ParagraphStyle("List", parent=body, leftIndent=16, firstLineIndent=-11,
                            spaceAfter=5)
    code = ParagraphStyle("Code", fontName="BookMono", fontSize=7.3, leading=10,
                          spaceBefore=4, spaceAfter=10, textColor=INK,
                          backColor=colors.Color(0.95, 0.95, 0.95), borderPadding=7)
    small = ParagraphStyle("Small", parent=body, fontName="BookSans", fontSize=9,
                           leading=13, textColor=MUTED)
    story = [Spacer(1, 70), Paragraph(inline(metadata["title"]), heading),
             Paragraph(inline(metadata["subtitle"]), section), Spacer(1, 28),
             Paragraph(inline(metadata["author"]), section), Spacer(1, 20),
             Paragraph("First edition / 2026", small), PageBreak(),
             Paragraph("About this edition", section)]
    text = INPUT.read_text()
    front = text.split("## Contents", 1)[0].splitlines()[4:]
    for paragraph in "\n".join(front).strip().split("\n\n"):
        if paragraph.strip() and not paragraph.startswith("## "):
            story.append(Paragraph(inline(paragraph.replace("\n", " ")), body))
    story.extend([PageBreak(), Paragraph("Contents", heading)])
    toc = TableOfContents()
    toc.tableStyle = TableStyle([
        *toc.tableStyle.getCommands(),
        ("FONTNAME", (0, 0), (-1, -1), "BookSans"),
    ])
    toc.levelStyles = [ParagraphStyle("TOC", fontName="BookSans",
                                      fontSize=9.4 if args.print_edition else 10.2,
                                      leading=13.5 if args.print_edition else 15,
                                      spaceBefore=5 if args.print_edition else 8, textColor=INK,
                                      rightIndent=24)]
    story.append(toc)
    lines = text[text.index('<a id="c01">'):].splitlines()
    index = 0
    anchor = None
    while index < len(lines):
        line = lines[index].strip()
        index += 1
        if not line or line == "---":
            continue
        if line.startswith('<a id="'):
            anchor = re.search(r'id="([^"]+)"', line)[1]
            continue
        if line.startswith("## "):
            story.append(PageBreak())
            paragraph = Paragraph(inline(line[3:]), heading)
            paragraph.chapter_anchor = anchor
            story.append(paragraph)
            anchor = None
            continue
        if line.startswith("### "):
            story.append(Paragraph(inline(line[4:]), section))
            continue
        if line.startswith("#### "):
            story.append(Paragraph(inline(line[5:]), subheading))
            continue
        if line.startswith("```"):
            block = []
            while index < len(lines) and not lines[index].strip().startswith("```"):
                block.append(lines[index])
                index += 1
            index += 1
            story.append(XPreformatted(html.escape("\n".join(block)), code,
                                       maxLineLength=94))
            continue
        if line.startswith("|"):
            rows = [table_cells(line)]
            while index < len(lines) and lines[index].strip().startswith("|"):
                row = lines[index].strip()
                index += 1
                if not re.fullmatch(r"\|[\s|:\-]+\|", row):
                    rows.append(table_cells(row))
            columns = len(rows[0])
            if any(len(row) != columns for row in rows):
                raise ValueError(f"Inconsistent table near line {index}")
            if args.print_edition and columns == 5 and rows[0][0] == "Record":
                for row in rows[1:]:
                    record = [Paragraph(inline(f"**{row[0]}** - {row[1]}"), body),
                              Paragraph(inline(
                                  f"{row[2]}. Source version: {row[3]}. Accessed {row[4]}."), small)]
                    destination = re.search(r"\]\((https://[^)]+)\)", row[1])
                    if destination:
                        url = destination[1]
                        record.append(Paragraph(inline(f"[{url}]({url})"), small))
                    record.append(Spacer(1, 10))
                    story.append(KeepTogether(record))
                continue
            weights = [max(24, min(65, max(len(re.sub(r'\]\([^)]*\)', '', row[c]))
                                          for row in rows))) for c in range(columns)]
            widths = [TEXT_WIDTH * weight / sum(weights) for weight in weights]
            data = [[Paragraph(inline(value), cell) for value in row] for row in rows]
            table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
            table.setStyle(TableStyle([
                ("FONTNAME", (0, 0), (-1, -1), "BookSans"),
                ("BACKGROUND", (0, 0), (-1, 0), colors.Color(0.9, 0.9, 0.9)),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.Color(0.97, 0.97, 0.97)]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("LINEBELOW", (0, 0), (-1, 0), 0.6, MUTED),
            ]))
            story.extend([table, Spacer(1, 10)])
            continue
        if re.match(r"(?:[-*] |\d+\. )", line):
            line = re.sub(r"^[-*] ", "• ", line)
            story.append(Paragraph(inline(line), bullet))
            continue
        paragraph_lines = [line]
        while index < len(lines) and lines[index].strip():
            next_line = lines[index].strip()
            if next_line.startswith(("#", "|", "```", "<a ")) or next_line == "---":
                break
            paragraph_lines.append(next_line)
            index += 1
        content = " ".join(paragraph_lines)
        if content.startswith("> "):
            content = content[2:]
        story.append(Paragraph(inline(content), body))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = Book(str(OUTPUT), pagesize=(WIDTH, HEIGHT), leftMargin=MARGIN, rightMargin=MARGIN,
               topMargin=54, bottomMargin=52, title="Engineering with AI: Beyond Vibe Coding",
               author=metadata["author"], pageCompression=1, initialFontName="BookBody")
    frame = Frame(MARGIN, 52, TEXT_WIDTH, HEIGHT - 106, leftPadding=0,
                  rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates(PageTemplate(id="Book", frames=frame, onPage=page_furniture))
    doc.multiBuild(story, canvasmaker=partial(Canvas, initialFontName="BookBody"))
    if args.print_edition:
        from pypdf import PdfReader, PdfWriter
        reader = PdfReader(str(OUTPUT))
        if len(reader.pages) % 2:
            writer = PdfWriter()
            writer.clone_document_from_reader(reader)
            writer.add_blank_page(width=WIDTH, height=HEIGHT)
            with OUTPUT.open("wb") as stream:
                writer.write(stream)
    prune_unused_fonts(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()
