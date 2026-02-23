#!/usr/bin/env python3
<<<<<<< HEAD
"""KNOT/KNU to GitHub Issues sync tool.

Reads LC01 CSVs and generates issue bodies for each KNOT.

Usage:
    python tools/ci/knot_issues_sync.py --dry-run
=======
"""Synchronise KNOT/KNU register with GitHub Issues.

Reads KNOTS.csv and KNU_PLAN.csv from SSOT/LC01_PROBLEM_STATEMENT/ and
creates or updates GitHub Issues with appropriate labels and status.

Usage:
    python tools/ci/knot_issues_sync.py --dry-run
    python tools/ci/knot_issues_sync.py --sync
>>>>>>> origin/main
"""

import argparse
import csv
import os
import sys

<<<<<<< HEAD
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
=======
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
>>>>>>> origin/main
LC01_PATH = os.path.join(REPO_ROOT, "SSOT", "LC01_PROBLEM_STATEMENT")


def load_knots():
<<<<<<< HEAD
    """Load KNOTs from CSV."""
    path = os.path.join(LC01_PATH, "KNOTS.csv")
    if not os.path.isfile(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
=======
    """Load KNOTS.csv and return list of dicts."""
    knots_file = os.path.join(LC01_PATH, "KNOTS.csv")
    if not os.path.isfile(knots_file):
        print(f"KNOTS.csv not found at {knots_file}")
        return []
    with open(knots_file, newline="", encoding="utf-8") as f:
>>>>>>> origin/main
        return list(csv.DictReader(f))


def load_knu_plan():
<<<<<<< HEAD
    """Load KNU plan from CSV."""
    path = os.path.join(LC01_PATH, "KNU_PLAN.csv")
    if not os.path.isfile(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
=======
    """Load KNU_PLAN.csv and return list of dicts."""
    knu_file = os.path.join(LC01_PATH, "KNU_PLAN.csv")
    if not os.path.isfile(knu_file):
        print(f"KNU_PLAN.csv not found at {knu_file}")
        return []
    with open(knu_file, newline="", encoding="utf-8") as f:
>>>>>>> origin/main
        return list(csv.DictReader(f))


def extract_ata_label(knot_id):
<<<<<<< HEAD
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
=======
    """Extract ATA label from KNOT ID (e.g., KNOT-ATA28-10-00-001 -> ATA-28)."""
    parts = knot_id.split("-")
    for part in parts:
        if part.startswith("ATA"):
            chapter = part[3:]
            if chapter.isdigit():
                return f"ATA-{chapter}"
    return None


def generate_issue_body(knot, knus):
    """Generate GitHub Issue body for a KNOT."""
    lines = [
        f"## {knot['Title']}",
        "",
        f"**KNOT ID:** `{knot['KNOT_ID']}`",
        f"**Residual:** {knot['Residual']} → Target: {knot['Target']}",
        f"**TT Pool:** {knot['Pool_TT']} TT",
        f"**Close Date:** {knot['Close_Date']}",
        f"**Status:** {knot['Status']}",
        "",
        "### Planned KNUs",
        "",
    ]
    related = [k for k in knus if k["KNOT_ID"] == knot["KNOT_ID"]]
    if related:
        lines.append("| KNU_ID | Type | Title | Phase | Status |")
        lines.append("|---|---|---|---|---|")
        for k in related:
            lines.append(f"| {k['KNU_ID']} | {k['KNU_Type']} | {k['Title']} | {k['LC_Phase']} | {k['Status']} |")
    else:
        lines.append("_No KNUs planned yet._")
>>>>>>> origin/main
    return "\n".join(lines)


def main():
<<<<<<< HEAD
    parser = argparse.ArgumentParser(description="KNOT → GitHub Issues sync")
    parser.add_argument("--dry-run", action="store_true", help="Print issue plan without creating")
    args = parser.parse_args()

=======
    parser = argparse.ArgumentParser(description="KNOT/KNU → GitHub Issues sync")
    parser.add_argument("--dry-run", action="store_true", help="Print issues without creating them")
    parser.add_argument("--sync", action="store_true", help="Create/update GitHub Issues (requires GITHUB_TOKEN)")
    args = parser.parse_args()

    if not args.dry_run and not args.sync:
        parser.error("Specify --dry-run or --sync")

>>>>>>> origin/main
    knots = load_knots()
    knus = load_knu_plan()

    if not knots:
<<<<<<< HEAD
        print("No KNOTs found in LC01.")
        sys.exit(0)

    for knot in knots:
        knot_id = knot.get("KNOT_ID", "")
        title = f"[{knot_id}] {knot.get('TITLE', '')}"
        ata_label = extract_ata_label(knot_id)
        labels = ["KNOT", knot.get("STATUS", "OPEN"), ata_label]
        body = generate_issue_body(knot, knus)
=======
        print("No KNOTs found. Nothing to sync.")
        sys.exit(0)

    print(f"Found {len(knots)} KNOTs and {len(knus)} KNUs")
    print()

    for knot in knots:
        ata_label = extract_ata_label(knot["KNOT_ID"])
        body = generate_issue_body(knot, knus)
        title = f"[{knot['KNOT_ID']}] {knot['Title']}"
        labels = ["KNOT", knot["Status"]]
        if ata_label:
            labels.append(ata_label)
>>>>>>> origin/main

        if args.dry_run:
            print(f"--- Issue: {title}")
            print(f"    Labels: {', '.join(labels)}")
<<<<<<< HEAD
            print(f"    Body preview ({len(body)} chars)")
            print()

    print(f"Total: {len(knots)} KNOT(s) processed.")
=======
            print(f"    KNUs: {sum(1 for k in knus if k['KNOT_ID'] == knot['KNOT_ID'])}")
            print()
        elif args.sync:
            print(f"SYNC not implemented in standalone mode — use GitHub Actions workflow")
            print(f"  Would create: {title}")

    print(f"✅ Processed {len(knots)} KNOTs")
>>>>>>> origin/main


if __name__ == "__main__":
    main()
