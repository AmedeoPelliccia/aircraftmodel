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

try:
    import yaml
except ImportError:
    yaml = None

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

ASKM_DIRS = [
    ".askm/observer",
    ".askm/delineant",
]

ASIT_DIRS = [
    ".asit/agents",
    ".asit/operator",
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
            severity = "ERROR" if strict else "WARNING"
            label_prefix = f"{label}: " if label else ""
            msg = f"{severity}: {label_prefix}missing directory {d}"
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


def check_askm_governance():
    """Validate .askm/ governance configuration consistency."""
    errors = []
    warnings = []

    # Check that config.yaml exists in each .askm/ subdirectory
    for subdir in ["observer", "delineant"]:
        config_path = os.path.join(REPO_ROOT, ".askm", subdir, "config.yaml")
        if not os.path.isfile(config_path):
            errors.append(f"MISSING: .askm/{subdir}/config.yaml")
            continue

        if yaml is None:
            warnings.append("PyYAML not installed — skipping YAML content checks")
            continue

        try:
            with open(config_path) as f:
                config = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            errors.append(f"INVALID YAML in .askm/{subdir}/config.yaml: {exc}")
            continue

        if not isinstance(config, dict):
            errors.append(f"INVALID: .askm/{subdir}/config.yaml is not a YAML mapping")
            continue

        # Observer must not declare delta_class: STRUCTURAL
        if subdir == "observer":
            delta_class = config.get("delta_class", "NONE")
            if delta_class == "STRUCTURAL":
                errors.append(
                    "GOVERNANCE VIOLATION: .askm/observer/config.yaml declares "
                    "delta_class: STRUCTURAL — observer cannot produce structural deltas"
                )

        # Delineant must declare requires_observer_baseline: true
        if subdir == "delineant":
            if not config.get("requires_observer_baseline", False):
                errors.append(
                    "GOVERNANCE VIOLATION: .askm/delineant/config.yaml must declare "
                    "requires_observer_baseline: true"
                )

    return errors, warnings


def check_asit_consistency():
    """Validate .asit/ agent and operator enforcement consistency."""
    errors = []
    warnings = []

    if yaml is None:
        warnings.append("PyYAML not installed — skipping .asit/ content checks")
        return errors, warnings

    # Check that agent configs reference valid modes from .askm/
    agents_dir = os.path.join(REPO_ROOT, ".asit", "agents")
    if os.path.isdir(agents_dir):
        for fname in os.listdir(agents_dir):
            if not fname.endswith(".yaml"):
                continue
            fpath = os.path.join(agents_dir, fname)
            try:
                with open(fpath) as f:
                    agent = yaml.safe_load(f)
            except yaml.YAMLError as exc:
                errors.append(f"INVALID YAML in .asit/agents/{fname}: {exc}")
                continue

            if not isinstance(agent, dict):
                continue

            modes = agent.get("modes", [])
            for mode_entry in modes:
                if not isinstance(mode_entry, dict):
                    continue
                mode_name = mode_entry.get("mode", "")
                config_ref = mode_entry.get("config_ref", "")
                if config_ref:
                    ref_path = os.path.join(REPO_ROOT, config_ref)
                    if not os.path.isfile(ref_path):
                        errors.append(
                            f"BROKEN REF in .asit/agents/{fname}: "
                            f"mode {mode_name} references {config_ref} which does not exist"
                        )

    # Check enforcement rules cover required forbidden operations
    enforcement_path = os.path.join(REPO_ROOT, ".asit", "operator", "enforcement-rules.yaml")
    if os.path.isfile(enforcement_path):
        try:
            with open(enforcement_path) as f:
                enforcement = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            errors.append(f"INVALID YAML in .asit/operator/enforcement-rules.yaml: {exc}")
            return errors, warnings

        if isinstance(enforcement, dict):
            forbidden_ops = enforcement.get("forbidden_cross_mode_operations", [])
            required_ops = [
                "OBSERVER_cannot_emit_MODEL_DELTA",
                "DELINEANT_cannot_emit_STATE_CAPTURE_without_source",
            ]
            for op in required_ops:
                if op not in forbidden_ops:
                    errors.append(
                        f"GOVERNANCE GAP: .asit/operator/enforcement-rules.yaml "
                        f"missing required forbidden operation: {op}"
                    )

    return errors, warnings


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
            (".askm governance", ASKM_DIRS),
            (".asit enforcement", ASIT_DIRS),
        ]:
            e, w = check_dirs(dirs, label, args.strict)
            all_errors.extend(e)
            all_warnings.extend(w)

    bin_errors = check_ssot_no_binaries()
    all_errors.extend(bin_errors)

    # GEN-MODEL governance checks
    askm_errors, askm_warnings = check_askm_governance()
    all_errors.extend(askm_errors)
    all_warnings.extend(askm_warnings)

    asit_errors, asit_warnings = check_asit_consistency()
    all_errors.extend(asit_errors)
    all_warnings.extend(asit_warnings)

    for w in all_warnings:
        print(f"  WARN: {w}")
    for e in all_errors:
        print(f"  ERROR: {e}")

    if all_errors:
        print(f"\n❌ Validation FAILED — {len(all_errors)} error(s), {len(all_warnings)} warning(s)")
        sys.exit(1)
    else:
        total_checked = (len(REQUIRED_AXES) + len(ATA28_DIRS) + len(ATA47_DIRS)
                        + len(SSOT_DIRS) + len(PUB_DIRS)
                        + len(ASKM_DIRS) + len(ASIT_DIRS))
        if args.chapter:
            total_checked = len(CHAPTER_MAP.get(args.chapter, []))
        print(f"✅ Validation PASSED — {total_checked} directories checked, {len(all_warnings)} warning(s)")
        sys.exit(0)


if __name__ == "__main__":
    main()
