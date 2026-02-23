#!/usr/bin/env python3
"""KNOT/KNU to GitHub Issues sync tool.

Reads LC01 CSVs and generates issue bodies for each KNOT.

Usage:
    python tools/ci/knot_issues_sync.py --dry-run
"""

import argparse
import csv
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LC01_PATH = os.path.join(REPO_ROOT, "SSOT", "LC01_PROBLEM_STATEMENT")


def load_knots():
    """Load KNOTs from CSV."""
    path = os.path.join(LC01_PATH, "KNOTS.csv")
    if not os.path.isfile(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_knu_plan():
    """Load KNU plan from CSV."""
    path = os.path.join(LC01_PATH, "KNU_PLAN.csv")
    if not os.path.isfile(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def extract_ata_label(knot_id):
    """Extract ATA label from KNOT ID (e.g., KNOT-ATA28-10-00-001 -> ATA28)."""
    parts = knot_id.split("-")
    for p in parts:
        if p.startswith("ATA"):
            return p
    return "ATA-UNKNOWN"


def generate_issue_body(knot, knus):
    """Generate a GitHub issue body for a KNOT."""
    lines = [
        f"# {knot.get('TITLE', 'Untitled')}",
        "",
        f"**KNOT ID:** `{knot.get('KNOT_ID', '')}`",
        f"**ATA:** {knot.get('ATA', '')}",
        f"**TT Budget:** {knot.get('TT_BUDGET', '')}",
        f"**Status:** {knot.get('STATUS', '')}",
        "",
        f"> {knot.get('DESCRIPTION', '')}",
        "",
        "## Related KNUs",
        "",
    ]
    related = [k for k in knus if k.get("KNOT_ID") == knot.get("KNOT_ID")]
    if related:
        lines.append("| KNU ID | Title | Phase | Status |")
        lines.append("|---|---|---|---|")
        for k in related:
            lines.append(
                f"| `{k.get('KNU_ID', '')}` | {k.get('TITLE', '')} "
                f"| {k.get('LC_PHASE', '')} | {k.get('STATUS', '')} |"
            )
    else:
        lines.append("_No KNUs linked yet._")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="KNOT → GitHub Issues sync")
    parser.add_argument("--dry-run", action="store_true", help="Print issue plan without creating")
    args = parser.parse_args()

    knots = load_knots()
    knus = load_knu_plan()

    if not knots:
        print("No KNOTs found in LC01.")
        sys.exit(0)

    for knot in knots:
        knot_id = knot.get("KNOT_ID", "")
        title = f"[{knot_id}] {knot.get('TITLE', '')}"
        ata_label = extract_ata_label(knot_id)
        labels = ["KNOT", knot.get("STATUS", "OPEN"), ata_label]
        body = generate_issue_body(knot, knus)

        if args.dry_run:
            print(f"--- Issue: {title}")
            print(f"    Labels: {', '.join(labels)}")
            print(f"    Body preview ({len(body)} chars)")
            print()

    print(f"Total: {len(knots)} KNOT(s) processed.")


if __name__ == "__main__":
    main()
