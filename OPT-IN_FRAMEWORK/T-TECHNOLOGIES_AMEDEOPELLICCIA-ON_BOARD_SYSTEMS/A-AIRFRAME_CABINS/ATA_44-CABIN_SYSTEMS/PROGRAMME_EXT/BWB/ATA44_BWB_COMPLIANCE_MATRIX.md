# ATA 44 BWB — Compliance Matrix

**Doc ID:** T-A-ATA44-BWB-ACC-001
**Variant:** BWB
**Lifecycle:** LC01 (scaffold — evidence columns at LC06–LC09)
**Parent:** [BWB README](README.md)

---

## Scope

Compliance traceability for BWB-specific ATA 44 Cabin Systems requirements against
applicable certification standards (CS-25, EUROCAE ED-14G/DO-160G, ARINC specs).

---

## Compliance Matrix

| Standard / Para | Subject | BWB Delta | BWB Req File | Evidence File | Status |
|----------------|---------|-----------|-------------|--------------|--------|
| CS-25.1309 | System safety — distributed ZC failure conditions | DELTA-BWB-44-001 | REQ_BWB_44_100_CABIN_CORE.yaml | ANALYSIS_BWB_CMS_SAFETY_1309.md | OPEN — LC05 |
| CS-25.1309 | System safety — zone isolation (bay loss) | DELTA-BWB-44-002 | REQ_BWB_44_100_CABIN_CORE.yaml | ANALYSIS_BWB_CMS_SAFETY_1309.md | OPEN — LC05 |
| CS-25.1309 | System safety — inter-bay bridge failure | DELTA-BWB-44-003 | REQ_BWB_44_100_CABIN_CORE.yaml | ANALYSIS_BWB_CMS_SAFETY_1309.md | OPEN — LC05 |
| CS-25.1353 | Wiring separation (spar bay penetrations) | DELTA-BWB-44-004 | REQ_BWB_44_100_CABIN_CORE.yaml | INSPECTION_BWB_WIRING_QA.md | OPEN — LC06 |
| ARINC 664 Part 7 | AFDX per-bay segment + inter-bay bridge conformance | DELTA-BWB-44-005 | REQ_BWB_44_100_CABIN_CORE.yaml | TEST_BWB_NETWORK_CONFORMANCE.md | OPEN — LC07 |
| CS-25.854 | Smoke detection — bay isolation (fire detection per bay) | DELTA-BWB-44-007 | REQ_BWB_44_500_CABIN_MONITORING.yaml | TEST_BWB_CMS_FUNCTIONAL_44_10.md | OPEN — LC06 |
| CS-25.853 | Flammability — distributed IFE nodes | DELTA-BWB-44-006 | REQ_BWB_44_200_IFE.yaml | TEST_BWB_IFE_FLAMMABILITY_853.md | OPEN — LC07 |
| ED-14G Section 20 | EMI — distributed ZC LRUs per bay | DELTA-BWB-44-001 | REQ_BWB_44_100_CABIN_CORE.yaml | TEST_BWB_CMS_FUNCTIONAL_44_10.md | OPEN — LC07 |

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

- [ATA44_BWB_INDEX.yaml](ATA44_BWB_INDEX.yaml)
- [Verification Evidence](ATA44_BWB_VERIFICATION_EVIDENCE/README.md)
- [ATA 44 SHARED baseline](../../README.md)
- [WTW parallel](../WTW/ATA44_WTW_COMPLIANCE_MATRIX.md)
