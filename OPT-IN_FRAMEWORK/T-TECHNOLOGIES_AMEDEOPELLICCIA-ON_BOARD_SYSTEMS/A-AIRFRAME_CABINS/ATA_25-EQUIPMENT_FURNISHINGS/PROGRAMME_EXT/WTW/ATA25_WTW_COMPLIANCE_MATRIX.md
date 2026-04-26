# ATA 25 WTW — Compliance Matrix

**Doc ID:** T-A-ATA25-WTW-ACC-001
**Variant:** WTW
**Lifecycle:** LC01 (scaffold — evidence columns to be filled at LC06–LC09)
**Parent:** [WTW README](README.md)

---

## Scope

CS-25 compliance traceability for WTW-specific ATA 25 requirements. Each row identifies:
- The CS-25 regulation paragraph
- The WTW-specific delta requirement ID
- The evidence object file (test/analysis/inspection)
- Compliance status

---

## Compliance Matrix

| CS-25 Para | Subject | WTW Delta ID | WTW Req File | Evidence File | Status |
|-----------|---------|-------------|-------------|--------------|--------|
| CS-25.561 | Emergency landing — seat loads (flight deck) | DELTA-WTW-25-002 | REQ_WTW_25_100_FLT_COMPARTMENT.yaml | ANALYSIS_WTW_SEAT_LOADS_25_561.md | OPEN — LC05 |
| CS-25.561 | Emergency landing — seat loads (cabin) | DELTA-WTW-25-001 | REQ_WTW_25_200_PASS_COMPARTMENT.yaml | ANALYSIS_WTW_SEAT_LOADS_25_561.md | OPEN — LC05 |
| CS-25.562 | Dynamic seat test (flight deck) | DELTA-WTW-25-002 | REQ_WTW_25_100_FLT_COMPARTMENT.yaml | ANALYSIS_WTW_SEAT_LOADS_25_561.md | OPEN — LC06 |
| CS-25.803 | Emergency evacuation (WTW exits) | DELTA-WTW-25-005 | REQ_WTW_25_600_EMERGENCY_EQUIP.yaml | INSPECTION_WTW_EMERGENCY_EQUIP.md | OPEN — LC06 |
| CS-25.810 | Emergency exit markings and lighting | DELTA-WTW-25-005 | REQ_WTW_25_600_EMERGENCY_EQUIP.yaml | INSPECTION_WTW_EMERGENCY_EQUIP.md | OPEN — LC06 |
| CS-25.853(a) | Flammability — cabin interior materials | DELTA-WTW-25-001 | REQ_WTW_25_200_PASS_COMPARTMENT.yaml | TEST_WTW_FLAMMABILITY_25_853.md | OPEN — LC06 |
| CS-25.853(a) | Flammability — galley panels | DELTA-WTW-25-003 | REQ_WTW_25_300_GALLEY.yaml | TEST_WTW_FLAMMABILITY_25_853.md | OPEN — LC06 |
| CS-25.853(a) | Flammability — lavatory panels | DELTA-WTW-25-004 | REQ_WTW_25_400_LAVATORY.yaml | TEST_WTW_FLAMMABILITY_25_853.md | OPEN — LC06 |
| CS-25.853(a) | Flammability — cargo liners | DELTA-WTW-25-006 | REQ_WTW_25_500_CARGO_LINERS.yaml | TEST_WTW_FLAMMABILITY_25_853.md | OPEN — LC06 |
| CS-25.1411 | Safety equipment stowage accessibility | DELTA-WTW-25-005 | REQ_WTW_25_600_EMERGENCY_EQUIP.yaml | INSPECTION_WTW_EMERGENCY_EQUIP.md | OPEN — LC06 |

---

## Status Legend

| Status | Meaning |
|--------|---------|
| OPEN — LCxx | Not yet addressed; planned for lifecycle gate LCxx |
| IN WORK | Evidence being developed |
| COMPLETE | Evidence available; compliance shown |
| N/A | Not applicable to WTW variant |

---

## Related Documents

- [ATA25_WTW_INDEX.yaml](ATA25_WTW_INDEX.yaml)
- [Verification Evidence](ATA25_WTW_VERIFICATION_EVIDENCE/README.md)
- [ATA 25 SHARED baseline](../README.md)
