#!/usr/bin/env python3
"""Check all registered chapter drafts; retain the historical pilot checker."""
from check_pilot import ROOT, main

if __name__ == "__main__":
    main(ROOT / "research/evidence/MANUSCRIPT_MANIFEST.json")
