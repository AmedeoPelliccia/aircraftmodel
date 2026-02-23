#!/usr/bin/env python3
"""Synchronise KNOT/KNU register with GitHub Issues.

Reads KNOTS.csv and KNU_PLAN.csv from SSOT/LC01_PROBLEM_STATEMENT/ and
creates or updates GitHub Issues with appropriate labels and status.

Usage:
    python tools/ci/knot_issues_sync.py --dry-run
    python tools/ci/knot_issues_sync.py --sync
"""

import argparse
import csv
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LC01_PATH = os.path.join(REPO_ROOT, "SSOT", "LC01_PROBLEM_STATEMENT")


def load_knots():
    """Load KNOTS.csv and return list of dicts."""
    knots_file = os.path.join(LC01_PATH, "KNOTS.csv")
    if not os.path.isfile(knots_file):
        print(f"KNOTS.csv not found at {knots_file}")
        return []
    with open(knots_file, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_knu_plan():
    """Load KNU_PLAN.csv and return list of dicts."""
    knu_file = os.path.join(LC01_PATH, "KNU_PLAN.csv")
    if not os.path.isfile(knu_file):
        print(f"KNU_PLAN.csv not found at {knu_file}")
        return []
    with open(knu_file, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def extract_ata_label(knot_id):
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
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="KNOT/KNU → GitHub Issues sync")
    parser.add_argument("--dry-run", action="store_true", help="Print issues without creating them")
    parser.add_argument("--sync", action="store_true", help="Create/update GitHub Issues (requires GITHUB_TOKEN)")
    args = parser.parse_args()

    if not args.dry_run and not args.sync:
        parser.error("Specify --dry-run or --sync")

    knots = load_knots()
    knus = load_knu_plan()

    if not knots:
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

        if args.dry_run:
            print(f"--- Issue: {title}")
            print(f"    Labels: {', '.join(labels)}")
            print(f"    KNUs: {sum(1 for k in knus if k['KNOT_ID'] == knot['KNOT_ID'])}")
            print()
        elif args.sync:
            print(f"SYNC not implemented in standalone mode — use GitHub Actions workflow")
            print(f"  Would create: {title}")

    print(f"✅ Processed {len(knots)} KNOTs")


if __name__ == "__main__":
    main()
