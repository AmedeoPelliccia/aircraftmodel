---
ata_sns: "57-30-60"
ata_chapter: "57"
ata_section: "30"
ata_subject: "60"
ata_title: "Inspection and NDT Tasks — Wing-Tip Winglets"
programme_controlled_subject: true
document_role: "standard"
---
# ATA 57-30-60 — Winglets Inspection and NDT Tasks

**SNS:** ATA 57-30-60 (Wings — Winglets — Inspection and NDT)
**Doc ID:** T-A-ATA57-30-60-001
**Lifecycle:** LC04 (planned increment)
**Applicability:** WTW and BWB variants
**Parent:** [WINGLETS README](README.md)

---

## 1) Scope

Defines winglet-specific inspection tasks and NDT invocation rules for the outboard wing-tip region on AMPEL360 Q100 (both WTW and BWB variants).

These requirements overlay and supplement the shared ATA 51-70-60 NDT guidance. Where this document adds a more restrictive requirement, this document governs. Where no specific winglet rule exists, the ATA 51-70-60 baseline applies.

> **BWB note:** For BWB variant winglets, the blend-zone inboard boundary condition shall be applied for any inspection task that extends to within 300 mm of the blend-zone outboard boundary. See `../ATA_53-50-00_BLEND_ZONE_CENTREBODY_INTERFACE/ATA_53-50-60_INSPECTION_NDT_TASKS.md`.

---

## 2) Winglet-Specific Inspection Tasks

| Task | Method | Trigger | Notes |
|------|--------|---------|-------|
| Primary member skin disbond check | Tap test + UT | Any maintenance access | Member spacing registers require NDT verification post-optimisation |
| Member bay boundary inspection | DVI | After any aerodynamic event (hail, bird strike) | Focus on run-out regions |
| Winglet attachment lug check | DVI + ET (eddy current) | Scheduled fatigue inspection | Fatigue-critical feature at root attachment |
| Tip device geometric check | GVI + dimensional measurement | A-check | Verify aeroelastic deformation within limits |
| Post-repair laminate continuity | UT (pulse-echo or TTU) | After any composite repair | Required before return to service |

---

## 3) Additional NDT Invocation Rules (Winglets)

1. **Eddy current (ET)** is mandatory at all metallic winglet attachment lug fastener holes at every fatigue inspection interval.
2. **UT** (pulse-echo minimum; TTU preferred) is required for any composite repair to a winglet primary member.
3. **Tap test** is acceptable as a first-level screen for secondary structure; shall not substitute for UT on primary members.
4. **Level II UT** certification (EN4179/NAS410) is required for primary composite winglet structure inspections.

---

## Related Documents

- [ATA_51-70-60_INSPECTION_NDT.md](../ATA_51-00-00_STANDARD_PRACTICES_STRUCTURES_GENERAL/ATA_51-70-60_INSPECTION_NDT.md) — Shared baseline NDT guidance
- [ATA_57-30-70_REPAIR_BONDING_INTEGRITY.md](ATA_57-30-70_REPAIR_BONDING_INTEGRITY.md) — Winglet bonding integrity
- [ATA_57-30-80_ELECTRICAL_BONDING_LIGHTNING_CONTINUITY.md](ATA_57-30-80_ELECTRICAL_BONDING_LIGHTNING_CONTINUITY.md) — Electrical bonding
- [../ATA_53-50-00_BLEND_ZONE_CENTREBODY_INTERFACE/ATA_53-50-60_INSPECTION_NDT_TASKS.md](../ATA_53-50-00_BLEND_ZONE_CENTREBODY_INTERFACE/ATA_53-50-60_INSPECTION_NDT_TASKS.md) — Blend zone NDT (BWB inboard boundary)
