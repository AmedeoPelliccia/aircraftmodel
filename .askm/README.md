# `.askm/` — GEN-MODEL Role Configuration

## Purpose

This directory defines the two operational modes of the GEN-MODEL layer
for LC05 Analysis Models:

| Mode        | Directory              | Function                     |
|-------------|------------------------|------------------------------|
| **Observer**  | `.askm/observer/`    | Read-only state extraction   |
| **Delineant** | `.askm/delineant/`   | Structural write (gated)     |

## Formal Specification

See: `SSOT/LC05_ANALYSIS_MODELS/LC05-GEN-MODEL-ROLE-SPEC.md`
(KNU-ATA96-70-001)

## Governance

Mode separation is enforced at three layers:

1. **Pre-commit hook** — `.github/hooks/pre-commit` (Rules 4–5)
2. **CI workflow** — `.github/workflows/gen-model-validation.yml`
3. **Structure validator** — `tools/ci/optin_structure_validator.py`

## Agent Binding

The `.asit/agents/gen-model-agent.yaml` registry binds agent instances
to the modes defined here. See `.asit/README.md`.

## Traceability

- KNOT: `KNOT-ATA96-70-00-001`
- KNU: `KNU-ATA96-70-001`
- Programme: ID-A360-Q100 · AMPEL360
