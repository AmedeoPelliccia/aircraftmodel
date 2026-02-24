# ATA 25 — Equipment / Furnishings — WTW Programme Extension

**Domain:** T-TECHNOLOGIES / A-AIRFRAME_CABINS
**Boundary:** PROGRAMME_EXT / WTW (variant overlay)
**Doc ID:** T-A-ATA25-WTW-001
**Lifecycle:** Standard (LC01–LC13)

## Scope

WTW-only deltas to ATA 25 baseline practices and requirements for AMPEL360 Q100.
This folder SHALL NOT duplicate SHARED content except as traceable excerpts.

## Overlay Rules

- SHARED baseline location: `../` (ATA_25 root)
- This overlay provides: ΔREQ, ΔICD, ΔAcceptability, ΔEvidence
- Conflicts resolved by: Type design basis > SRM/CMM > SHARED ATA25 > WTW overlay > local WI

## Contents

| File / Folder | Description |
|---------------|-------------|
| `ATA25_WTW_INDEX.yaml` | Index of all WTW delta items (SSOT) |
| `ATA25_WTW_DELTA_LOG.yaml` | Auditable change log of delta evolution |
| `ATA25_WTW_COMPLIANCE_MATRIX.md` | CS-25 compliance traceability for WTW-specific requirements |
| `ATA25_WTW_INTERFACES/` | WTW cabin geometry, attach points, access, installation constraints |
| `ATA25_WTW_REQUIREMENTS/` | WTW-only requirements by ATA 25 subchapter |
| `ATA25_WTW_ACCEPTABILITY/` | WTW-specific acceptability limits and rework rules |
| `ATA25_WTW_VERIFICATION_EVIDENCE/` | Evidence objects linked to WTW deltas (test/analysis/inspection) |

## LC Phase Gating

| LC Gate | Content added |
|---------|--------------|
| LC01–LC02 | Scaffold + delta index + requirement titles only |
| LC03 | ICDs (geometry, attach points, access) + requirement thresholds |
| LC04–LC05 | Acceptability rules + verification plan skeleton |
| LC06–LC09 | Evidence objects (test/analysis/inspection) with trace links |
| LC10–LC13 | Operational feedback + lessons-learned deltas |

## Cross-References

Typical impacted ATAs:

- ATA 11 (Placards/Markings), ATA 21 (ECS), ATA 24 (Electrical)
- ATA 26 (Fire Protection), ATA 38 (Water/Waste)
- ATA 44 (Cabin Systems), ATA 52 (Doors), ATA 53/56/57 (Structure)

## Related Documents

- ATA 25 baseline (SHARED): [../README.md](../README.md)
- Lifecycle registry: [../../../../lifecycle/LC_PHASE_REGISTRY.yaml](../../../../lifecycle/LC_PHASE_REGISTRY.yaml)
