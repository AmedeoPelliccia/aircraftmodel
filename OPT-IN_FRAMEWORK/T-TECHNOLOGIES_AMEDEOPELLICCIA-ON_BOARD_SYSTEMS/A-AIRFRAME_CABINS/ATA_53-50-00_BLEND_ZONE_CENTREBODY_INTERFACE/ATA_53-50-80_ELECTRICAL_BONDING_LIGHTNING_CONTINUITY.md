---
ata_sns: "53-50-80"
ata_chapter: "53"
ata_section: "50"
ata_subject: "80"
ata_title: "Electrical Bonding and Lightning Continuity — Blend Zone Centrebody Interface"
programme_controlled_subject: true
document_role: "standard"
---
# ATA 53-50-80 — Blend Zone Electrical Bonding and Lightning Continuity

**SNS:** ATA 53-50-80 (Fuselage — Blend Zone — Electrical Bonding / Lightning Continuity)
**Doc ID:** T-A-ATA53-50-80-001
**Lifecycle:** LC04 (planned increment)
**Applicability:** BWB variant only
**Parent:** [BLEND_ZONE README](README.md)

> **SNS reservation note:** Subject 80 at ATA 53-50 is reserved exclusively for Electrical Bonding / Lightning Continuity. CSDB/S1000D publication mapping artefacts shall not be assigned to this subject. See `CSDB_S1000D_MAP.yaml` (administrative file, `not_ata_subject: true`).

---

## 1) Scope

Defines electrical bonding and lightning continuity requirements specific to the fuselage-to-wing blend zone on the BWB AMPEL360 Q100 variant.

The blend zone represents a structural and electrical transition between the centrebody fuselage and the outboard composite wing torque box. Ensuring electrical continuity across this transition is critical for lightning protection and HIRF shielding.

---

## 2) Bonding Requirements

| Requirement ID | Location | Bonding method | Resistance limit | Verification |
|---------------|----------|----------------|-----------------|--------------|
| BZ-80-001 | Spar web bonding jumpers | Dedicated bonding jumper (copper braid or equivalent) at each spar web penetration | ≤ 2.5 mΩ structure-to-structure | DC resistance measurement per maintenance task |
| BZ-80-002 | Composite skin segments — lightning mesh continuity | Expanded copper mesh or conductive primer ply co-cured into skin | Continuity per approved acceptance standard | End-to-end resistance test per Bonding Continuity AMM task |
| BZ-80-003 | Centrebody-to-wing torque box transition | Bonding jumpers at interface attach fittings | ≤ 2.5 mΩ across transition | Resistance measurement after installation |
| BZ-80-004 | Bonding verification after repair | Any repair disturbing conductive mesh or bonding path shall restore electrical continuity before close-up | Per original limits | Post-repair bonding check per applicable SRM task |

---

## 3) Lightning Strike Zones

The blend zone transitions between lightning strike zones. Zone assignments shall be as specified in the AMPEL360 Q100 Lightning Protection Design Document.

| Structural location | Zone | Implications |
|--------------------|------|-------------|
| Outboard blend zone upper surface | Zone 1A (direct attachment, initial) | Highest conductive path requirement |
| Centrebody lower surface | Zone 2A (swept channel) | Standard mesh continuity |
| Spar bay boundaries | Zone 1B/2A boundary | Bonding jumpers mandatory at each bay |

---

## Related Documents

- [ATA_53-50-70_REPAIR_BONDING_INTEGRITY.md](ATA_53-50-70_REPAIR_BONDING_INTEGRITY.md) — Repair bonding integrity (structural)
- [ATA_53-50-60_INSPECTION_NDT_TASKS.md](ATA_53-50-60_INSPECTION_NDT_TASKS.md) — NDT tasks
- [CSDB_S1000D_MAP.yaml](CSDB_S1000D_MAP.yaml) — Publication mapping (administrative file, non-SNS)
