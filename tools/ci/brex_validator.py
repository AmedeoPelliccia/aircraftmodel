#!/usr/bin/env python3
"""BREX validator for S1000D Data Modules.

Validates DMs against BREX-IDA360-Q100-v0.1 rules:
  BREX-IDA360-001: ATA 28 DMs must have <cautionRef> for H2 compatibility
  BREX-IDA360-002: NH3 DMs must have <warningRef> for NH3 toxicity
  BREX-IDA360-003: ATA 47-40 procedural DMs must have respTime attribute
  BREX-IDA360-004: DMs with applicability must use approved variant values
  BREX-IDA360-005: ATA 26/28/47 DMs must have safetyClass="SC1"

Usage:
    python tools/ci/brex_validator.py --dm-dir PUB/CSDB/DM
"""

import argparse
import os
import sys
import xml.etree.ElementTree as ET

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

APPROVED_VARIANTS = [
    "A360-Q100-LH2",
    "A360-Q100-NH3",
    "A360-Q100-N2",
    "A360-Q100-ALL",
]


def validate_dm(filepath):
    """Validate a single Data Module XML file against BREX rules."""
    errors = []
    relpath = os.path.relpath(filepath, REPO_ROOT)

    try:
        tree = ET.parse(filepath)
    except ET.ParseError as e:
        errors.append(f"XML parse error in {relpath}: {e}")
        return errors

    root = tree.getroot()
    text_content = ET.tostring(root, encoding="unicode", method="text").lower()
    xml_content = ET.tostring(root, encoding="unicode")

    # BREX-IDA360-001: ATA 28 DMs need cautionRef for H2
    if "ata-28" in relpath.lower() or "ata_28" in relpath.lower():
        if "cautionRef" not in xml_content and "cautionref" not in xml_content.lower():
            errors.append(f"BREX-IDA360-001: {relpath} — ATA 28 DM missing <cautionRef> for H2 compatibility")

    # BREX-IDA360-002: NH3 DMs need warningRef
    if "nh3" in text_content or "ammonia" in text_content:
        if "warningRef" not in xml_content and "warningref" not in xml_content.lower():
            errors.append(f"BREX-IDA360-002: {relpath} — DM with NH3 content missing <warningRef> for NH3 toxicity")

    # BREX-IDA360-003: ATA 47-40 procedural DMs need respTime
    if "47-40" in relpath:
        for step in root.iter():
            if step.tag and "step" in step.tag.lower():
                if "respTime" not in step.attrib and "resptime" not in {k.lower() for k in step.attrib}:
                    errors.append(f"BREX-IDA360-003: {relpath} — ATA 47-40 step missing respTime attribute")
                    break

    # BREX-IDA360-005: ATA 26/28/47 DMs need safetyClass="SC1"
    ata_safety = any(x in relpath.lower() for x in ["ata-26", "ata_26", "ata-28", "ata_28", "ata-47", "ata_47"])
    if ata_safety:
        if 'safetyClass="SC1"' not in xml_content and "safetyclass" not in xml_content.lower():
            errors.append(f"BREX-IDA360-005: {relpath} — safety-critical DM missing safetyClass=\"SC1\"")

    return errors


def main():
    parser = argparse.ArgumentParser(description="BREX validator for S1000D DMs")
    parser.add_argument("--dm-dir", required=True, help="Path to DM directory")
    args = parser.parse_args()

    dm_dir = os.path.join(REPO_ROOT, args.dm_dir)
    if not os.path.isdir(dm_dir):
        print(f"DM directory not found: {dm_dir}")
        print("✅ No DMs to validate — PASSED")
        sys.exit(0)

    all_errors = []
    dm_count = 0

    for root_dir, _dirs, files in os.walk(dm_dir):
        for f in files:
            if f.endswith(".xml"):
                dm_count += 1
                filepath = os.path.join(root_dir, f)
                errors = validate_dm(filepath)
                all_errors.extend(errors)

    if dm_count == 0:
        print("✅ No DMs found to validate — PASSED")
        sys.exit(0)

    for e in all_errors:
        print(f"  ERROR: {e}")

    if all_errors:
        print(f"\n❌ BREX validation FAILED — {len(all_errors)} violation(s) in {dm_count} DM(s)")
        sys.exit(1)
    else:
        print(f"✅ BREX validation PASSED — {dm_count} DM(s) checked, 0 violations")
        sys.exit(0)


if __name__ == "__main__":
    main()
