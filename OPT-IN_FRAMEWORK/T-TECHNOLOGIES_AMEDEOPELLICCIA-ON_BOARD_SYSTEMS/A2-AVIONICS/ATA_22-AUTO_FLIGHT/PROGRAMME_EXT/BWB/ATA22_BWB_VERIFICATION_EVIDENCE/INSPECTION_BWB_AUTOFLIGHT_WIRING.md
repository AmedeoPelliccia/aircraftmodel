# INSPECTION — BWB Autoflight Wiring and Installation

**Evidence ID:** EV-BWB-22-005
**Doc ID:** T-A2-ATA22-BWB-INSP-001
**Delta Refs:** DELTA-BWB-22-001, DELTA-BWB-22-005
**CS-25 Ref:** CS-25.1329, CS-25.1302, CS-25.1353
**Method:** Physical inspection per AMM / Installation Drawing review
**Status:** STUB
**Lifecycle:** Standard (LC01–LC13)
**Content Deferred To:** LC07 (first article / prototype installation)

---

## 1. Purpose

This inspection stub defines the scope of BWB-specific autoflight installation inspections. It covers the additional wiring and routing requirements arising from the distributed effector FCC-to-FCS interface (DELTA-BWB-22-001) and the 4-channel FADEC auto-thrust interface (DELTA-BWB-22-005). SHARED baseline installation inspections are not repeated.

---

## 2. Inspection Scope — BWB Delta (Stub)

### 2.1 FCC to FCS Effector Bus Wiring

| Inspection Item | Requirement | Pass Criteria | LC Gate |
|---|---|---|---|
| Physical routing of FCC–FCS effector demand buses | CS-25.1329, CS-25.1353 | Routing segregated from hydraulic/fuel lines per CS-25.1309 zonal analysis | LC07 |
| Wire harness identification markings | AMM — TBD | All bus harnesses identified per electrical standard (TBD) | LC07 |
| Connector torque and locking at FCC end | AMM — TBD | All connectors torqued to AMM values; locking verified | LC07 |
| Connector torque and locking at FCS ACTU end | AMM — TBD | All connectors torqued to AMM values; locking verified | LC07 |
| Shielding continuity (EMI protection) | HIRF protection requirement — TBD | Shielding resistance < TBD Ω (LC06) | LC07 |
| Segregation between redundant channels | CS-25.1309 AC physical separation | Minimum TBD mm separation between redundant bus pairs (LC04) | LC07 |

### 2.2 FCC to FADEC 4-Channel Auto-Thrust Wiring

| Inspection Item | Requirement | Pass Criteria | LC Gate |
|---|---|---|---|
| 4× FADEC AT demand bus routing | CS-25.1329, CS-25.1353 | Routing from FCC/ATC to each FADEC independently routed; no common failure point | LC07 |
| FADEC-1 (ENG1) harness condition | AMM — TBD | No chafing, adequate support, correct termination | LC07 |
| FADEC-2 (ENG2) harness condition | AMM — TBD | No chafing, adequate support, correct termination | LC07 |
| FADEC-3 (ENG3) harness condition | AMM — TBD | No chafing, adequate support, correct termination | LC07 |
| FADEC-4 (ENG4) harness condition | AMM — TBD | No chafing, adequate support, correct termination | LC07 |
| Cross-engine harness segregation | CS-25.1309 physical separation | Left/right engine harnesses segregated by TBD mm (LC04) | LC07 |

### 2.3 FCC Installation

| Inspection Item | Requirement | Pass Criteria | LC Gate |
|---|---|---|---|
| FCC rack mounting torque | AMM — TBD | All fasteners to AMM values | LC07 |
| FCC cooling air connections | AMM — TBD | Cooling duct attached and sealed | LC07 |
| FCC power supply connections | AMM — TBD | Correct bus bar routing per electrical load analysis | LC07 |
| NDI module identification (if separate LRU) | AMM — TBD | Part number and version confirmed against design definition | LC07 |

---

## 3. Inspection Method

Inspections shall be performed per:
- **Applicable AMM Chapters:** TBD (LC06) — to be issued when installation design is complete
- **Inspection authority:** Responsible Design Organisation (DO) delegated inspector
- **Record format:** Inspection record sheet — TBD (LC06)

---

## 4. Prerequisites for Inspection

| Prerequisite | LC Gate |
|---|---|
| BWB installation drawings (IDs) released | LC06 |
| AMM electrical installation chapters issued | LC06 |
| Physical separation requirements from zonal analysis | LC04 |
| HIRF shielding resistance values | LC06 |

---

## 5. Open Items

| Item | Description | LC Gate |
|---|---|---|
| OI-INSP-001 | Obtain installation drawing IDs from design team | LC06 |
| OI-INSP-002 | Define shielding resistance acceptance values | LC06 |
| OI-INSP-003 | Define physical separation distances from zonal analysis | LC04 |
| OI-INSP-004 | Issue inspection record forms | LC06 |
