#!/usr/bin/env python3
"""Package the prepared upload files and their validation records."""

import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/engineering-with-ai-publication.zip"


def main():
    spec = json.loads((ROOT / "output/publication/print-specifications.json").read_text())
    status = json.loads((ROOT / "research/evidence/PUBLICATION_FORMAT_CHECKS.json").read_text())
    assert status["status"] == "PASS"
    files = {
        "engineering-with-ai.epub": "output/publication/engineering-with-ai.epub",
        "engineering-with-ai-print.pdf": "output/pdf/engineering-with-ai-print.pdf",
        "engineering-with-ai-reading.pdf": "output/pdf/engineering-with-ai.pdf",
        "engineering-with-ai-paperback-cover.pdf": "output/publication/engineering-with-ai-paperback-cover.pdf",
        "engineering-with-ai-ebook-cover.jpg": "output/publication/engineering-with-ai-ebook-cover.jpg",
        "metadata.json": "publication/metadata.json",
        "store-description.html": "publication/store-description.html",
        "store-listing.md": "publication/STORE_LISTING.md",
        "review-report.md": "publication/REVIEW_REPORT.md",
        "print-specifications.json": "output/publication/print-specifications.json",
        "checks/epubcheck.json": "research/evidence/EPUBCHECK_PUBLICATION.json",
        "checks/format-checks.json": "research/evidence/PUBLICATION_FORMAT_CHECKS.json",
        "checks/visual-layout.json": "research/evidence/PUBLICATION_VISUAL_QA.json",
        "checks/kindle-previewer-status.json": "research/evidence/KINDLE_PREVIEWER_STATUS.json",
        "checks/source-similarity-audit.json": "research/evidence/PUBLICATION_AUDIT_2026_11_05.json",
        "checks/copyedits.json": "research/evidence/PUBLICATION_COPYEDITS.json",
        "checks/policy-tests.tap": "research/evidence/PUBLICATION_POLICY_CHECKS.tap",
    }
    contents = {name: (ROOT / path).read_bytes() for name, path in files.items()}
    # Prevent a stale file from silently entering the release package.
    for relative, expected in status["files"].items():
        assert hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == expected, relative
    guide = f"""# Engineering with AI — prepared publication package

Title: Engineering with AI
Subtitle: Beyond Vibe Coding
Author: Yunus Kiran
Language: English (US)

## Kindle ebook

Upload engineering-with-ai.epub as the manuscript and engineering-with-ai-ebook-cover.jpg as the cover. The EPUB is reflowable and passed EPUBCheck 5.4.0 with zero errors and warnings. The ebook cover is RGB, 1600 x 2560 pixels.

Official Kindle Previewer inspection remains open. The downloaded Amazon package and application failed signature verification and were not executed. Use a valid signed Kindle Previewer installation or KDP Online Previewer to inspect navigation, tables, source cards and large-font views on phone, tablet and e-reader modes before publication. The status record is included under checks/.

## Paperback

Upload engineering-with-ai-print.pdf as the interior and engineering-with-ai-paperback-cover.pdf as the single back/spine/front cover. Select 6 x 9 inches, black ink, white paper and no interior bleed. Prepared page count: {spec['interiorPages']}. Cover size: {spec['coverInches'][0]:.6f} x {spec['coverInches'][1]:.2f} inches. Spine width: {spec['spineInches']:.6f} inches. The cover includes 0.125-inch bleed and a blank barcode area.

No ISBN has been assigned. Use the selected publishing service's ISBN/barcode process. If paper, trim or interior page count changes, regenerate the cover before upload. Check the final upload preview and order a physical proof before authorizing print sales.

engineering-with-ai-reading.pdf is the larger reading copy. Use the explicitly named print file for the 6 x 9 paperback.

## Store information

metadata.json and store-listing.md contain the title, author, description, three candidate categories and seven keyword fields. store-description.html contains the description in HTML. Category labels must be matched to the choices offered by the selected marketplace. The byline uses the connected GitHub profile name. No author biography or credential was invented.

The manuscript text and programmatic cover were created using an AI assistant. The listing prepares AI-generated text and cover disclosure. Account, territory, pricing, rights and any exclusivity choice remain publishing decisions.

## Review scope

The technical, source, bounded similarity and English editorial pass was performed by the drafting AI assistant. All 35 source records were reopened, and all 95 GitHub citation occurrences resolved to retrieved ranges. The 12-word comparison covered twenty pinned GitHub files and fourteen chapters. It does not certify originality against all external publications. Independent human technical/copyedit and full rights clearance remain open.

No marketplace upload or GitHub publication was performed in this preparation pass. No blanket public reuse licence has been selected for the manuscript. Third-party marks and source material retain their respective rights.

SHA256SUMS.txt identifies the packaged files. Validation and review records are under checks/ and in review-report.md.
"""
    contents["README.md"] = guide.encode()
    contents["SHA256SUMS.txt"] = ("\n".join(
        hashlib.sha256(content).hexdigest() + "  " + name
        for name, content in sorted(contents.items())) + "\n").encode()
    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in contents.items():
            archive.writestr("engineering-with-ai/" + name, content)
    with zipfile.ZipFile(OUTPUT) as archive:
        assert archive.testzip() is None
    (ROOT / "output/publication/UPLOAD_GUIDE.md").write_text(guide)
    print(OUTPUT)


if __name__ == "__main__":
    main()
