# ATA 57-30-70 — Winglets Repair Bonding Integrity

**SNS:** ATA 57-30-70 (Wings — Winglets — Repair and Bonding Integrity)
**Doc ID:** T-A-ATA57-30-70-001
**Lifecycle:** LC04 (planned increment)
**Applicability:** WTW and BWB variants
**Parent:** [WINGLETS README](README.md)

---

## 1) Scope

Defines winglet-specific bonding integrity requirements as an overlay on the shared ATA 51-70-70 standard. Applies to both WTW and BWB variants of the AMPEL360 Q100 winglet/wing-tip region.

The ATA 51-70-70 baseline requirements apply in full. This document adds restrictions specific to the slender geometry, high aeroelastic load cycling, and environmental exposure characteristics of winglets.

---

## 2) Winglet-Specific Bonding Integrity Requirements

| Requirement ID | Shall statement | Rationale |
|---------------|-----------------|-----------|
| WG-70-001 | All bonded repairs to winglet primary composite members shall use only approved adhesive systems specified in the applicable SRM chapter for ATA 57. | Winglet composites may require specific hot-cure systems; cold-cure systems not acceptable for primary structure. |
| WG-70-002 | Cure-cycle monitoring for winglet repairs shall use a minimum of 2 thermocouples per repair, regardless of repair area. | Thin winglet skins have lower thermal mass — temperature variation risk. |
| WG-70-003 | UT bond-line verification is mandatory for all bonded repairs to winglet skin panels and primary members, regardless of repair area size. | No minimum area exemption applies due to fatigue cycling. |
| WG-70-004 | For BWB winglets, any bonded repair within 300 mm of the blend-zone inboard boundary shall also satisfy the blend-zone bonding integrity requirements in `ATA_53-50-70`. | Inboard boundary condition imposes additional structural requirements. |

---

## 3) Release Gate (Winglet Supplement)

In addition to the ATA 51-70-70 release gate requirements, winglet bonded repairs shall additionally require:

1. Thermocouple cure log with minimum 2 thermocouples.
2. UT bond-line scan for all primary member repairs (no area threshold exemption).
3. For BWB winglets near blend zone: confirmation of compliance with ATA 53-50-70.

---

## Related Documents

- [ATA_51-70-70_REPAIR_BONDING_INTEGRITY.md](../../ATA_51-70-70_REPAIR_BONDING_INTEGRITY.md) — Shared baseline
- [ATA_57-30-60_INSPECTION_NDT_TASKS.md](ATA_57-30-60_INSPECTION_NDT_TASKS.md) — Winglet NDT
- [ATA_57-30-80_ELECTRICAL_BONDING_LIGHTNING_CONTINUITY.md](ATA_57-30-80_ELECTRICAL_BONDING_LIGHTNING_CONTINUITY.md) — Electrical bonding
- [../BLEND_ZONE/ATA_53-50-70_REPAIR_BONDING_INTEGRITY.md](../BLEND_ZONE/ATA_53-50-70_REPAIR_BONDING_INTEGRITY.md) — Blend zone bonding (BWB inboard)
