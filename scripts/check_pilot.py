#!/usr/bin/env python3
"""Audit pilot document integrity; this does not certify source truth or run code."""

import hashlib
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "research/evidence/PILOT_MANIFEST.json"


def count_words(text):
    """Count headings/prose/table text; exclude banners, markers and link URLs."""
    text = re.sub(r"^>.*$", "", text, flags=re.M)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"^\|[\s|:-]+\|$", "", text, flags=re.M)
    return len(re.findall(r"[A-Za-z0-9]+(?:[’'/-][A-Za-z0-9]+)*", text))


def main(manifest_path=MANIFEST):
    # Read each file once: hashes, counts and links must refer to the same bytes.
    # This also avoids repeatedly hydrating files on a synchronized filesystem.
    cache = {}

    def file_bytes(path):
        path = path.resolve()
        if path not in cache:
            if os.environ.get("BOOK_AUDIT_PROGRESS") == "1":
                print(f"Checking {path.relative_to(ROOT)}", file=sys.stderr, flush=True)
            cache[path] = path.read_bytes()
        return cache[path]

    def file_text(path):
        return file_bytes(path).decode("utf-8")

    manifest = json.loads(file_text(manifest_path))
    receipts = []
    supplements = []
    for receipt_path in manifest["sourceReceiptFiles"]:
        record = json.loads(file_text(ROOT / receipt_path))
        receipts.extend(record["sources"])
        supplements.extend(record.get("supplementalInspections", []))
    old_sources = {
        x["id"]: x for x in json.loads(
            file_text(ROOT / "research/evidence/SOURCE_RECEIPTS.json")
        )["sources"]
    }
    by_url = {x["url"]: x for x in receipts}
    errors = []
    github_citations = 0
    web_citations = 0
    sections = []
    total_words = 0
    used_sources = set()

    if len({s["sourceId"] for s in receipts}) != len(receipts):
        errors.append("Duplicate source IDs in pilot receipt set")

    by_id = {s["sourceId"]: s for s in receipts}
    for supplement in supplements:
        source = by_id.get(supplement["sourceId"])
        if (not source or source["url"] != supplement["url"]
                or source.get("ref") != supplement.get("ref")
                or supplement["retrieval"] != "INSPECTED"):
            errors.append(f"Invalid supplemental inspection: {supplement['sourceId']}")
            continue
        source["inspectedRanges"] = source["inspectedRanges"] + supplement["inspectedRanges"]

    for source in receipts:
        old = old_sources.get(source["sourceId"], {})
        if source["sourceId"].startswith("M2-") and old.get("url") != source["url"]:
            errors.append(f"Source identity mismatch: {source['sourceId']}")
        if not source["sourceId"].startswith("M2-") and not source.get("claimId"):
            errors.append(f"New pilot source lacks bounded claim: {source['sourceId']}")
        if source["retrieval"] != "INSPECTED":
            errors.append(f"Uninspected pilot source: {source['sourceId']}")

    for artifact in manifest["artifacts"]:
        path = ROOT / artifact["path"]
        text = file_text(path)
        digest = hashlib.sha256(file_bytes(path)).hexdigest()
        words = count_words(text)
        actual_sections = re.findall(r"<!-- (C\d+-S\d+) -->", text)
        if digest != artifact["sha256"]:
            errors.append(f"Artifact changed since manifest: {artifact['path']}")
        if words != artifact["words"]:
            errors.append(f"Word count changed: {artifact['path']}")
        if actual_sections != artifact["sectionIds"]:
            errors.append(f"Section coverage changed: {artifact['path']}")
        total_words += words
        sections.extend(actual_sections)

        for dest in re.findall(r"\[[^\]]+\]\((https://[^\s)]+)\)", text):
            base, _, fragment = dest.partition("#")
            source = by_url.get(base)
            if not source:
                errors.append(f"External citation lacks recheck receipt: {dest}")
                continue
            used_sources.add(source["sourceId"])
            if source["kind"] == "github-file":
                match = re.fullmatch(r"L(\d+)(?:-L(\d+))?", fragment)
                if not match:
                    errors.append(f"Missing GitHub line locator: {dest}")
                    continue
                start = int(match[1])
                end = int(match[2] or match[1])
                if not any(a <= start <= end <= b for a, b in source["inspectedRanges"]):
                    errors.append(f"Citation exceeds rechecked range: {dest}")
                github_citations += 1
            else:
                web_citations += 1

    if len(sections) != len(set(sections)) or len(sections) != manifest["expectedSectionCount"]:
        errors.append("Unique planned section count differs from manifest")
    if total_words != manifest["totalWords"]:
        errors.append("Total word count mismatch")
    if used_sources != {x["sourceId"] for x in receipts}:
        errors.append("Used citation sources differ from pilot receipt set")

    for entry in manifest.get("ancillaryArtifacts", []):
        path = ROOT / entry["path"]
        if not path.exists() or hashlib.sha256(file_bytes(path)).hexdigest() != entry["sha256"]:
            errors.append(f"Ancillary artifact hash mismatch: {entry['path']}")

    for record_path in manifest.get("executionRecords", []):
        record = json.loads(file_text(ROOT / record_path))
        if record["exitCode"] != 0:
            errors.append(f"Execution record is not passing: {record_path}")
        for relative, expected_hash in record["files"].items():
            if hashlib.sha256(file_bytes(ROOT / relative)).hexdigest() != expected_hash:
                errors.append(f"Execution evidence is stale for: {relative}")

    # Resolve local paths in the registered book/active documents. Legacy pilot
    # manifests retain the older whole-repository scan. Neither checks anchors.
    local_links = 0
    link_paths = ([ROOT / p for p in manifest["linkCheckPaths"]]
                  if "linkCheckPaths" in manifest else ROOT.rglob("*.md"))
    for path in link_paths:
        if any(part in {".git", "node_modules"} for part in path.parts):
            continue
        for dest in re.findall(r"(?<!!)\[[^\]]+\]\(([^\n)]+)\)", file_text(path)):
            dest = dest.strip("<>")
            parsed = urlsplit(dest)
            if parsed.scheme or dest.startswith("#") or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.exists():
                errors.append(f"Broken local path in {path.relative_to(ROOT)}: {dest}")
            local_links += 1

    master = ROOT / "docs/BOOK_MASTER_PLAN.md"
    if hashlib.sha256(file_bytes(master)).hexdigest() != manifest["originalMasterSha256"]:
        errors.append("Original master hash changed")
    plan = json.loads(file_text(ROOT / "research/CHAPTER_PLAN.json"))
    # The approved outline is also pinned, so unchanged titles/order are checkable.
    outline = ROOT / "OUTLINE.md"
    if hashlib.sha256(file_bytes(outline)).hexdigest() != manifest["outlineSha256"]:
        errors.append("Approved outline changed")
    if len(plan["chapters"]) != 14 or sum(c["targetWords"] for c in plan["chapters"]) != 66500:
        errors.append("Chapter count or approved word allocation changed")
    chapters = {c["id"]: c for c in plan["chapters"]}
    for artifact in manifest["artifacts"]:
        if artifact["chapterId"]:
            chapter = chapters[artifact["chapterId"]]
            expected = [s["id"] for s in chapter["sections"]]
            if artifact["sectionIds"] != expected:
                errors.append(f"Pilot sections differ from brief plan: {chapter['id']}")
            if artifact["finalChapterTargetWords"] != chapter["targetWords"]:
                errors.append(f"Pilot target differs from approved allocation: {chapter['id']}")
            title = f"# {chapter['number']}. {chapter['title']}"
            if file_text(ROOT / artifact["path"]).splitlines()[0] != title:
                errors.append(f"Pilot chapter title differs: {chapter['id']}")
    readiness = file_text(ROOT / "research/EXPERIMENT_READINESS.md")
    if len(re.findall(r"^- \[ \]", readiness, flags=re.M)) != 13:
        errors.append("Experiment readiness state differs from thirteen open checks")

    if errors:
        raise SystemExit("FAIL\n" + "\n".join(errors))
    print(json.dumps({
        "status": "PASS — document integrity only",
        "artifacts": len(manifest["artifacts"]),
        "words": total_words,
        "sections": len(sections),
        "githubCitationOccurrences": github_citations,
        "webCitationOccurrences": web_citations,
        "distinctInspectedSources": len(receipts),
        "localLinkPaths": local_links,
        "linkCheckScope": ("registered manuscript and active project documents"
                           if "linkCheckPaths" in manifest else "repository Markdown"),
        "originalMaster": "unchanged",
        "approvedOutline": "unchanged",
        "experimentReadiness": "13 unchecked",
        "independentReview": "pending, not evaluated by this script",
        "registeredExecutionRecords": len(manifest.get("executionRecords", [])),
    }, indent=2))


if __name__ == "__main__":
    main()
