#!/usr/bin/env python3
"""OPT-IN Framework structure validator.

Checks that the repository follows the OPT-IN 5-axis topology,
required ATA directories exist, and SSOT contains no binary deliverables.

Usage:
    python tools/ci/optin_structure_validator.py --check
"""

import argparse
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

REQUIRED_AXES = [
    "OPT-IN_FRAMEWORK/O-ORGANIZATIONS",
    "OPT-IN_FRAMEWORK/P-PROGRAMS",
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES",
    "OPT-IN_FRAMEWORK/I-INFRASTRUCTURES",
    "OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS",
]

ATA28_DIRS = [
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/C2-CIRCULAR_CRYOGENIC_CELLS/ATA_28-FUEL",
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/C2-CIRCULAR_CRYOGENIC_CELLS/ATA_28-FUEL/28-10-storage-reservoir",
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/C2-CIRCULAR_CRYOGENIC_CELLS/ATA_28-FUEL/28-20-distribution",
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/C2-CIRCULAR_CRYOGENIC_CELLS/ATA_28-FUEL/28-30-dump-jettison",
    "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/C2-CIRCULAR_CRYOGENIC_CELLS/ATA_28-FUEL/28-40-indicating",
]

ATA47_DIRS = []  # placeholder for future ATA 47 validation

SSOT_DIRS = [
    "SSOT/LC01_PROBLEM_STATEMENT",
]

PUB_DIRS = [
    "PUB/CSDB/BREX",
    "PUB/CSDB/DM",
    "PUB/EXPORT",
]

CHAPTER_MAP = {
    "ATA_28": ATA28_DIRS,
    "ATA_47": ATA47_DIRS,
}

BINARY_EXTENSIONS = {".pdf", ".html", ".docx", ".xlsx"}


def check_dirs(dirs, label, strict=True):
    """Check that all directories in the list exist."""
    errors = []
    for d in dirs:
        full = os.path.join(REPO_ROOT, d)
        if not os.path.isdir(full):
            msg = f"[{label}] Missing directory: {d}"
            errors.append(msg)
    return errors


def check_ssot_no_binaries():
    """Check that SSOT/ contains no binary deliverables."""
    errors = []
    ssot_path = os.path.join(REPO_ROOT, "SSOT")
    if not os.path.isdir(ssot_path):
        return errors
    for root, _dirs, files in os.walk(ssot_path):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in BINARY_EXTENSIONS:
                rel = os.path.relpath(os.path.join(root, f), REPO_ROOT)
                errors.append(f"[SSOT] Binary file not allowed: {rel}")
    return errors


def main():
    parser = argparse.ArgumentParser(description="OPT-IN structure validator")
    parser.add_argument("--check", action="store_true", help="Run all checks")
    parser.add_argument("--chapter", help="Validate a specific ATA chapter (e.g. ATA_28)")
    args = parser.parse_args()

    if not args.check and not args.chapter:
        parser.print_help()
        sys.exit(0)

    errors = []

    if args.check:
        errors.extend(check_dirs(REQUIRED_AXES, "OPT-IN axes"))
        errors.extend(check_dirs(ATA28_DIRS, "ATA 28"))
        errors.extend(check_dirs(SSOT_DIRS, "SSOT"))
        errors.extend(check_dirs(PUB_DIRS, "PUB"))
        errors.extend(check_ssot_no_binaries())

    if args.chapter:
        chapter_dirs = CHAPTER_MAP.get(args.chapter, [])
        if not chapter_dirs:
            print(f"No validation rules for chapter: {args.chapter}")
            sys.exit(0)
        errors.extend(check_dirs(chapter_dirs, args.chapter))

    if errors:
        print(f"FAIL — {len(errors)} error(s):")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    else:
        print("PASS — structure valid")
        sys.exit(0)


if __name__ == "__main__":
    main()
