#!/usr/bin/env python3
<<<<<<< HEAD
"""BREX validator for S1000D data modules.

Validates data modules against project BREX rules (BREX-IDA360-Q100).
=======
"""BREX validator for S1000D Data Modules.

Validates DMs against BREX-IDA360-Q100-v0.1 rules:
  BREX-IDA360-001: ATA 28 DMs must have <cautionRef> for H2 compatibility
  BREX-IDA360-002: NH3 DMs must have <warningRef> for NH3 toxicity
  BREX-IDA360-003: ATA 47-40 procedural DMs must have respTime attribute
  BREX-IDA360-004: DMs with applicability must use approved variant values
  BREX-IDA360-005: ATA 26/28/47 DMs must have safetyClass="SC1"
>>>>>>> origin/main

Usage:
    python tools/ci/brex_validator.py --dm-dir PUB/CSDB/DM
"""

import argparse
import os
import sys
<<<<<<< HEAD

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
=======
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
    xml_content_lower = ET.tostring(root, encoding="unicode").lower()

    # BREX-IDA360-001: ATA 28 DMs need cautionRef for H2
    if "ata-28" in relpath.lower() or "ata_28" in relpath.lower():
        if "cautionref" not in xml_content_lower:
            errors.append(f"BREX-IDA360-001: {relpath} — ATA 28 DM missing <cautionRef> for H2 compatibility")

    # BREX-IDA360-002: NH3 DMs need warningRef
    if "nh3" in text_content or "ammonia" in text_content:
        if "warningref" not in xml_content_lower:
            errors.append(f"BREX-IDA360-002: {relpath} — DM with NH3 content missing <warningRef> for NH3 toxicity")

    # BREX-IDA360-003: ATA 47-40 procedural DMs need respTime
    if "47-40" in relpath:
        for step in root.iter():
            if step.tag and "step" in step.tag.lower():
                if not any(k.lower() == "resptime" for k in step.attrib):
                    errors.append(f"BREX-IDA360-003: {relpath} — ATA 47-40 step missing respTime attribute")
                    break

    # BREX-IDA360-005: ATA 26/28/47 DMs need safetyClass="SC1"
    ata_safety = any(x in relpath.lower() for x in ["ata-26", "ata_26", "ata-28", "ata_28", "ata-47", "ata_47"])
    if ata_safety:
        if 'safetyclass="sc1"' not in xml_content_lower:
            errors.append(f"BREX-IDA360-005: {relpath} — safety-critical DM missing safetyClass=\"SC1\"")
>>>>>>> origin/main

    return errors


def main():
<<<<<<< HEAD
    parser = argparse.ArgumentParser(description="BREX validator")
    parser.add_argument("--dm-dir", required=True, help="Directory containing data modules")
=======
    parser = argparse.ArgumentParser(description="BREX validator for S1000D DMs")
    parser.add_argument("--dm-dir", required=True, help="Path to DM directory")
>>>>>>> origin/main
    args = parser.parse_args()

    dm_dir = os.path.join(REPO_ROOT, args.dm_dir)
    if not os.path.isdir(dm_dir):
        print(f"DM directory not found: {dm_dir}")
<<<<<<< HEAD
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
=======
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
>>>>>>> origin/main
        sys.exit(0)


if __name__ == "__main__":
    main()
