# ATA 25 BWB — Compliance Matrix

**Doc ID:** T-A-ATA25-BWB-ACC-001
**Variant:** BWB
**Lifecycle:** LC01 (scaffold — evidence columns to be filled at LC06–LC09)
**Parent:** [BWB README](README.md)

---

## Scope

CS-25 compliance traceability for BWB-specific ATA 25 requirements. Each row identifies:
- The CS-25 regulation paragraph
- The BWB-specific delta requirement ID
- The evidence object file (test/analysis/inspection)
- Compliance status

---

## Compliance Matrix

| CS-25 Para | Subject | BWB Delta ID | BWB Req File | Evidence File | Status |
|-----------|---------|-------------|-------------|--------------|--------|
| CS-25.561 | Emergency landing — floor grid seat loads | DELTA-BWB-25-002 | REQ_BWB_25_200_PASSENGER_COMPARTMENT.yaml | ANALYSIS_BWB_SEAT_AND_RESTRAINTS_25_562.md | OPEN — LC05 |
| CS-25.561 | Emergency landing — monument load paths | DELTA-BWB-25-003 | REQ_BWB_25_300_GALLEYS.yaml | ANALYSIS_BWB_MONUMENT_LOADPATHS_25_561.md | OPEN — LC05 |
| CS-25.562 | Dynamic seat test (flight deck) | DELTA-BWB-25-006 | REQ_BWB_25_100_FLIGHT_COMPARTMENT.yaml | ANALYSIS_BWB_SEAT_AND_RESTRAINTS_25_562.md | OPEN — LC06 |
| CS-25.562 | Dynamic seat test (cabin) | DELTA-BWB-25-002 | REQ_BWB_25_200_PASSENGER_COMPARTMENT.yaml | ANALYSIS_BWB_SEAT_AND_RESTRAINTS_25_562.md | OPEN — LC06 |
| CS-25.785 | Stowage strength and CG effects | DELTA-BWB-25-004 | REQ_BWB_25_200_PASSENGER_COMPARTMENT.yaml | ANALYSIS_BWB_MONUMENT_LOADPATHS_25_561.md | OPEN — LC05 |
| CS-25.803 | Emergency evacuation (BWB multi-zone) | DELTA-BWB-25-005 | REQ_BWB_25_600_EMERGENCY_EQUIPMENT.yaml | TEST_BWB_EGRESS_DEMONSTRATION.md | OPEN — LC06 |
| CS-25.810 | Emergency exit marking/lighting (BWB) | DELTA-BWB-25-005 | REQ_BWB_25_600_EMERGENCY_EQUIPMENT.yaml | TEST_BWB_EGRESS_DEMONSTRATION.md | OPEN — LC06 |
| CS-25.853(a) | Flammability — cabin interior (BWB) | DELTA-BWB-25-001 | REQ_BWB_25_200_PASSENGER_COMPARTMENT.yaml | TEST_BWB_FLAMMABILITY_25_853.md | OPEN — LC06 |
| CS-25.853(a) | Flammability — cargo liners | DELTA-BWB-25-007 | REQ_BWB_25_500_CARGO_LINERS.yaml | TEST_BWB_FLAMMABILITY_25_853.md | OPEN — LC06 |
| CS-25.1411 | Safety equipment stowage accessibility | DELTA-BWB-25-005 | REQ_BWB_25_600_EMERGENCY_EQUIPMENT.yaml | INSPECTION_BWB_INSTALLATION_QA.md | OPEN — LC06 |

---

## Status Legend

| Status | Meaning |
|--------|---------|
| OPEN — LCxx | Not yet addressed; planned for lifecycle gate LCxx |
| IN WORK | Evidence being developed |
| COMPLETE | Evidence available; compliance shown |
| N/A | Not applicable to BWB variant |

---

## Related Documents

- [ATA25_BWB_INDEX.yaml](ATA25_BWB_INDEX.yaml)
- [Verification Evidence](ATA25_BWB_VERIFICATION_EVIDENCE/README.md)
- [ATA 25 SHARED baseline](../../README.md)
- [WTW Compliance Matrix](../WTW/ATA25_WTW_COMPLIANCE_MATRIX.md)
