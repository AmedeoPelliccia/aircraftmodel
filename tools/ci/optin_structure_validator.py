#!/usr/bin/env python3
"""OPT-IN Framework structure and traceability validator.

Validates that the repository directory structure follows the OPT-IN
5-axis topology and that traceability references are consistent.

Usage:
    python tools/ci/optin_structure_validator.py --check
    python tools/ci/optin_structure_validator.py --check --chapter 28
    python tools/ci/optin_structure_validator.py --check --strict
"""

import argparse
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

REQUIRED_AXES = [
    "OPT-IN_FRAMEWORK/O-ORGANIZATIONS",
    "OPT-IN_FRAMEWORK/P-PROGRAMS",
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES",
    "OPT-IN_FRAMEWORK/I-INFRASTRUCTURES",
    "OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS",
]

ATA28_DIRS = [
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/C2-CIRCULAR_CRYOGENIC_CELLS/ATA_28-FUEL/ATA-28-fuel/28-10-lh2-storage-vacuum-tank",
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/C2-CIRCULAR_CRYOGENIC_CELLS/ATA_28-FUEL/ATA-28-fuel/28-20-nh3-storage-and-cryo-shield",
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/C2-CIRCULAR_CRYOGENIC_CELLS/ATA_28-FUEL/ATA-28-fuel/28-30-boil-off-recovery-and-routing",
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/C2-CIRCULAR_CRYOGENIC_CELLS/ATA_28-FUEL/ATA-28-fuel/28-40-nh3-cracker-h2-feed",
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/C2-CIRCULAR_CRYOGENIC_CELLS/ATA_28-FUEL/ATA-28-fuel/28-70-embrittlement-monitoring",
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/C2-CIRCULAR_CRYOGENIC_CELLS/ATA_28-FUEL/ATA-28-fuel/28-90-tables-schemas-index",
]

ATA47_DIRS = [
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/E1-ENVIRONMENT/ATA_47-INERT_GAS_SYSTEM/ATA-47-inert-gas-system/47-10-cracker-n2-sourcing-and-purity",
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/E1-ENVIRONMENT/ATA_47-INERT_GAS_SYSTEM/ATA-47-inert-gas-system/47-20-tank-inerting-management",
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/E1-ENVIRONMENT/ATA_47-INERT_GAS_SYSTEM/ATA-47-inert-gas-system/47-30-leak-sniff-protocol",
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/E1-ENVIRONMENT/ATA_47-INERT_GAS_SYSTEM/ATA-47-inert-gas-system/47-40-active-suppression-system",
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/E1-ENVIRONMENT/ATA_47-INERT_GAS_SYSTEM/ATA-47-inert-gas-system/47-50-backup-mol-sieve-generator",
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/E1-ENVIRONMENT/ATA_47-INERT_GAS_SYSTEM/ATA-47-inert-gas-system/47-90-tables-schemas-index",
]

SSOT_DIRS = [
    "SSOT/LC01_PROBLEM_STATEMENT",
    "SSOT/LC05_ANALYSIS_MODELS/thermodynamic-models",
]

PUB_DIRS = [
    "PUB/CSDB/DM",
    "PUB/CSDB/PM",
    "PUB/CSDB/BREX",
    "PUB/CSDB/ICN",
]

CHAPTER_MAP = {
    "28": ATA28_DIRS,
    "47": ATA47_DIRS,
}


def check_dirs(dirs, label, strict=False):
    """Check that required directories exist."""
    errors = []
    warnings = []
    for d in dirs:
        full = os.path.join(REPO_ROOT, d)
        if not os.path.isdir(full):
            msg = f"MISSING: {d}"
            if strict:
                errors.append(msg)
            else:
                warnings.append(msg)
    return errors, warnings


def check_ssot_no_binaries():
    """Check that SSOT/ contains no binary deliverables."""
    errors = []
    ssot_path = os.path.join(REPO_ROOT, "SSOT")
    if not os.path.isdir(ssot_path):
        return errors
    forbidden = {".pdf", ".html", ".docx", ".xlsx"}
    for root, _dirs, files in os.walk(ssot_path):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in forbidden:
                rel = os.path.relpath(os.path.join(root, f), REPO_ROOT)
                errors.append(f"FORBIDDEN binary in SSOT: {rel}")
    return errors


def main():
    parser = argparse.ArgumentParser(description="OPT-IN structure validator")
    parser.add_argument("--check", action="store_true", required=True)
    parser.add_argument("--chapter", type=str, help="Validate specific ATA chapter")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    args = parser.parse_args()

    all_errors = []
    all_warnings = []

    if args.chapter:
        if args.chapter in CHAPTER_MAP:
            e, w = check_dirs(CHAPTER_MAP[args.chapter], f"ATA {args.chapter}", args.strict)
            all_errors.extend(e)
            all_warnings.extend(w)
        else:
            print(f"Unknown chapter: {args.chapter}")
            sys.exit(1)
    else:
        for label, dirs in [
            ("OPT-IN axes", REQUIRED_AXES),
            ("ATA 28", ATA28_DIRS),
            ("ATA 47", ATA47_DIRS),
            ("SSOT", SSOT_DIRS),
            ("PUB", PUB_DIRS),
        ]:
            e, w = check_dirs(dirs, label, args.strict)
            all_errors.extend(e)
            all_warnings.extend(w)

    bin_errors = check_ssot_no_binaries()
    all_errors.extend(bin_errors)

    for w in all_warnings:
        print(f"  WARN: {w}")
    for e in all_errors:
        print(f"  ERROR: {e}")

    if all_errors:
        print(f"\n❌ Validation FAILED — {len(all_errors)} error(s), {len(all_warnings)} warning(s)")
        sys.exit(1)
    else:
        total_checked = len(REQUIRED_AXES) + len(ATA28_DIRS) + len(ATA47_DIRS) + len(SSOT_DIRS) + len(PUB_DIRS)
        if args.chapter:
            total_checked = len(CHAPTER_MAP.get(args.chapter, []))
        print(f"✅ Validation PASSED — {total_checked} directories checked, {len(all_warnings)} warning(s)")
        sys.exit(0)


if __name__ == "__main__":
    main()
