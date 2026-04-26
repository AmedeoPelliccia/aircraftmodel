---
ata_sns: "53-50-70"
ata_chapter: "53"
ata_section: "50"
ata_subject: "70"
ata_title: "Repair Bonding Integrity — Blend Zone Centrebody Interface"
programme_controlled_subject: true
document_role: "standard"
---
# ATA 53-50-70 — Blend Zone Repair Bonding Integrity

**SNS:** ATA 53-50-70 (Fuselage — Blend Zone — Repair and Bonding Integrity)
**Doc ID:** T-A-ATA53-50-70-001
**Lifecycle:** LC04 (planned increment)
**Applicability:** BWB variant only
**Parent:** [BLEND_ZONE README](README.md)

---

## 1) Scope

Defines blend-zone-specific bonding integrity requirements as an overlay on the shared ATA 51-70-70 standard. Applies to the fuselage-to-wing structural transition region on the BWB AMPEL360 Q100 variant.

The ATA 51-70-70 baseline requirements apply in full. This document adds restrictions specific to the complex topology and fatigue loading of the blend zone.

---

## 2) Blend-Zone-Specific Bonding Integrity Requirements

| Requirement ID | Shall statement | Rationale |
|---------------|-----------------|-----------|
| BZ-70-001 | All adhesive bonding repairs in the blend zone shall be subject to mandatory pre-bond surface preparation verification (contamination, moisture content, peel-ply removal) in addition to the standard ATA 51-70-70 process monitoring. | Large composite skin area with complex curvature; surface preparation is critical. |
| BZ-70-002 | Any prepreg or wet layup repair spanning a TDF patch boundary shall require engineering approval prior to application. | TDF patch boundaries are fatigue stress concentration locations. |
| BZ-70-003 | TTU (through-transmission UT) shall be the primary NDT method for bond-line verification on blend-zone composite panels exceeding 0.5 m² in repair area. | Single-sided UT insufficient for large-area bond integrity confirmation. |
| BZ-70-004 | The cure-cycle thermocouple record shall include a minimum of 3 thermocouples distributed across the repair area for any repair exceeding 0.25 m². | Temperature gradient risk in large repairs. |

---

## 3) Release Gate (Blend Zone Supplement)

In addition to the ATA 51-70-70 release gate requirements, blend zone bonded repairs shall additionally require:

1. Pre-bond surface preparation record (contamination check, moisture content within limit, peel-ply removed and recorded).
2. TTU scan record for repairs > 0.5 m².
3. Multi-point thermocouple cure log for repairs > 0.25 m².

---

## Related Documents

- [ATA_51-70-70_REPAIR_BONDING_INTEGRITY.md](../ATA_51-00-00_STANDARD_PRACTICES_STRUCTURES_GENERAL/ATA_51-70-70_REPAIR_BONDING_INTEGRITY.md) — Shared baseline
- [ATA_53-50-60_INSPECTION_NDT_TASKS.md](ATA_53-50-60_INSPECTION_NDT_TASKS.md) — Blend zone NDT
- [ATA_53-50-80_ELECTRICAL_BONDING_LIGHTNING_CONTINUITY.md](ATA_53-50-80_ELECTRICAL_BONDING_LIGHTNING_CONTINUITY.md) — Electrical bonding
