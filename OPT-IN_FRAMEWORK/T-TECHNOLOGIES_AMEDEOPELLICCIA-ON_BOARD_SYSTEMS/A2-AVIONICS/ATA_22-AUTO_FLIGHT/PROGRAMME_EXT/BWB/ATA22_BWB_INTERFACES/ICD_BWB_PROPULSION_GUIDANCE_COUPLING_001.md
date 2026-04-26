# ICD — BWB Autoflight to Propulsion Guidance Coupling

**ICD ID:** ICD-BWB-22-003
**Doc ID:** T-A2-ATA22-BWB-ICD-003
**Delta Ref:** DELTA-BWB-22-005
**System A:** ATA 22 Auto Flight / Auto-Thrust Computer (FCC / ATC)
**System B:** ATA 73/76 Engine FADEC × 4
**Status:** STUB
**Lifecycle:** Standard (LC01–LC13)
**Baseline Ref:** `../../..` (ATA 22 SHARED)

---

## 1. Delta Statement

The SHARED baseline auto-thrust interface is defined for a conventional 2-engine layout with independent left/right thrust demands. The AMPEL360 Q100 BWB has 4 engines distributed symmetrically about the fuselage centreline. The autoflight system must:
1. Send independent thrust demands to each of the 4 FADECs
2. Receive individual engine state feedback from 4 FADECs
3. Implement asymmetric thrust compensation to maintain directional control

---

## 2. Engine Configuration (Stub)

| Engine | Position | FADEC | Notes |
|---|---|---|---|
| ENG 1 | Inboard Left | FADEC-1 | TBD exact station |
| ENG 2 | Outboard Left | FADEC-2 | TBD exact station |
| ENG 3 | Inboard Right | FADEC-3 | TBD exact station |
| ENG 4 | Outboard Right | FADEC-4 | TBD exact station |

Exact spanwise and fore-aft positions: **TBD (LC02)**.

---

## 3. Interface Additions and Modifications (Stub)

| Parameter | SHARED Baseline | BWB Delta | LC Gate |
|---|---|---|---|
| Thrust demand channels | 2 (LEFT, RIGHT) | 4 (ENG1–ENG4) | LC02 |
| Feedback channels | 2 | 4 | LC02 |
| Asymmetry compensation | Not applicable | Yaw/roll compensation from differential thrust — TBD | LC03 |
| Thrust balance law | N/A | Active balancing for drag minimisation — TBD | LC03 |
| Engine-out autoflight | 1-engine-out | 1- or 2-engine-out (adjacent or diagonal) — TBD | LC04 |

---

## 4. Data Items — Delta (Stub)

| Signal Name | Direction | Units | Notes | Status |
|---|---|---|---|---|
| N1_DEMAND_ENG1 | ATC → FADEC-1 | % N1 or EPR | TBD thrust parameter | STUB |
| N1_DEMAND_ENG2 | ATC → FADEC-2 | % N1 or EPR | TBD | STUB |
| N1_DEMAND_ENG3 | ATC → FADEC-3 | % N1 or EPR | TBD | STUB |
| N1_DEMAND_ENG4 | ATC → FADEC-4 | % N1 or EPR | TBD | STUB |
| ACTUAL_THRUST_ENG1 | FADEC-1 → ATC | kN or EPR | Feedback | STUB |
| ACTUAL_THRUST_ENG2 | FADEC-2 → ATC | kN or EPR | Feedback | STUB |
| ACTUAL_THRUST_ENG3 | FADEC-3 → ATC | kN or EPR | Feedback | STUB |
| ACTUAL_THRUST_ENG4 | FADEC-4 → ATC | kN or EPR | Feedback | STUB |
| ASYMMETRY_YAW_COMP | ATC → FCC | N·m | Yaw moment from thrust asymmetry | STUB |

---

## 5. Open Items

| Item | Description | LC Gate |
|---|---|---|
| OI-ICD003-001 | Confirm engine positions and thrust moment arms | LC02 |
| OI-ICD003-002 | Define asymmetric thrust compensation law | LC03 |
| OI-ICD003-003 | Define 2-engine-out autoflight capability | LC04 |
| OI-ICD003-004 | Confirm thrust parameter (N1 vs EPR vs direct thrust) | LC02 |
