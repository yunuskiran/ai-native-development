#!/usr/bin/env python3
"""Check EPUB structure, text transfer, print dimensions and cover consistency."""

import hashlib
import html
import json
import posixpath
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import zipfile

from lxml import etree
from PIL import Image
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
XHTML = "http://www.w3.org/1999/xhtml"
OPF = "http://www.idpf.org/2007/opf"
DC = "http://purl.org/dc/elements/1.1/"


def normalize(text):
    return re.sub(r"[^\w]", "", html.unescape(text)).casefold()


def plain_markdown(text):
    text = re.sub(r"\[([^\]]+)\]\([^\n)]+\)", r"\1", text)
    return text.replace("`", "").replace("**", "")


def embedded_fonts(reader):
    result = {}
    for page in reader.pages:
        resources = page.get("/Resources")
        if not resources:
            continue
        for font in resources.get_object().get("/Font", {}).values():
            font = font.get_object()
            descriptor = font.get("/FontDescriptor")
            if descriptor:
                descriptor = descriptor.get_object()
            result[str(font.get("/BaseFont"))] = bool(descriptor and any(
                key in descriptor for key in ("/FontFile", "/FontFile2", "/FontFile3")))
    assert result and all(result.values()), result
    return result


def pdf_body_text(reader):
    pages = []
    for i, page in enumerate(reader.pages, 1):
        lines = page.extract_text().splitlines()
        pages.append("\n".join(line for line in lines if line.strip() not in {
            "ENGINEERING WITH AI", "YUNUS KIRAN / FIRST EDITION", str(i)}))
    return normalize("\n".join(pages))


def main():
    metadata = json.loads((ROOT / "publication/metadata.json").read_text())
    manifest = json.loads((ROOT / "research/evidence/MANUSCRIPT_MANIFEST.json").read_text())
    spec = json.loads((ROOT / "output/publication/print-specifications.json").read_text())
    epub_path = ROOT / "output/publication/engineering-with-ai.epub"
    interior_path = ROOT / "output/pdf/engineering-with-ai-print.pdf"
    reading_path = ROOT / "output/pdf/engineering-with-ai.pdf"
    cover_path = ROOT / "output/publication/engineering-with-ai-paperback-cover.pdf"
    interior = PdfReader(interior_path)
    assert len(interior.pages) == spec["interiorPages"] and len(interior.pages) % 2 == 0
    assert len(interior.pages) <= 500, "Recalculate the gutter before using this page count"
    assert metadata["print"]["insideMarginInches"] >= 0.625
    assert all(abs(float(p.mediabox.width) - 432) < 0.01 and
               abs(float(p.mediabox.height) - 648) < 0.01 for p in interior.pages)
    assert interior.metadata.author == metadata["author"]
    fonts = embedded_fonts(interior)
    reading = PdfReader(reading_path)
    reading_fonts = embedded_fonts(reading)
    cover = PdfReader(cover_path)
    assert len(cover.pages) == 1
    cover_fonts = embedded_fonts(cover)
    actual_size = [float(cover.pages[0].mediabox.width) / 72,
                   float(cover.pages[0].mediabox.height) / 72]
    assert all(abs(a - b) < 0.0001 for a, b in zip(actual_size, spec["coverInches"]))
    assert abs(spec["spineInches"] - len(interior.pages) * 0.002252) < 0.000001
    image = Image.open(ROOT / "output/publication/engineering-with-ai-ebook-cover.jpg")
    assert image.size == (1600, 2560) and image.mode == "RGB"
    text = pdf_body_text(interior)
    reading_text = pdf_body_text(reading)
    checked = 0
    with zipfile.ZipFile(epub_path) as archive:
        files = archive.namelist()
        assert archive.read("EPUB/images/cover.jpg") == (
            ROOT / "output/publication/engineering-with-ai-ebook-cover.jpg").read_bytes()
        assert files[0] == "mimetype" and archive.read("mimetype") == b"application/epub+zip"
        assert archive.getinfo("mimetype").compress_type == zipfile.ZIP_STORED
        documents = {name: etree.fromstring(archive.read(name)) for name in files
                     if name.endswith((".xhtml", ".opf", ".xml"))}
        package = documents["EPUB/package.opf"]
        assert package.find(".//{" + DC + "}creator").text == metadata["author"]
        assert package.find(".//{" + DC + "}identifier").text == metadata["identifier"]
        items = {item.get("id"): item for item in package.findall(".//{" + OPF + "}item")}
        for ref in package.findall(".//{" + OPF + "}itemref"):
            assert ref.get("idref") in items
        assert any(item.get("properties") == "nav" for item in items.values())
        assert any(item.get("properties") == "cover-image" for item in items.values())
        links = 0
        for name, doc in documents.items():
            if not name.endswith(".xhtml"):
                continue
            for node in doc.iter():
                destination = node.get("href") or node.get("src")
                if not destination:
                    continue
                parsed = urlsplit(destination)
                if parsed.scheme:
                    continue
                target = posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(parsed.path))) if parsed.path else name
                assert target in files, (name, destination)
                if parsed.fragment:
                    assert target in documents
                    assert documents[target].xpath("//*[@id=$anchor]", anchor=parsed.fragment), (name, destination)
                links += 1
        for chapter in (a for a in manifest["artifacts"] if a["chapterId"]):
            source = (ROOT / chapter["path"]).read_text()
            doc = documents["EPUB/" + chapter["chapterId"].lower() + ".xhtml"]
            epub_text = normalize(" ".join(doc.itertext()))
            for paragraph in source.split("\n\n"):
                paragraph = paragraph.strip()
                if paragraph.startswith(("#", "|", "<", ">", "- ", "```")) or len(paragraph.split()) < 25:
                    continue
                if re.match(r"^\d+\. ", paragraph):
                    continue
                expected = normalize(plain_markdown(paragraph))
                assert expected in epub_text, ("EPUB", chapter["chapterId"], paragraph[:90])
                assert expected in text, ("PDF", chapter["chapterId"], paragraph[:90])
                assert expected in reading_text, ("Reading PDF", chapter["chapterId"], paragraph[:90])
                checked += 1
    result = {"date": "2026-11-05", "status": "PASS", "epubVersion": "3.0",
              "epubInternalReferencesChecked": links, "longChapterParagraphsVerified": checked,
              "printPages": len(interior.pages), "trimInches": [6, 9], "interiorBleed": False,
              "readingPages": len(reading.pages), "readingFontsEmbedded": reading_fonts,
              "printFontsEmbedded": fonts, "coverFontsEmbedded": cover_fonts,
              "wrapCoverInches": actual_size, "spineInches": spec["spineInches"],
              "ebookCoverPixels": [1600, 2560],
              "kindlePreviewer": "NOT COMPLETED: downloaded package and application failed signature verification",
              "files": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                        for p in (epub_path, interior_path, cover_path, reading_path)}}
    (ROOT / "research/evidence/PUBLICATION_FORMAT_CHECKS.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
