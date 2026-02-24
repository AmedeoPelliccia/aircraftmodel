# EVI-BWB-44-002 — BWB CMS Functional Test (Bay Isolation / Smoke Detection)

**Doc ID:** T-A-ATA44-BWB-EVI-002
**Evidence Type:** Functional Test
**Delta Ref:** DELTA-BWB-44-007
**Req Refs:** BWB-44-500-001, BWB-44-500-002, BWB-44-500-003
**Standard:** CS-25.854
**LC Gate:** LC06 (stub — test protocol at LC05, execution at LC06)
**Status:** STUB

---

## Test Objective

Demonstrate that:
1. Smoke/temperature sensor events in Bay N are detected and reported by ZC-N
   without dependency on BBU or adjacent bays.
2. Inter-bay smoke alerts propagate to all ZCs via BBU when available.
3. Zone/bay of origin is uniquely identified on crew display.

---

## Test Configuration (TBD at LC05)

| Item | Details |
|------|---------|
| Test facility | Ground integration laboratory or aircraft iron bird |
| CMS configuration | Full BWB CMS LRU set (all bays) |
| BBU availability | Tested with BBU active AND with BBU failed (disconnected) |
| Sensor simulation | Smoke injection or optical trigger simulation per bay |

---

## Test Cases (Placeholders)

| Test ID | Description | Pass Criteria |
|---------|-------------|--------------|
| TC-BWB-44-501 | Smoke trigger Bay 1, BBU active | ZC-01 detects; all ZCs receive inter-bay alert within TBD ms |
| TC-BWB-44-502 | Smoke trigger Bay 2, BBU-01 failed | ZC-02 detects locally; no dependency on BBU-01 |
| TC-BWB-44-503 | Smoke trigger Bay 3, all BBUs active | Crew display shows Bay 3 / zone origin |
| TC-BWB-44-504 | Temperature alarm Bay 1 | ZC-01 processes; no false alarm on adjacent bays |

---

## Related Documents

- [REQ_BWB_44_500_CABIN_MONITORING.yaml](../ATA44_BWB_REQUIREMENTS/REQ_BWB_44_500_CABIN_MONITORING.yaml)
- [ANALYSIS_BWB_CMS_SAFETY_1309.md](ANALYSIS_BWB_CMS_SAFETY_1309.md)
