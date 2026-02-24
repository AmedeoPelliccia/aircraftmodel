# EVI-004 — WTW ARINC 664 Network Conformance Test

**EVI ID:** T-A-ATA44-WTW-EVI-004
**Delta Refs:** DELTA-WTW-44-004
**Req Refs:** WTW-44-100-005
**Standard:** ARINC 664 Part 7 (AFDX)
**Status:** OPEN — Target LC07
**Parent:** [Evidence README](README.md)

---

## 1) Objective

Demonstrate that the WTW ATA 44 ARINC 664 Part 7 cabin network implementation conforms
to the AFDX specification and meets the WTW-specific VL allocation defined in
ICD T-A-ATA44-WTW-ICD-003.

---

## 2) Test Summary

| Test | Pass Criterion | Target LC |
|------|---------------|-----------|
| VL conformance (all VL IDs per icd_endpoints.yaml) | All VLs operate within BAG/max frame size limits | LC07 |
| Network latency (CMS command to CSU) | Latency ≤ TBD ms | LC07 |
| Bandwidth utilisation | Total utilisation ≤ TBD % of 100 Mbit/s backbone | LC07 |
| Fault containment (faulty VL does not affect others) | No cross-VL contamination | LC07 |
| Failover (switch A to switch B) | Seamless switchover within TBD ms | LC07 |

---

## 3) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Populate icd_endpoints.yaml with final VL/port allocation | Systems Integration | LC03 |
| Define latency and BW budgets | Systems Architecture | LC04 |
| Conduct AFDX conformance test on hardware rig | Test Engineering | LC07 |
