# ATA 44 — Cabin Systems — BWB Programme Extension

**Domain:** T-TECHNOLOGIES / A-AIRFRAME_CABINS
**Boundary:** PROGRAMME_EXT / BWB (variant overlay)
**Doc ID:** T-A-ATA44-BWB-001
**Lifecycle:** Standard (LC01–LC13)

## Scope

BWB-only deltas to ATA 44 baseline (SHARED) for AMPEL360 BWB (EIS 2042–48).
This folder SHALL NOT duplicate SHARED content except as traceable delta statements.

ATA 44 covers the Cabin Systems domain: Cabin Core System (44-10), In-Flight Entertainment
(44-20), External Communication (44-30), Cabin Mass Memory (44-40), Cabin Monitoring
(44-50), and Miscellaneous Cabin Systems (44-60).

## Overlay Rules

- SHARED baseline location: `../../` (ATA_44 root)
- This overlay provides: ΔARCH, ΔREQ, ΔICD, ΔAcceptability, ΔEvidence
- Precedence: Type design basis > approved data > SHARED ATA44 > BWB overlay > local WI

## Contents

| File / Folder | Description |
|---------------|-------------|
| `ATA44_BWB_INDEX.yaml` | Delta index — SSOT for all BWB ATA 44 deviations |
| `ATA44_BWB_DELTA_LOG.yaml` | Auditable change log of delta evolution |
| `ATA44_BWB_COMPLIANCE_MATRIX.md` | CS-25 / ED-14G compliance traceability for BWB-specific requirements |
| `ATA44_BWB_ARCHITECTURE/` | BWB topology, zonal distribution, network segmentation, models |
| `ATA44_BWB_INTERFACES/` | Zonal boundaries, endpoint maps, harness envelopes, controller placement |
| `ATA44_BWB_REQUIREMENTS/` | BWB-only requirements by ATA 44 subchapter |
| `ATA44_BWB_ACCEPTABILITY/` | BWB-specific zone isolation policies, dispatch rules, degraded-mode limits |
| `ATA44_BWB_VERIFICATION_EVIDENCE/` | Analysis/test/inspection objects linked to BWB deltas |

## BWB-Specific Cabin Systems Drivers

| Driver | BWB Characteristic |
|--------|-------------------|
| Fuselage topology | Composite wide-body planform; multiple spar bays interrupt harness routing |
| CMS controller placement | Distributed per-bay Zone Controllers (ZC); no single centralised CMC |
| IFE server location | Distributed per-bay IFE nodes; synchronised via bay-bridge links |
| PA/crew call | Radial zone topology; zone addressing based on bay + angular position |
| Cabin monitoring | Bay-partitioned sensor loops; bay-to-bay bridging via inter-bay bus |
| Network backbone | ARINC 664 (AFDX) cabin domain with inter-bay bridge switches; 100 Mbit/s |

## WTW vs BWB Architecture Delta

| Item | WTW | BWB |
|------|-----|-----|
| Controller topology | Centralised CMC/CAC pair | Distributed ZC per spar bay |
| Harness routing | Single longitudinal run | Bay-by-bay segments; inter-bay bridging |
| Zone definition | 2–4 longitudinal zones | Radial + bay zones |
| Network segmentation | Single AFDX switch pair | Per-bay AFDX segment; inter-bay bridges |
| IFE architecture | Central server + satellite units | Distributed per-bay IFE nodes |

## LC Phase Gating

| LC Gate | Content added |
|---------|--------------|
| LC01–LC02 | Scaffold + delta index + architecture overview |
| LC03 | Interface data (zone boundaries, controller positions, bay-bridge topology) |
| LC04–LC05 | Requirement thresholds + acceptability limits |
| LC06–LC09 | Verification evidence (test/analysis/inspection) |
| LC10–LC13 | Operational feedback + in-service delta updates |

## Cross-References

- ATA 23 (Communications), ATA 24 (Electrical), ATA 25 (Equipment/Furnishings)
- ATA 26 (Fire Protection), ATA 33 (Lights), ATA 38 (Water/Waste)
- ATA 46 (Information Systems), ATA 52 (Doors), ATA 53 (Fuselage)

## Related Documents

- ATA 44 baseline (SHARED): [../../README.md](../../README.md)
- WTW overlay (parallel): [../WTW/README.md](../WTW/README.md)
- ATA 25 BWB overlay: [../../../ATA_25-EQUIPMENT_FURNISHINGS/PROGRAMME_EXT/BWB/README.md](../../../ATA_25-EQUIPMENT_FURNISHINGS/PROGRAMME_EXT/BWB/README.md)
- Lifecycle registry: [../../../../lifecycle/LC_PHASE_REGISTRY.yaml](../../../../lifecycle/LC_PHASE_REGISTRY.yaml)
