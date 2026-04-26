---
ata_sns: "53-50-60"
ata_chapter: "53"
ata_section: "50"
ata_subject: "60"
ata_title: "Inspection and NDT Tasks — Blend Zone Centrebody Interface"
programme_controlled_subject: true
document_role: "standard"
---
# ATA 53-50-60 — Blend Zone Inspection and NDT Tasks

**SNS:** ATA 53-50-60 (Fuselage — Blend Zone — Inspection and NDT)
**Doc ID:** T-A-ATA53-50-60-001
**Lifecycle:** LC04 (planned increment)
**Applicability:** BWB variant only
**Parent:** [BLEND_ZONE README](README.md)

---

## 1) Scope

Defines blend-zone-specific inspection tasks and NDT invocation rules for the fuselage-to-wing structural transition region on the BWB AMPEL360 Q100 variant.

These requirements overlay and supplement the shared ATA 51-70-60 NDT guidance. Where this document adds a more restrictive requirement, this document governs. Where no specific blend-zone rule exists, the ATA 51-70-60 baseline applies.

---

## 2) Blend-Zone-Specific Inspection Tasks

| Task | Method | Trigger | Notes |
|------|--------|---------|-------|
| Composite skin disbond screening | Tap test + UT | Any maintenance access, post-flight event | Large-area composite — tap test mandatory first screen |
| Spar-bay boundary inspection | DVI + UT or thermography | Any repair within 150 mm of spar web | BWB-only: spar bay separation structural function |
| Stringer termination run-out check | DVI + eddy current (ET) if metallic) | Scheduled fatigue inspection interval | Fatigue-critical feature in blend transition |
| TDF patch boundary verification | UT (bond line) | Post any bonded TDF repair | See `ATA_53-50-70_REPAIR_BONDING_INTEGRITY.md` |

---

## 3) Additional NDT Invocation Rules (Blend Zone)

1. **GVI is insufficient alone** for any inspection of primary composite structure in the blend zone; UT (or thermography) shall be performed following any GVI that reveals surface anomalies.
2. **Through-transmission UT (TTU)** is preferred for large composite skin panels where access from both sides is achievable.
3. **Tap test alone** shall not substitute for UT on any blend-zone primary structural element.
4. **Spar web inspections** at spar bay crossings require Level II UT certification (EN4179/NAS410).

---

## Related Documents

- [ATA_51-70-60_INSPECTION_NDT.md](../ATA_51-00-00_STANDARD_PRACTICES_STRUCTURES_GENERAL/ATA_51-70-60_INSPECTION_NDT.md) — Shared baseline NDT guidance
- [ATA_53-50-70_REPAIR_BONDING_INTEGRITY.md](ATA_53-50-70_REPAIR_BONDING_INTEGRITY.md) — Blend zone bonding integrity
- [ATA_53-50-80_ELECTRICAL_BONDING_LIGHTNING_CONTINUITY.md](ATA_53-50-80_ELECTRICAL_BONDING_LIGHTNING_CONTINUITY.md) — Electrical bonding
