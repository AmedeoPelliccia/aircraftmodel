# ATA 50 — Cargo / Accessory Compartments — BWB Programme Extension

**Domain:** T-TECHNOLOGIES / A-AIRFRAME_CABINS
**Boundary:** PROGRAMME_EXT / BWB (variant overlay)
**Doc ID:** T-A-ATA50-BWB-001
**Lifecycle:** Standard (LC01–LC13)
**Status:** DRAFT

## Scope

BWB-only deltas to ATA 50 baseline (SHARED) for AMPEL360 BWB (Blended Wing Body).
This folder SHALL NOT duplicate SHARED content except as traceable delta statements.

The AMPEL360 BWB planform features a distributed multi-bay cargo deck integrated
within the wing box structure. Cargo compartments span multiple structural bays
separated by spars, requiring bay-specific envelope definitions, side-access door
configurations, flat-panel liner attachment schemes, spar-penetrating drain/vent
routing, and bay-partitioned fire containment liner interfaces.

## Overlay Rules

- SHARED baseline location: `../..` (ATA_50 root)
- This overlay provides: **ΔREQ, ΔICD, ΔAcceptability, ΔEvidence**
- Precedence: Type design basis > approved data > SHARED ATA50 > BWB overlay > local WI
- Any substitution of material/fasteners/process SHALL be approved by Engineering.
- No single cargo liner panel or drain routing SHALL cross more than one spar bay
  boundary without a discrete spar penetration fitting (per BWB-50-000-003).

## Contents

- `ATA50_BWB_INDEX.yaml` — delta index (SSOT for BWB deviations)
- `ATA50_BWB_DELTA_LOG.yaml` — auditable delta change log
- `ATA50_BWB_COMPLIANCE_MATRIX.md` — CS-25 traceability per delta
- `ATA50_BWB_INTERFACES/` — BWB-specific ICDs (envelope, access, liner, drain/vent, fire, bay boundary)
- `ATA50_BWB_REQUIREMENTS/` — BWB-only requirements by functional group
- `ATA50_BWB_ACCEPTABILITY/` — BWB-specific installation/damage limits and rework criteria
- `ATA50_BWB_VERIFICATION_EVIDENCE/` — analysis/test/inspection objects linked to deltas

## Named Deltas (Summary)

| Delta ID | Type | Subject | LC Gate |
|---|---|---|---|
| DELTA-BWB-50-001 | ΔICD | Multi-bay flat-deck cargo compartment envelope | LC03 |
| DELTA-BWB-50-002 | ΔICD | Side-access cargo door geometry and latch/hinge per bay | LC03 |
| DELTA-BWB-50-003 | ΔICD | Flat-panel liner attachment scheme (spar-boundary aware) | LC04 |
| DELTA-BWB-50-004 | ΔICD | Distributed drain/vent routing via spar bay penetrations | LC04 |
| DELTA-BWB-50-005 | ΔICD | Bay-partitioned fire containment liner interfaces | LC04 |
| DELTA-BWB-50-006 | ΔREQ+ΔICD | Cargo net/restraint attach at spar bay frames | LC05 |
| DELTA-BWB-50-007 | ΔREQ+ΔICD | Bay-to-bay access provisions through spar penetrations | LC05 |

## Cross-References

- ATA 20/51/53/57 (standard practices & structure/attachments)
- ATA 21 (ventilation, if applicable)
- ATA 24 (lighting/power)
- ATA 26 (fire protection / containment interfaces)
- ATA 38 (drainage / water & waste interfaces)
- ATA 52 (doors/hatches/access panels)
- ATA 25 (liners/stowage if treated in parallel chapter)
- ATA 44 BWB (cabin systems bay topology — shared bay boundary definitions)

## Change Control

All deltas governed by LC phase gates. Numerical thresholds (TBD) locked at LC03–LC05.
