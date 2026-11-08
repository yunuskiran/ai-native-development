#!/usr/bin/env python3
"""Build an EPUB 3 from the registered Markdown, using marked and lxml."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import unquote, urlsplit
import zipfile

from lxml import etree, html

from build_review_manuscript import OUTPUT as MANUSCRIPT, ROOT, assemble

XHTML = "http://www.w3.org/1999/xhtml"
EPUB = "http://www.idpf.org/2007/ops"
OPF = "http://www.idpf.org/2007/opf"
DC = "http://purl.org/dc/elements/1.1/"
OUTPUT = ROOT / "output/publication/engineering-with-ai.epub"
REPOSITORY = "https://github.com/yunuskiran/ai-native-development/blob/main/"
CSS = """body { margin: 5%; line-height: 1.45; }
h1,h2,h3,h4 { font-family: sans-serif; line-height: 1.2; text-align: left; }
h1 { margin-top: 1em; font-size: 1.65em; }
h2 { margin-top: 1.7em; font-size: 1.25em; break-after: avoid; }
h3 { margin-top: 1.4em; font-size: 1.05em; break-after: avoid; }
p { margin: 0 0 0.85em; orphans: 2; widows: 2; }
a { text-decoration: underline; }
code,pre { font-family: monospace; font-size: 0.9em; }
pre { white-space: pre-wrap; overflow-wrap: anywhere; }
table { width: 100%; border-collapse: collapse; font-size: 0.85em; margin: 1em 0; }
th,td { border: 1px solid #aaa; padding: 0.4em; vertical-align: top; overflow-wrap: anywhere; }
th { background: #eee; text-align: left; }
blockquote { margin-left: 1em; }
li { margin-bottom: 0.45em; }
nav ol { padding-left: 1.2em; }
nav li { margin-bottom: 0.65em; }
.cover { margin: 0; text-align: center; }
.cover img { width: 100%; height: auto; max-width: 100%; }
.titlepage { text-align: center; margin-top: 15%; }
.source-record { margin-bottom: 1.4em; }
.source-record dt { font-weight: bold; margin-top: 0.5em; }
.source-record dd { margin-left: 0; overflow-wrap: anywhere; }
"""


def element(parent, tag, text=None, **attributes):
    node = etree.SubElement(parent, tag, attributes)
    node.text = text
    return node


def xhtml_document(title):
    root = etree.Element("html", nsmap={None: XHTML, "epub": EPUB},
                         attrib={"lang": "en", "{http://www.w3.org/XML/1998/namespace}lang": "en"})
    head = element(root, "head")
    element(head, "title", title)
    element(head, "meta", charset="utf-8")
    element(head, "link", href="styles/book.css", rel="stylesheet", type="text/css")
    return root, element(root, "body")


def serialized(node):
    return etree.tostring(node, encoding="utf-8", xml_declaration=True, pretty_print=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    bundled = Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/marked/bin/marked.js"
    parser.add_argument("--marked", type=Path, default=bundled,
                        help="Path to the marked CLI (tested with marked 17.0.5)")
    args = parser.parse_args()
    if MANUSCRIPT.read_text() != assemble():
        raise SystemExit("Rebuild the consolidated manuscript before building EPUB")
    if not args.marked.exists():
        raise SystemExit("Pass --marked with a path to the installed marked CLI")
    metadata = json.loads((ROOT / "publication/metadata.json").read_text())
    text = MANUSCRIPT.read_text()
    parts = re.split(r'<a id="([^"]+)"></a>\s*', text)
    anchors = parts[1::2]
    paths = {anchor: ("sources.xhtml" if anchor == "source-notes" else anchor + ".xhtml")
             for anchor in anchors}
    resources = {"styles/book.css": CSS.encode()}
    navigation = []
    chapter_text = []

    def render(markdown):
        result = subprocess.run([shutil.which("node") or "node", str(args.marked)],
                                input=markdown, text=True, capture_output=True, check=True)
        return html.fragment_fromstring(result.stdout, create_parent="div")

    def rewrite_links(fragment):
        for link in fragment.iter("a"):
            destination = link.get("href", "")
            parsed = urlsplit(destination)
            if parsed.scheme or destination.startswith("mailto:"):
                continue
            if destination.startswith("#") and destination[1:] in paths:
                link.set("href", paths[destination[1:]])
                continue
            if parsed.path:
                target = (MANUSCRIPT.parent / unquote(parsed.path)).resolve()
                if not target.is_relative_to(ROOT) or not target.exists():
                    raise ValueError(f"Invalid repository link: {destination}")
                url = REPOSITORY + target.relative_to(ROOT).as_posix()
                if parsed.fragment:
                    url += "#" + parsed.fragment
                link.set("href", url)

    for anchor, markdown in zip(anchors, parts[2::2]):
        markdown = re.sub(r"\n---\s*$", "", markdown).strip()
        fragment = render(markdown)
        rewrite_links(fragment)
        # Use lists for the five-column bibliography on small ebook screens.
        if anchor == "source-notes":
            for table in list(fragment.iter("table")):
                rows = table.findall(".//tr")
                headers = rows[0].findall("th")
                if len(headers) != 5:
                    continue
                labels = ["".join(cell.itertext()) for cell in headers]
                records = etree.Element("div")
                for row in rows[1:]:
                    listing = etree.SubElement(records, "dl", {"class": "source-record"})
                    for label, cell in zip(labels, row.findall("td")):
                        element(listing, "dt", label)
                        value = element(listing, "dd")
                        value.text = cell.text
                        for child in list(cell):
                            value.append(child)
                table.getparent().replace(table, records)
        headings = []
        for index, heading in enumerate(fragment.xpath(".//h2 | .//h3 | .//h4 | .//h5")):
            level = int(heading.tag[1:]) - 1
            heading.tag = f"h{level}"
            heading.set("id", f"{anchor}-heading-{index}")
            if level == 2:
                headings.append((heading.get("id"), "".join(heading.itertext())))
        title_node = fragment.find("h1")
        if title_node is None:
            raise ValueError(f"Chapter title missing in {anchor}")
        title = "".join(title_node.itertext())
        root, body = xhtml_document(title)
        body.set("{" + EPUB + "}type", "bibliography" if anchor == "source-notes" else "bodymatter")
        body.text = fragment.text
        for child in list(fragment):
            body.append(child)
        for table in body.iter("table"):
            for header in table.iter("th"):
                header.set("scope", "col")
        path = paths[anchor]
        resources[path] = serialized(root)
        navigation.append((path, title, headings))
        chapter_text.append({"anchor": anchor, "file": path, "title": title})

    root, body = xhtml_document(metadata["title"] + ": " + metadata["subtitle"])
    body.set("class", "titlepage")
    body.set("{" + EPUB + "}type", "titlepage")
    element(body, "h1", metadata["title"])
    element(body, "p", metadata["subtitle"])
    element(body, "p", metadata["author"])
    element(body, "p", "First edition, 2026")
    element(body, "h2", "About this edition")
    element(body, "p", metadata["aiDisclosure"])
    element(body, "p", "The case is a synthetic qualitative walkthrough. Method descriptions use dated source snapshots. Third-party names and marks identify the subjects discussed. Their owners retain their respective rights. No official endorsement is implied.")
    resources["title.xhtml"] = serialized(root)
    root, body = xhtml_document("Cover")
    body.set("class", "cover")
    body.set("{" + EPUB + "}type", "cover")
    element(body, "img", src="images/cover.jpg", alt=metadata["title"] + ": " + metadata["subtitle"] + " by " + metadata["author"])
    resources["cover.xhtml"] = serialized(root)
    resources["images/cover.jpg"] = (ROOT / "output/publication/engineering-with-ai-ebook-cover.jpg").read_bytes()
    root, body = xhtml_document("Contents")
    nav = element(body, "nav", id="toc")
    nav.set("{" + EPUB + "}type", "toc")
    element(nav, "h1", "Contents")
    listing = element(nav, "ol")
    for path, title, headings in navigation:
        item = element(listing, "li")
        element(item, "a", title, href=path)
        if headings:
            nested = element(item, "ol")
            for anchor, label in headings:
                sub = element(nested, "li")
                element(sub, "a", label, href=path + "#" + anchor)
    landmarks = element(body, "nav", id="landmarks", hidden="hidden")
    landmarks.set("{" + EPUB + "}type", "landmarks")
    listing = element(landmarks, "ol")
    for path, label, kind in [("cover.xhtml", "Cover", "cover"),
                              ("c01.xhtml", "Beginning", "bodymatter")]:
        link = element(element(listing, "li"), "a", label, href=path)
        link.set("{" + EPUB + "}type", kind)
    resources["nav.xhtml"] = serialized(root)
    package = etree.Element("package", nsmap={None: OPF}, version="3.0",
                            attrib={"unique-identifier": "book-id"})
    info = element(package, "metadata")
    info.nsmap.update({"dc": DC})
    element(info, "{" + DC + "}identifier", metadata["identifier"], id="book-id")
    element(info, "{" + DC + "}title", metadata["title"] + ": " + metadata["subtitle"])
    element(info, "{" + DC + "}creator", metadata["author"], id="creator")
    element(info, "{" + DC + "}language", "en-US")
    element(info, "{" + DC + "}date", metadata["publicationDate"])
    element(info, "{" + DC + "}description", metadata["description"])
    element(info, "meta", metadata["publicationDate"] + "T00:00:00Z", property="dcterms:modified")
    element(info, "meta", name="cover", content="cover-image")
    element(info, "meta", "reflowable", property="rendition:layout")
    for subject in metadata["subjects"]:
        element(info, "{" + DC + "}subject", subject)
    manifest = element(package, "manifest")
    item_ids = {}
    for index, path in enumerate(resources):
        item_id = "cover-image" if path == "images/cover.jpg" else f"item-{index}"
        item_ids[path] = item_id
        media = "application/xhtml+xml" if path.endswith(".xhtml") else "text/css" if path.endswith(".css") else "image/jpeg"
        attrs = {"id": item_id, "href": path, "media-type": media}
        if path == "nav.xhtml":
            attrs["properties"] = "nav"
        elif path == "images/cover.jpg":
            attrs["properties"] = "cover-image"
        element(manifest, "item", **attrs)
    spine = element(package, "spine")
    for path in ["cover.xhtml", "title.xhtml", "nav.xhtml", *[x[0] for x in navigation]]:
        element(spine, "itemref", idref=item_ids[path])
    resources["package.opf"] = serialized(package)
    container = b'<?xml version="1.0" encoding="UTF-8"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="EPUB/package.opf" media-type="application/oebps-package+xml"/></rootfiles></container>'
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        archive.writestr("META-INF/container.xml", container)
        for path, content in resources.items():
            archive.writestr("EPUB/" + path, content)
    record = {"format": "EPUB 3 reflowable", "file": OUTPUT.relative_to(ROOT).as_posix(),
              "sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
              "chapters": chapter_text, "renderer": "marked 17.0.5 and lxml",
              "embeddedFonts": False, "coverPixels": [1600, 2560]}
    (OUTPUT.parent / "epub-build.json").write_text(json.dumps(record, indent=2) + "\n")
    print(OUTPUT)


if __name__ == "__main__":
    main()
