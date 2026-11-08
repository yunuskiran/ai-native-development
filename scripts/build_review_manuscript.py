#!/usr/bin/env python3
"""Assemble the registered chapters and source notes into one review copy."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "manuscript/REVIEW_MANUSCRIPT.md"
MANIFEST = ROOT / "research/evidence/MANUSCRIPT_MANIFEST.json"


def assemble():
    manifest = json.loads(MANIFEST.read_text())
    chapters = [a for a in manifest["artifacts"] if a["chapterId"]]
    anchors = {(ROOT / a["path"]).resolve(): a["chapterId"].lower() for a in chapters}
    notes = ROOT / "manuscript/SOURCE_NOTES.md"
    anchors[notes.resolve()] = "source-notes"
    contents = []
    parts = []

    def rewrite_link(match, source):
        label, destination = match.groups()
        parsed = urlsplit(destination)
        if parsed.scheme or not parsed.path or destination.startswith("#"):
            return match.group(0)
        target = (source.parent / unquote(parsed.path)).resolve()
        if not target.exists():
            raise ValueError(f"Missing link target in {source}: {destination}")
        if target in anchors and not parsed.fragment and not parsed.query:
            return f"[{label}](#{anchors[target]})"
        relative = Path(os.path.relpath(target, OUTPUT.parent)).as_posix()
        if parsed.query:
            relative += "?" + parsed.query
        if parsed.fragment:
            relative += "#" + parsed.fragment
        return f"[{label}]({relative})"

    for artifact in chapters:
        source = ROOT / artifact["path"]
        raw = source.read_bytes()
        if hashlib.sha256(raw).hexdigest() != artifact["sha256"]:
            raise ValueError(f"Chapter differs from registered revision: {source}")
        text = raw.decode("utf-8")
        title = text.splitlines()[0][2:]
        anchor = artifact["chapterId"].lower()
        contents.append(f"- [{title}](#{anchor})")
        # Revision banners are retained in source files and summarized up front.
        text = re.sub(r"^> .*\n", "", text, count=1, flags=re.M)
        text = re.sub(r"<!-- C\d+-S\d+ -->\n", "", text)
        text = re.sub(r"^#{1,5} ", lambda m: "#" + m[0], text, flags=re.M)
        text = re.sub(r"\[([^\]]+)\]\(([^\n)]+)\)",
                      lambda m: rewrite_link(m, source), text)
        parts.append(f'<a id="{anchor}"></a>\n\n{text.strip()}')

    note_text = re.sub(r"^#{1,5} ", lambda m: "#" + m[0], notes.read_text(), flags=re.M)
    note_text = re.sub(r"\[([^\]]+)\]\(([^\n)]+)\)",
                       lambda m: rewrite_link(m, notes), note_text)
    parts.append('<a id="source-notes"></a>\n\n' + note_text.strip())
    contents.append("- [Source notes](#source-notes)")
    metadata = json.loads((ROOT / "publication/metadata.json").read_text())
    preface = f"""# {metadata['title']}: {metadata['subtitle']}

{metadata['author']} · First edition · 2026

A practical comparison of BMAD Method, GSD, AWS AI-DLC, and AI Unified Process for developers, technical leads, and architects. The book follows decisions, context, and verification through a synthetic multi-tenant approval service.

The method accounts describe dated source snapshots. The case is a qualitative walkthrough. A separate TypeScript policy model has ten passing local checks. The source notes identify the inspected revisions and the limits of the evidence.

## About this edition

{metadata['aiDisclosure']}

The methods and product names belong to their respective owners. Their use identifies the subjects discussed. This publication is independently prepared and carries no endorsement from the method maintainers or platform vendors. No third-party logo or screenshot is used on the cover.

Read chapters 1–3 for the comparison vocabulary, 4–7 for the four methods, 8–10 for specification policy, comparison and selection, and 11–14 for the case, assurance, diagnosis and future evaluation.

## Contents

"""
    return preface + "\n".join(contents) + "\n\n---\n\n" + "\n\n---\n\n".join(parts) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify the copy matches its inputs")
    args = parser.parse_args()
    expected = assemble()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text() != expected:
            raise SystemExit("Review manuscript is missing or stale")
        print("PASS — review copy matches registered chapters and source notes")
    else:
        OUTPUT.write_text(expected)
        print(OUTPUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
