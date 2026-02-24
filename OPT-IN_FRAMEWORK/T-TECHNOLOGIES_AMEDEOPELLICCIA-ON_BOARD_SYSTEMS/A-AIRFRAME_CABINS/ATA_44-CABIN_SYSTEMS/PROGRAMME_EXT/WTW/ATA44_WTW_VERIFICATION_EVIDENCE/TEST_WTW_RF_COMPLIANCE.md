# EVI-005 — WTW External Comm RF Compliance Test (ETSI EN 303 360)

**EVI ID:** T-A-ATA44-WTW-EVI-005
**Delta Refs:** DELTA-WTW-44-006
**Req Refs:** WTW-44-300-002, WTW-44-300-003
**Standard:** ETSI EN 303 360 (satcom), ETSI EN 301 893 (Wi-Fi 5 GHz), FCC Part 25 (as applicable)
**Status:** OPEN — Target LC07
**Parent:** [Evidence README](README.md)

---

## 1) Objective

Demonstrate that WTW external communication systems (satcom, Wi-Fi, cellular/ATG)
comply with applicable RF regulatory requirements and that the CFRP crown structure
does not excessively attenuate satcom signals.

---

## 2) Test Summary

| Test | Standard | Pass criterion | Target LC |
|------|----------|---------------|-----------|
| Satcom EIRP and G/T (system level) | ETSI EN 303 360 / ITU-R S.580 | Within allocated bandwidth, EIRP ≥ TBD dBW | LC07 |
| CFRP panel RF attenuation (satcom Ku/Ka band) | ICD T-A-ATA44-WTW-ICD-005 Req WTW-44-300-002 | Attenuation ≤ TBD dB | LC07 |
| Wi-Fi 2.4/5 GHz regulatory compliance | ETSI EN 300 328 / EN 301 893 | Power density within regulatory limits | LC07 |
| EMI to aircraft systems (conducted / radiated) | ED-14G Section 20 | No interference to critical avionics | LC07 |

---

## 3) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Select satcom supplier and obtain system RF budget | Avionics | LC03 |
| Test representative CFRP crown panel samples at RF lab | Test Engineering | LC06 |
| Conduct system-level RF compliance test on aircraft | Test Engineering | LC07 |
