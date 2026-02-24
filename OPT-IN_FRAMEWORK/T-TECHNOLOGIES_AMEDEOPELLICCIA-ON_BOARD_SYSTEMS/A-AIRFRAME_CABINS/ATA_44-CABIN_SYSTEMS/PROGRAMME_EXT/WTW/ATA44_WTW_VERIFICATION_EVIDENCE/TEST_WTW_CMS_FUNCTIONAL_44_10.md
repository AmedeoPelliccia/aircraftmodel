# EVI-002 — WTW CMS Functional Test (CS-25.854 / ED-14G)

**EVI ID:** T-A-ATA44-WTW-EVI-002
**Delta Refs:** DELTA-WTW-44-007
**Req Refs:** WTW-44-500-001, WTW-44-600-002
**Standard:** CS-25.854 (smoke detection), ED-14G Section 20 (EMI)
**Status:** OPEN — Target LC06
**Parent:** [Evidence README](README.md)

---

## 1) Objective

Demonstrate that the WTW cabin monitoring system (smoke detectors, temperature sensors)
and PA integration function correctly in the WTW zone topology.

---

## 2) Test Summary

| Test | Requirement | Pass Criterion | Target LC |
|------|-------------|---------------|-----------|
| Smoke detector functional (per zone) | WTW-44-500-001 / CS-25.854 | All detectors respond within TBD s of smoke introduction | LC06 |
| PA/CMS isolation (audio bus vs AFDX) | WTW-44-600-002 / CS-25.1309 | No AFDX traffic disruption during PA announcement | LC06 |
| ED-14G Section 20 (EMI at LRU) | WTW-44-000-002 | LRU operates within EMI limits at E/E bay category | LC07 |

---

## 3) Test Conditions

| Condition | Basis | Notes |
|-----------|-------|-------|
| Cabin representative test rig or ground test aircraft | TBD | LC06 |
| Full zone configuration (CSU-01 to CSU-04 installed) | — | — |
| PA announcement from FWD and AFT positions | — | — |
| Smoke: optical or test aerosol per CS-25.854 guidance | — | Quantity TBD |

---

## 4) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Define test procedure detail | Test Engineering | LC05 |
| Confirm test facility (rig vs aircraft) | Test Engineering | LC05 |
| Conduct test and issue test report | Test Engineering | LC06–LC07 |
