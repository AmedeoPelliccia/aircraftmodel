# ATA 22 BWB — Compliance Matrix

**Doc ID:** T-A2-ATA22-BWB-COMPLIANCE-001
**Variant:** AMPEL360 Q100 BWB
**Overlay Ref:** ATA22-BWB-OVERLAY-001
**Baseline Ref:** `../..`
**Status:** DRAFT
**Lifecycle:** Standard (LC01–LC13)

---

## Scope

This matrix traces BWB-specific delta requirements and evidence against the CS-25 certification basis for ATA 22 Auto Flight. Only delta items are listed here. SHARED baseline compliance is tracked in the SHARED baseline compliance matrix at `../..`.

---

## Compliance Matrix

| CS-25 Reference | Requirement Topic | Delta Ref | Req IDs | Evidence File(s) | Status |
|---|---|---|---|---|---|
| CS-25.1329(a) | Autopilot system — general design | DELTA-BWB-22-001, DELTA-BWB-22-002 | BWB-22-100-001, BWB-22-100-002, BWB-22-100-003, BWB-22-100-004 | ANALYSIS_BWB_CONTROL_LAW_STABILITY_CS25_1329.md | STUB |
| CS-25.1329(b) | Autopilot — override force | DELTA-BWB-22-001 | BWB-22-100-002 | TEST_BWB_AUTOFLIGHT_FUNCTIONAL.md | STUB |
| CS-25.1329(c) | Autopilot — engagement/disengagement | DELTA-BWB-22-002 | BWB-22-100-003 | TEST_BWB_AUTOFLIGHT_FUNCTIONAL.md | STUB |
| CS-25.1329(d) | Autopilot — warning at disconnect | DELTA-BWB-22-002 | BWB-22-100-004 | TEST_BWB_AUTOFLIGHT_FUNCTIONAL.md | STUB |
| CS-25.1329(i) | Autopilot — failure modes | DELTA-BWB-22-002 | BWB-22-100-004 | ANALYSIS_BWB_AUTOFLIGHT_SAFETY_CS25_1309.md | STUB |
| CS-25.1302 | Installed equipment — flight crew interface | DELTA-BWB-22-001, DELTA-BWB-22-002, DELTA-BWB-22-003 | BWB-22-000-002 | TEST_BWB_AUTOFLIGHT_FUNCTIONAL.md | STUB |
| CS-25.143(a) | Controllability — general | DELTA-BWB-22-002 | BWB-22-100-001 | ANALYSIS_BWB_CONTROL_LAW_STABILITY_CS25_1329.md | STUB |
| CS-25.143(f) | Controllability — envelope protection | DELTA-BWB-22-003 | BWB-22-400-001, BWB-22-400-002, BWB-22-400-003 | TEST_BWB_ENVELOPE_PROTECTION.md | STUB |
| CS-25.253 | High-speed characteristics | DELTA-BWB-22-003 | BWB-22-400-002 | ANALYSIS_BWB_AUTOFLIGHT_SAFETY_CS25_1309.md | STUB |
| CS-25.1309 | Systems and equipment — safety assessment | DELTA-BWB-22-001, DELTA-BWB-22-002, DELTA-BWB-22-003, DELTA-BWB-22-005 | BWB-22-000-003 | ANALYSIS_BWB_AUTOFLIGHT_SAFETY_CS25_1309.md | STUB |
| CS-25.1329 + AMC | FMS guidance — performance | DELTA-BWB-22-004 | BWB-22-200-001, BWB-22-200-002 | *(TBD — LC04)* | STUB |
| CS-25.1329 + AMC | Auto-thrust — 4-engine management | DELTA-BWB-22-005 | BWB-22-300-001, BWB-22-300-002 | TEST_BWB_AUTOFLIGHT_FUNCTIONAL.md | STUB |

---

## Compliance Status Definitions

| Status | Meaning |
|---|---|
| STUB | Evidence file created; content deferred to stated LC gate |
| OPEN | Compliance activity identified; evidence not yet started |
| IN-WORK | Evidence being produced |
| CLOSED | Evidence complete and reviewed |

---

## Notes

- All quantitative compliance thresholds (e.g., alpha limits, buffet margins, thrust asymmetry limits) are **TBD (LC03)**.
- Special Condition SC-FCS-001 applicability for NDI control laws requires confirmation at **LC03**.
- DO-178C DAL-B software plan evidence is addressed in the software lifecycle plan, not this matrix.
- DO-254 complex electronics evidence is addressed in the hardware lifecycle plan, not this matrix.
