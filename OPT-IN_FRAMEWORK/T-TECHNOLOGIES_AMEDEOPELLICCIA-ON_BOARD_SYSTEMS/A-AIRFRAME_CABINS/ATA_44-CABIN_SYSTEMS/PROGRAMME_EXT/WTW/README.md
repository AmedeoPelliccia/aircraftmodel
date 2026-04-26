# ATA 44 — Cabin Systems — WTW Programme Extension

**Domain:** T-TECHNOLOGIES / A-AIRFRAME_CABINS
**Boundary:** PROGRAMME_EXT / WTW (variant overlay)
**Doc ID:** T-A-ATA44-WTW-001
**Lifecycle:** Standard (LC01–LC13)

## Scope

WTW-only deltas to ATA 44 baseline (SHARED) for AMPEL360 WTW (EIS 2035–40).
This folder SHALL NOT duplicate SHARED content except as traceable delta statements.

ATA 44 covers the Cabin Systems domain: Cabin Core System (44-10), In-Flight Entertainment
(44-20), External Communication (44-30), Cabin Mass Memory (44-40), Cabin Monitoring
(44-50), and Miscellaneous Cabin Systems (44-60).

## Overlay Rules

- SHARED baseline location: `../../` (ATA_44 root)
- This overlay provides: ΔREQ, ΔICD, ΔARCH, ΔAcceptability, ΔEvidence
- Precedence: Type design basis > approved data > SHARED ATA44 > WTW overlay > local WI

## Contents

| File / Folder | Description |
|---------------|-------------|
| `ATA44_WTW_INDEX.yaml` | Delta index — SSOT for all WTW ATA 44 deviations |
| `ATA44_WTW_DELTA_LOG.yaml` | Auditable change log of delta evolution |
| `ATA44_WTW_COMPLIANCE_MATRIX.md` | CS-25 / ED-14 compliance traceability for WTW-specific requirements |
| `ATA44_WTW_ARCHITECTURE/` | WTW topology overview, zone definition, network/ICD models |
| `ATA44_WTW_INTERFACES/` | Controller placement, wiring route envelopes, network endpoints |
| `ATA44_WTW_REQUIREMENTS/` | WTW-only requirements by ATA 44 subchapter |
| `ATA44_WTW_ACCEPTABILITY/` | WTW-specific installation limits, dispatch rules, MEL impact |
| `ATA44_WTW_VERIFICATION_EVIDENCE/` | Analysis/test/inspection objects linked to WTW deltas |

## WTW-Specific Cabin Systems Drivers

| Driver | WTW Characteristic |
|--------|-------------------|
| Fuselage topology | Circular single-aisle/twin-aisle tube with longitudinal harness run |
| CMS controller placement | Forward E/E bay + AFT bay LRU cabinets |
| IFE server location | Forward avionics + distributed satellite units per cabin zone |
| PA/crew call | Linear zone topology, fore-to-aft sequential addressing |
| Cabin monitoring | Conventional ring/bus topology across 2–4 zones |
| Network backbone | ARINC 664 (AFDX) cabin domain, 100 Mbit/s passenger-network |

## LC Phase Gating

| LC Gate | Content added |
|---------|--------------|
| LC01–LC02 | Scaffold + delta index + architecture overview |
| LC03 | Interface data (controller/server locations, wiring envelopes, endpoints) |
| LC04–LC05 | Requirement thresholds + acceptability limits |
| LC06–LC09 | Verification evidence (test/analysis/inspection) |
| LC10–LC13 | Operational feedback + in-service delta updates |

## Cross-References

- ATA 23 (Communications), ATA 24 (Electrical), ATA 25 (Equipment/Furnishings)
- ATA 26 (Fire Protection), ATA 33 (Lights), ATA 38 (Water/Waste)
- ATA 46 (Information Systems), ATA 52 (Doors)

## Related Documents

- ATA 44 baseline (SHARED): [../../README.md](../../README.md)
- BWB overlay (parallel): [../BWB/README.md](../BWB/README.md)
- ATA 25 WTW overlay: [../../ATA_25-EQUIPMENT_FURNISHINGS/PROGRAMME_EXT/WTW/README.md](../../../ATA_25-EQUIPMENT_FURNISHINGS/PROGRAMME_EXT/WTW/README.md)
- Lifecycle registry: [../../../../lifecycle/LC_PHASE_REGISTRY.yaml](../../../../lifecycle/LC_PHASE_REGISTRY.yaml)
