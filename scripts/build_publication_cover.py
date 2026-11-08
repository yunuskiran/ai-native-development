#!/usr/bin/env python3
"""Draw an original ebook cover and a paperback wrap sized to the final interior."""

import json
from pathlib import Path
import subprocess
import tempfile

from PIL import Image
from pypdf import PdfReader
from reportlab.lib.colors import CMYKColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph
from build_book_pdf import prune_unused_fonts

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/publication"
FONTS = Path("/System/Library/Fonts/Supplemental")
POPPLER = Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm"
INK = CMYKColor(0.8, 0.55, 0.35, 0.7)
CREAM = CMYKColor(0.01, 0.02, 0.07, 0)
TEAL = CMYKColor(0.62, 0.0, 0.29, 0.03)
ORANGE = CMYKColor(0, 0.52, 0.65, 0)


def paragraph(canvas, text, x, top, width, size=10.5, leading=15):
    style = ParagraphStyle("CoverCopy", fontName="CoverBody", fontSize=size,
                           leading=leading, textColor=CREAM)
    item = Paragraph(text, style)
    _, height = item.wrap(width, 800)
    item.drawOn(canvas, x, top - height)
    return top - height


def front(canvas, x, y, width, height, metadata):
    canvas.saveState()
    canvas.translate(x, y)
    canvas.setFillColor(INK)
    canvas.rect(0, 0, width, height, fill=1, stroke=0)
    left = 38
    canvas.setFillColor(TEAL)
    canvas.setFont("CoverSans", 8.5)
    canvas.drawString(left, height - 45, "FOUR METHODS / ONE ENGINEERING LENS")
    canvas.setFillColor(CREAM)
    canvas.setFont("CoverBold", 34)
    canvas.drawString(left, height - 115, "ENGINEERING")
    canvas.setFont("CoverBold", 48)
    canvas.drawString(left, height - 174, "WITH AI")
    canvas.setFillColor(ORANGE)
    canvas.setFont("CoverSans", 20)
    canvas.drawString(left, height - 222, metadata["subtitle"])
    paragraph(canvas,
              "Choosing and evaluating development workflows<br/>with decisions, context, and evidence",
              left, height - 250, width - 2 * left, 10, 15)
    center_x, center_y = width / 2, height * 0.32
    nodes = [(left + 8, center_y + 44, "INTENT"),
             (width - left - 8, center_y + 44, "DECISIONS"),
             (left + 8, center_y - 44, "CONTEXT"),
             (width - left - 8, center_y - 44, "EVIDENCE")]
    canvas.setStrokeColor(TEAL)
    canvas.setLineWidth(1)
    for nx, ny, label in nodes:
        canvas.line(center_x, center_y, nx, ny)
        canvas.setFillColor(INK)
        canvas.rect(nx - 4, ny - 4, 8, 8, fill=1, stroke=1)
        canvas.setFillColor(CREAM)
        canvas.setFont("CoverSans", 8)
        canvas.drawCentredString(nx, ny + (14 if ny > center_y else -19), label)
    canvas.setFillColor(ORANGE)
    canvas.rect(center_x - 9, center_y - 9, 18, 18, fill=1, stroke=0)
    canvas.setFillColor(CREAM)
    canvas.setFont("CoverSans", 9)
    canvas.drawString(left, 93, "BMAD  /  GSD  /  AWS AI-DLC  /  AIUP")
    canvas.setFont("CoverBold", 18)
    canvas.drawString(left, 56, metadata["author"])
    canvas.restoreState()


def main():
    for name, filename in [("CoverSans", "Arial.ttf"), ("CoverBold", "Arial Bold.ttf"),
                           ("CoverBody", "Georgia.ttf")]:
        pdfmetrics.registerFont(TTFont(name, str(FONTS / filename)))
    metadata = json.loads((ROOT / "publication/metadata.json").read_text())
    interior = PdfReader(ROOT / "output/pdf/engineering-with-ai-print.pdf")
    pages = len(interior.pages)
    assert pages % 2 == 0
    assert all(abs(float(p.mediabox.width) - 432) < 0.01 and
               abs(float(p.mediabox.height) - 648) < 0.01 for p in interior.pages)
    spine = pages * metadata["print"]["spineInchesPerPage"] * 72
    bleed, trim_w, trim_h = 9, 432, 648
    width, height = 2 * trim_w + spine + 2 * bleed, trim_h + 2 * bleed
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "engineering-with-ai-paperback-cover.pdf"
    canvas = Canvas(str(path), pagesize=(width, height), initialFontName="CoverSans")
    canvas.setTitle(metadata["title"] + ": " + metadata["subtitle"] + " - paperback cover")
    canvas.setAuthor(metadata["author"])
    canvas.setFillColor(INK)
    canvas.rect(0, 0, width, height, fill=1, stroke=0)
    front_x = bleed + trim_w + spine
    front(canvas, front_x, bleed, trim_w, trim_h, metadata)
    # Extend the artwork to each outside bleed edge.
    canvas.setFillColor(INK)
    canvas.rect(front_x + trim_w, 0, bleed, height, fill=1, stroke=0)
    left, top = bleed + 36, height - bleed - 46
    canvas.setFillColor(TEAL)
    canvas.setFont("CoverSans", 9)
    canvas.drawString(left, top, "ENGINEERING WITH AI")
    top = paragraph(canvas, "From generated output<br/>to accepted change", left, top - 30,
                    trim_w - 72, 23, 29) - 26
    for block in metadata["backCover"].split("\n\n")[1:]:
        top = paragraph(canvas, block, left, top, trim_w - 72) - 14
    assert top > 140, "Back-cover copy enters the reserved bottom area"
    canvas.setFont("CoverSans", 8)
    canvas.setFillColor(CREAM)
    canvas.drawString(left, 119, "FIRST EDITION / 2026")
    # KDP places its barcode in this blank 2 x 1.2 inch area.
    barcode = [bleed + trim_w - 18 - 144, bleed + 18, 144, 86.4]
    canvas.setFillColorCMYK(0, 0, 0, 0)
    canvas.rect(*barcode, fill=1, stroke=0)
    canvas.saveState()
    canvas.translate(bleed + trim_w + spine / 2, bleed + 42)
    canvas.rotate(90)
    canvas.setFillColor(CREAM)
    canvas.setFont("CoverBold", 11)
    canvas.drawString(0, -3.5, "Engineering with AI")
    canvas.setFont("CoverSans", 9)
    canvas.drawRightString(trim_h - 84, -3, metadata["author"])
    canvas.restoreState()
    canvas.showPage()
    canvas.save()
    prune_unused_fonts(path)
    with tempfile.TemporaryDirectory(prefix="book-cover-") as temp:
        temp = Path(temp)
        digital = Canvas(str(temp / "front.pdf"), pagesize=(432, 691.2),
                         initialFontName="CoverSans")
        front(digital, 0, 0, 432, 691.2, metadata)
        digital.showPage()
        digital.save()
        subprocess.run([str(POPPLER), "-singlefile", "-scale-to-x", "1600",
                        "-scale-to-y", "2560", "-png", str(temp / "front.pdf"),
                        str(temp / "front")], check=True, capture_output=True)
        image = Image.open(temp / "front.png").convert("RGB")
        assert image.size == (1600, 2560)
        image.save(OUT / "engineering-with-ai-ebook-cover.jpg", quality=95, dpi=(300, 300))
    record = {"trimInches": [6, 9], "paper": "white", "ink": "black and white",
              "interiorPages": pages, "spineInches": spine / 72,
              "coverInches": [width / 72, height / 72], "coverBleedInches": 0.125,
              "barcodeAreaPoints": barcode, "ebookCoverPixels": [1600, 2560],
              "artwork": "Original AI-designed programmatic typography and geometry",
              "specification": "https://kdp.amazon.com/en_US/help/topic/G201953020"}
    (OUT / "print-specifications.json").write_text(json.dumps(record, indent=2) + "\n")
    print(path)
    print(OUT / "engineering-with-ai-ebook-cover.jpg")


if __name__ == "__main__":
    main()
