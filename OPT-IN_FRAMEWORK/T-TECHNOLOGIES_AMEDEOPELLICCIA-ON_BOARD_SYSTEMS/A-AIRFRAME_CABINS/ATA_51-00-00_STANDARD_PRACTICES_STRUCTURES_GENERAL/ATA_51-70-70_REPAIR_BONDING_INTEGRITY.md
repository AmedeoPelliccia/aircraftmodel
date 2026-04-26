---
ata_sns: "51-70-70"
ata_chapter: "51"
ata_section: "70"
ata_subject: "70"
ata_title: "Repair Bonding Integrity — Standard Practices and Structures General"
programme_controlled_subject: true
document_role: "standard"
---
# ATA 51-70-70 — Repair Bonding Integrity — Mandatory Verification

**SNS:** ATA 51-70-70 (Structures Standard Practices — Repair — Bonding Integrity)
**Doc ID:** T-A-ATA51-70-70-001
**Lifecycle:** LC04 (planned increment)
**Parent:** [ATA 51 README](README.md)

---

## 1) Scope

Defines mandatory verification requirements for any structural repair relying on bonding integrity, applicable to both WTW and BWB variants of the **AMPEL360 Q100** platform.

Repair types covered by this document:
- Adhesive bonding
- Wet layup
- Prepreg repair
- Co-cure bonding
- Secondary-bonded repair

> **Note:** NDT method selection guidance is in `ATA_51-70-60_INSPECTION_NDT.md`. Repair acceptability decision flow is in `ATA_51-70-00_REPAIR_ACCEPTABILITY.md`.

---

## 2) Mandatory Verification Requirements

Any repair that relies on **bonding integrity** shall include mandatory verification of the bonding process and final bond condition before release to service.

| Verification step | Mandatory requirement | Evidence required |
|-------------------|-----------------------|-------------------|
| Process monitoring | Record and review cure-cycle parameters, including temperature, pressure, vacuum level, dwell time, ramp rate, and hold duration, as applicable to the repair scheme. | Cure log, vacuum log, pressure log, thermocouple record, equipment calibration status |
| Post-cure visual inspection | Inspect the repaired area for voids, porosity, resin starvation, resin richness, edge lift, incomplete cure, colour anomaly, tackiness, contamination, wrinkles, bridging, or delamination indications. | Visual inspection record, photographs where required, inspector sign-off |
| NDT verification | Perform approved NDT, such as ultrasonic testing (UT), through-transmission ultrasonic (TTU), tap test, thermography, or other approved method, to verify bond-line continuity and absence of unacceptable disbond or delamination. | NDT report, scan record, equipment settings, certified inspector identification |
| Acceptance criteria | Accept or reject the repair strictly against the applicable repair scheme, SRM, engineering order, or approved NDT acceptance standard. | Acceptance statement, reference to approved limits, disposition of defects |

---

## 3) Release Gate

The repair shall **not be released to service** unless all required bonding-integrity verification records are complete, reviewed, and accepted by authorized personnel.

**Release gate checklist (all items shall be confirmed before close-up):**

1. Cure-cycle log reviewed and confirmed within specified limits.
2. Post-cure visual inspection completed and recorded.
3. NDT verification performed, results within acceptance criteria.
4. Acceptance statement signed by authorised inspector.
5. All non-conformances dispositioned under applicable repair scheme, SRM, or engineering order.

---

## 4) Controlled Requirement Text

> Repairs relying on adhesive bonding, wet layup, prepreg, co-cure, or secondary bonding shall not be released to service without documented evidence of cure-cycle compliance, post-cure visual inspection, and approved NDT bond-line verification. All records shall be reviewed and accepted by authorised personnel prior to close-up of the repair area. Non-conformances identified during verification shall be dispositioned under the applicable repair scheme, SRM, or engineering order before release.

---

## 5) Area-Specific Overlays

For local area implementations (BLEND_ZONE, WINGLETS), bonding integrity requirements are additionally governed by the applicable chapter document:

| Structural area | Applicable overlay |
|----------------|--------------------|
| Fuselage-to-wing blend zone (BWB) | [../ATA_53-50-00_BLEND_ZONE_CENTREBODY_INTERFACE/ATA_53-50-70_REPAIR_BONDING_INTEGRITY.md](../ATA_53-50-00_BLEND_ZONE_CENTREBODY_INTERFACE/ATA_53-50-70_REPAIR_BONDING_INTEGRITY.md) |
| Winglets (BWB/WTW outboard) | [../ATA_57-30-00_WING_TIP_WINGLETS/ATA_57-30-70_REPAIR_BONDING_INTEGRITY.md](../ATA_57-30-00_WING_TIP_WINGLETS/ATA_57-30-70_REPAIR_BONDING_INTEGRITY.md) |

---

## Related Documents

- [ATA 51 README](README.md)
- [ATA_51-70-60_INSPECTION_NDT.md](ATA_51-70-60_INSPECTION_NDT.md)
- [ATA_51-70-00_REPAIR_ACCEPTABILITY.md](ATA_51-70-00_REPAIR_ACCEPTABILITY.md)
- [ATA 20 governance](../ATA_20-00-00_STANDARD_PRACTICES_AIRFRAME_SHARED/README.md)
