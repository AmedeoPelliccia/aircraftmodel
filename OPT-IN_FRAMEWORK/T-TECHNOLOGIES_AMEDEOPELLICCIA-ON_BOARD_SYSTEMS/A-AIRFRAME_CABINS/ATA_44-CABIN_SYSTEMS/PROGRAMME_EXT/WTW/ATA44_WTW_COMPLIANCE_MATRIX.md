# ATA 44 WTW — Compliance Matrix

**Doc ID:** T-A-ATA44-WTW-ACC-001
**Variant:** WTW
**Lifecycle:** LC01 (scaffold — evidence columns at LC06–LC09)
**Parent:** [WTW README](README.md)

---

## Scope

Compliance traceability for WTW-specific ATA 44 Cabin Systems requirements against
applicable certification standards (CS-25, EUROCAE ED-14G/DO-160G, ARINC specs).

---

## Compliance Matrix

| Standard / Para | Subject | WTW Delta | WTW Req File | Evidence File | Status |
|----------------|---------|-----------|-------------|--------------|--------|
| CS-25.1309 | System safety — CMS failure conditions | DELTA-WTW-44-001 | REQ_WTW_44_100_CABIN_CORE.yaml | ANALYSIS_WTW_CMS_SAFETY_1309.md | OPEN — LC05 |
| CS-25.1309 | System safety — network topology failure | DELTA-WTW-44-002 | REQ_WTW_44_100_CABIN_CORE.yaml | ANALYSIS_WTW_CMS_SAFETY_1309.md | OPEN — LC05 |
| CS-25.1353 | Wiring separation (cabin harness) | DELTA-WTW-44-003 | REQ_WTW_44_100_CABIN_CORE.yaml | INSPECTION_WTW_WIRING_QA.md | OPEN — LC06 |
| CS-25.854 | Smoke detection (lavatory/cabin) | DELTA-WTW-44-007 | REQ_WTW_44_500_CABIN_MONITORING.yaml | TEST_WTW_CMS_FUNCTIONAL_44_10.md | OPEN — LC06 |
| CS-25.853 | Flammability — IFE LRUs | DELTA-WTW-44-005 | REQ_WTW_44_200_IFE.yaml | TEST_WTW_IFE_FLAMMABILITY_853.md | OPEN — LC06 |
| ED-14G Section 20 | Electrical bonding / EMI | DELTA-WTW-44-001 | REQ_WTW_44_100_CABIN_CORE.yaml | TEST_WTW_CMS_FUNCTIONAL_44_10.md | OPEN — LC07 |
| ARINC 664 Part 7 | AFDX cabin network conformance | DELTA-WTW-44-004 | REQ_WTW_44_100_CABIN_CORE.yaml | TEST_WTW_NETWORK_CONFORMANCE.md | OPEN — LC07 |
| ETSI EN 303 360 | Passenger satcom/Wi-Fi RF compliance | DELTA-WTW-44-006 | REQ_WTW_44_300_EXTERNAL_COMM.yaml | TEST_WTW_RF_COMPLIANCE.md | OPEN — LC07 |

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

- [ATA44_WTW_INDEX.yaml](ATA44_WTW_INDEX.yaml)
- [Verification Evidence](ATA44_WTW_VERIFICATION_EVIDENCE/README.md)
- [ATA 44 SHARED baseline](../../README.md)
