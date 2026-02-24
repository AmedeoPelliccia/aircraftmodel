# ICD — BWB Autoflight to FCS Effector Map

**ICD ID:** ICD-BWB-22-001
**Doc ID:** T-A2-ATA22-BWB-ICD-001
**Delta Ref:** DELTA-BWB-22-001
**System A:** ATA 22 Auto Flight (FCC)
**System B:** ATA 27 Flight Control System (FCS)
**Status:** STUB
**Lifecycle:** Standard (LC01–LC13)
**Baseline Ref:** `../../..` (ATA 22 SHARED)

---

## 1. Delta Statement

The SHARED baseline ICD between Auto Flight and FCS assumes conventional elevator and aileron demand signals. The BWB delta replaces these with a **surface demand vector** covering the distributed elevon/spoileron array. This ICD describes only the delta from the SHARED interface.

---

## 2. Interface Description (Stub)

| Parameter | SHARED Baseline | BWB Delta |
|---|---|---|
| Pitch surface demand | Single elevator channel | Inboard + Mid Elevon pitch component |
| Roll surface demand | Single aileron channel | Mid + Outboard Elevon + Spoileron roll component |
| Yaw surface demand | Rudder channel | Differential elevon + spoileron (no vertical tail) — TBD |
| Signal count | 2–3 demands | N demands (one per effector side) — TBD (LC02) |
| Bus type | TBD SHARED | TBD (ARINC 429 / AFDX — LC02) |
| Update rate | TBD SHARED | TBD (LC03) |
| Latency budget | TBD SHARED | TBD (LC03) |
| Integrity level | TBD SHARED | DAL-B consistent — TBD (LC03) |

---

## 3. Data Items (Stub)

| Signal Name | Direction | Units | Range | Resolution | Latency | Status |
|---|---|---|---|---|---|---|
| δ_IE_LEFT_demand | FCC → FCS | deg | TBD (LC03) | TBD | TBD | STUB |
| δ_IE_RIGHT_demand | FCC → FCS | deg | TBD (LC03) | TBD | TBD | STUB |
| δ_ME_LEFT_demand | FCC → FCS | deg | TBD (LC03) | TBD | TBD | STUB |
| δ_ME_RIGHT_demand | FCC → FCS | deg | TBD (LC03) | TBD | TBD | STUB |
| δ_OE_LEFT_demand | FCC → FCS | deg | TBD (LC03) | TBD | TBD | STUB |
| δ_OE_RIGHT_demand | FCC → FCS | deg | TBD (LC03) | TBD | TBD | STUB |
| δ_SP_LEFT_demand | FCC → FCS | deg | TBD (LC03) | TBD | TBD | STUB |
| δ_SP_RIGHT_demand | FCC → FCS | deg | TBD (LC03) | TBD | TBD | STUB |
| FCS_EFFECTOR_STATUS | FCS → FCC | Discrete | TBD | TBD | TBD | STUB |

---

## 4. Open Items

| Item | Description | LC Gate |
|---|---|---|
| OI-ICD001-001 | Confirm signal count from effector map (OI-EFFMAP-001) | LC02 |
| OI-ICD001-002 | Define data bus type and protocol | LC02 |
| OI-ICD001-003 | Define deflection range and resolution for each signal | LC03 |
| OI-ICD001-004 | Define latency and integrity requirements | LC03 |
