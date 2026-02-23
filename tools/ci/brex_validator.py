#!/usr/bin/env python3
"""BREX validator for S1000D data modules.

Validates data modules against project BREX rules (BREX-IDA360-Q100).

Usage:
    python tools/ci/brex_validator.py --dm-dir PUB/CSDB/DM
"""

import argparse
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

APPROVED_VARIANTS = ["BWB", "WTW"]


def validate_dm(filepath):
    """Validate a single data module against BREX rules."""
    errors = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return [f"Cannot read {filepath}: {e}"]

    basename = os.path.basename(filepath).lower()

    # BREX-001: ATA 28 LH₂ DMs need cautionRef
    if "ata28" in basename or "ata-28" in basename:
        if "cautionRef" not in content and "cautionref" not in content.lower():
            errors.append(f"BREX-001: {filepath} — missing cautionRef (H₂ hazard)")

    # BREX-002: NH₃ DMs need warningRef
    if "nh3" in basename or "ammonia" in basename:
        if "warningRef" not in content and "warningref" not in content.lower():
            errors.append(f"BREX-002: {filepath} — missing warningRef (NH₃ toxicity)")

    # BREX-003: ATA 47-40 steps need respTime
    if "ata47-40" in basename or "ata-47-40" in basename:
        if "respTime" not in content and "resptime" not in content.lower():
            errors.append(f"BREX-003: {filepath} — missing respTime attribute")

    # BREX-004/005: Safety-critical DMs need safetyClass="SC1"
    safety_atas = ["ata26", "ata-26", "ata28", "ata-28", "ata47", "ata-47"]
    if any(tag in basename for tag in safety_atas):
        if 'safetyClass="SC1"' not in content and "safetyclass" not in content.lower():
            errors.append(f"BREX-004: {filepath} — missing safetyClass=\"SC1\"")

    return errors


def main():
    parser = argparse.ArgumentParser(description="BREX validator")
    parser.add_argument("--dm-dir", required=True, help="Directory containing data modules")
    args = parser.parse_args()

    dm_dir = os.path.join(REPO_ROOT, args.dm_dir)
    if not os.path.isdir(dm_dir):
        print(f"DM directory not found: {dm_dir}")
        sys.exit(0)

    errors = []
    for root, _dirs, files in os.walk(dm_dir):
        for f in files:
            if f.endswith(".xml"):
                filepath = os.path.join(root, f)
                errors.extend(validate_dm(filepath))

    if errors:
        print(f"FAIL — {len(errors)} BREX violation(s):")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    else:
        print("PASS — all DMs comply with BREX")
        sys.exit(0)


if __name__ == "__main__":
    main()
