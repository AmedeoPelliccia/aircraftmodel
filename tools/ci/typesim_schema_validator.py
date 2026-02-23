#!/usr/bin/env python3
"""TypeSim OpenAPI schema validator.

Validates the TypeSim OpenAPI 3.0.0 specification for structural
correctness and AMPEL360-specific contract requirements.

Usage:
    python tools/ci/typesim_schema_validator.py --spec SSOT/LC05_ANALYSIS_MODELS/typesim-api/typesim-openapi.yaml
    python tools/ci/typesim_schema_validator.py --spec <path> --strict
"""

import argparse
import sys
from pathlib import Path

import yaml


# Required paths in the OpenAPI spec
REQUIRED_PATHS = ["/typesim/run", "/typesim/status", "/typesim/pnrd"]

# Required schemas in components
REQUIRED_SCHEMAS = [
    "TypeSimInput",
    "TypeSimOutput",
    "ModelState",
    "ConstraintSet",
    "Environment",
    "SimulatedState",
    "RiskVector",
    "ImpactMetrics",
    "GovernanceRecord",
    "ToplapStatus",
    "PNRDDeclaration",
]

# Required fields in GovernanceRecord
GOVERNANCE_REQUIRED = ["model_hash", "constraints_hash", "solver_versions", "mode", "PNRD_status"]

# TypeSimInput required fields
INPUT_REQUIRED = ["model", "constraints", "mode", "process_set_id", "run_id"]

# PNRD required fields
PNRD_REQUIRED = ["selected_solution_hash", "objective_hash", "constraints_hash", "authority"]


def validate_spec(spec_path: str, strict: bool = False) -> int:
    """Validate the TypeSim OpenAPI spec. Returns 0 on success, 1 on failure."""
    path = Path(spec_path)
    if not path.exists():
        print(f"❌ Spec file not found: {spec_path}")
        return 1

    with open(path) as f:
        try:
            spec = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"❌ YAML parse error: {e}")
            return 1

    errors = []
    warnings = []

    # Check OpenAPI version
    openapi_ver = spec.get("openapi", "")
    if not openapi_ver.startswith("3.0"):
        errors.append(f"OpenAPI version must be 3.0.x, got: {openapi_ver}")

    # Check info block
    info = spec.get("info", {})
    if "title" not in info:
        errors.append("Missing info.title")
    if "version" not in info:
        errors.append("Missing info.version")

    # Check required paths
    paths = spec.get("paths", {})
    for rp in REQUIRED_PATHS:
        if rp not in paths:
            errors.append(f"Missing required path: {rp}")

    # Check /typesim/run has POST
    run_path = paths.get("/typesim/run", {})
    if "post" not in run_path:
        errors.append("/typesim/run must have a POST operation")

    # Check /typesim/status has GET
    status_path = paths.get("/typesim/status", {})
    if "get" not in status_path:
        errors.append("/typesim/status must have a GET operation")

    # Check /typesim/pnrd has POST
    pnrd_path = paths.get("/typesim/pnrd", {})
    if "post" not in pnrd_path:
        errors.append("/typesim/pnrd must have a POST operation")

    # Check required schemas
    schemas = spec.get("components", {}).get("schemas", {})
    for rs in REQUIRED_SCHEMAS:
        if rs not in schemas:
            errors.append(f"Missing required schema: {rs}")

    # Validate GovernanceRecord required fields
    gov_schema = schemas.get("GovernanceRecord", {})
    gov_required = gov_schema.get("required", [])
    for field in GOVERNANCE_REQUIRED:
        if field not in gov_required:
            errors.append(f"GovernanceRecord missing required field: {field}")

    # Validate GovernanceRecord has hash chain fields
    gov_props = gov_schema.get("properties", {})
    for chain_field in ["prev_hash", "hash", "timestamp"]:
        if chain_field not in gov_props:
            errors.append(f"GovernanceRecord missing hash-chain field: {chain_field}")

    # Validate TypeSimInput required fields
    input_schema = schemas.get("TypeSimInput", {})
    input_required = input_schema.get("required", [])
    for field in INPUT_REQUIRED:
        if field not in input_required:
            errors.append(f"TypeSimInput missing required field: {field}")

    # Validate mode enum values
    input_props = input_schema.get("properties", {})
    mode_prop = input_props.get("mode", {})
    mode_enum = mode_prop.get("enum", [])
    for expected_mode in ["EXPLORATORY", "PROPAGATION"]:
        if expected_mode not in mode_enum:
            errors.append(f"TypeSimInput.mode missing enum value: {expected_mode}")

    # Validate PNRDDeclaration required fields
    pnrd_schema = schemas.get("PNRDDeclaration", {})
    pnrd_required = pnrd_schema.get("required", [])
    for field in PNRD_REQUIRED:
        if field not in pnrd_required:
            errors.append(f"PNRDDeclaration missing required field: {field}")

    # Validate ToplapStatus has state bounds
    toplap_schema = schemas.get("ToplapStatus", {})
    toplap_props = toplap_schema.get("properties", {})
    toplap_state = toplap_props.get("TOPLAP_STATE", {})
    if toplap_state.get("maximum") != 6:
        warnings.append("ToplapStatus.TOPLAP_STATE should have maximum: 6")

    # Validate ImpactMetrics has FPAI
    impact_schema = schemas.get("ImpactMetrics", {})
    impact_props = impact_schema.get("properties", {})
    if "HORIZON_FPAI_360" not in impact_props:
        errors.append("ImpactMetrics missing HORIZON_FPAI_360")
    if "EEI" not in impact_props:
        warnings.append("ImpactMetrics missing EEI (Energy Efficiency Index)")

    # Validate ModelState has toplap_state
    model_schema = schemas.get("ModelState", {})
    model_props = model_schema.get("properties", {})
    if "toplap_state" not in model_props:
        errors.append("ModelState missing toplap_state field")

    # Report results
    if warnings:
        for w in warnings:
            print(f"⚠️  {w}")

    if errors:
        for e in errors:
            print(f"❌ {e}")
        print(f"\n❌ Validation FAILED — {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    if strict and warnings:
        print(f"\n❌ Strict mode: {len(warnings)} warning(s) treated as errors")
        return 1

    print(f"✅ TypeSim API spec valid — {len(REQUIRED_SCHEMAS)} schemas, "
          f"{len(REQUIRED_PATHS)} paths, {len(warnings)} warning(s)")
    return 0


def main():
    parser = argparse.ArgumentParser(description="TypeSim OpenAPI schema validator")
    parser.add_argument(
        "--spec",
        default="SSOT/LC05_ANALYSIS_MODELS/typesim-api/typesim-openapi.yaml",
        help="Path to the TypeSim OpenAPI spec (default: SSOT/LC05_ANALYSIS_MODELS/typesim-api/typesim-openapi.yaml)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors",
    )
    args = parser.parse_args()
    sys.exit(validate_spec(args.spec, args.strict))


if __name__ == "__main__":
    main()
