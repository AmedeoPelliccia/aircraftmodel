# ATA 25 — Equipment / Furnishings — BWB Programme Extension

**Domain:** T-TECHNOLOGIES / A-AIRFRAME_CABINS
**Boundary:** PROGRAMME_EXT / BWB (variant overlay)
**Doc ID:** T-A-ATA25-BWB-001
**Lifecycle:** Standard (LC01–LC13)

## Scope

BWB-only deltas to ATA 25 baseline (SHARED) for AMPEL360 BWB (EIS 2042–48).
This folder SHALL NOT duplicate SHARED content except as traceable delta statements.

## Overlay Rules

- SHARED baseline location: `../../` (ATA_25 root)
- This overlay provides: ΔREQ, ΔICD, ΔAcceptability, ΔEvidence
- Precedence: Type design basis > approved data > SHARED ATA25 > BWB overlay > local WI

## Contents

| File / Folder | Description |
|---------------|-------------|
| `ATA25_BWB_INDEX.yaml` | Delta index — SSOT for all BWB ATA 25 deviations |
| `ATA25_BWB_DELTA_LOG.yaml` | Auditable change log of delta evolution |
| `ATA25_BWB_COMPLIANCE_MATRIX.md` | CS-25 compliance traceability for BWB-specific requirements |
| `ATA25_BWB_INTERFACES/` | Cabin envelope, floor grid, monuments, stowage, egress clearances |
| `ATA25_BWB_REQUIREMENTS/` | BWB-only requirements by ATA 25 subchapter |
| `ATA25_BWB_ACCEPTABILITY/` | BWB-specific tolerances, clearances, rework and damage limits |
| `ATA25_BWB_VERIFICATION_EVIDENCE/` | Analysis/test/inspection objects linked to BWB deltas |

## Key BWB-Specific Deltas

The BWB configuration drives unique ATA 25 deltas primarily in:

- **Floor grid / attach philosophy** — distributed loads, non-tube structural attach patterns
- **Monument load paths** — galleys/lavs/stowage anchored to wide-body composite structure
- **Egress geometry** — radial aisle flow, clearances across wider planform, multi-zone evacuation
- **Stowage distribution** — bins/closets affect CG and load distribution differently across BWB span
- **Maintenance access** — panels, underfloor zones, monument removal envelopes in composite bay

## LC Phase Gating

| LC Gate | Content added |
|---------|--------------|
| LC01–LC02 | Scaffold + delta index + requirement titles only |
| LC03 | ICDs (envelope, floor grid, monuments, stowage, egress) + thresholds |
| LC04–LC05 | Acceptability rules + verification plan skeleton |
| LC06–LC09 | Evidence objects (test/analysis/inspection) with trace links |
| LC10–LC13 | Operational feedback + lessons-learned deltas |

## Cross-References

Common interacting ATAs:

- ATA 11 (Placards/Markings), ATA 21 (ECS), ATA 23 (Comm), ATA 24 (Electrical)
- ATA 26 (Fire Protection), ATA 33 (Lights), ATA 35 (Oxygen)
- ATA 38 (Water/Waste), ATA 44 (Cabin Systems), ATA 52 (Doors)
- ATA 53/56/57 (Structure)

## Related Documents

- ATA 25 baseline (SHARED): [../../README.md](../../README.md)
- WTW overlay (parallel): [../WTW/README.md](../WTW/README.md)
- Lifecycle registry: [../../../../lifecycle/LC_PHASE_REGISTRY.yaml](../../../../lifecycle/LC_PHASE_REGISTRY.yaml)
