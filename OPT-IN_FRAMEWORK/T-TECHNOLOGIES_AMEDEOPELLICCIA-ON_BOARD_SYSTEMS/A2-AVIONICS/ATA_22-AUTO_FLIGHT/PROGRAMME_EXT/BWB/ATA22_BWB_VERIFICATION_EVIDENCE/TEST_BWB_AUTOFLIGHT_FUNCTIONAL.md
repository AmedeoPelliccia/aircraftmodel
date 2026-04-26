# TEST — BWB Autoflight Functional Test

**Evidence ID:** EV-BWB-22-003
**Doc ID:** T-A2-ATA22-BWB-TEST-001
**Delta Refs:** DELTA-BWB-22-001, DELTA-BWB-22-002, DELTA-BWB-22-005
**CS-25 Ref:** CS-25.1329, CS-25.1302
**Method:** Iron-bird / Simulator / Flight test
**Status:** STUB
**Lifecycle:** Standard (LC01–LC13)
**Content Deferred To:** LC05 (simulator/iron-bird), LC06 (flight test)

---

## 1. Purpose

This test stub defines the scope and structure of BWB autoflight functional testing. It covers delta test cases arising from the distributed effector control allocation (DELTA-BWB-22-001), NDI control laws (DELTA-BWB-22-002), and 4-engine auto-thrust (DELTA-BWB-22-005). SHARED baseline test cases are not repeated.

---

## 2. Test Programme Overview (Stub)

| Test Phase | Facility | Primary Delta | LC Gate |
|---|---|---|---|
| Control allocation verification | Iron-bird (FCS rig) | DELTA-BWB-22-001 | LC05 |
| NDI functional verification | FCC integration bench | DELTA-BWB-22-002 | LC05 |
| AT 4-engine functional | Engine integration rig / simulator | DELTA-BWB-22-005 | LC05 |
| System integration | Full flight simulator (FFS) | All | LC05 |
| Flight test — AP modes | Aircraft | All | LC06 |
| Flight test — AT 4-engine | Aircraft | DELTA-BWB-22-005 | LC06 |

---

## 3. Delta Test Cases (Stub)

### TC-BWB-22-001: Control Allocation — Full Authority Range

| Field | Value |
|---|---|
| Test Case ID | TC-BWB-22-001 |
| Delta Ref | DELTA-BWB-22-001 |
| Requirement | BWB-22-100-003 |
| Objective | Verify control allocation distributes demanded moments across all effector groups correctly |
| Facility | Iron-bird / FCS rig |
| Pass Criteria | Surface deflections match allocation matrix output within TBD deg tolerance (LC03) |
| Status | STUB |
| LC Gate | LC05 |

### TC-BWB-22-002: Control Allocation — Saturation Handling

| Field | Value |
|---|---|
| Test Case ID | TC-BWB-22-002 |
| Delta Ref | DELTA-BWB-22-001 |
| Requirement | BWB-22-100-003 |
| Objective | Verify saturation of one or more surfaces does not destabilise autoflight outer loop |
| Facility | FCC bench + simulation |
| Pass Criteria | AP remains stable and meets CS-25.1329 for TBD saturation combinations (LC04) |
| Status | STUB |
| LC Gate | LC05 |

### TC-BWB-22-003: NDI Engagement / Disengagement

| Field | Value |
|---|---|
| Test Case ID | TC-BWB-22-003 |
| Delta Ref | DELTA-BWB-22-002 |
| Requirement | BWB-22-100-004 |
| Objective | Verify AP disconnects and alerts within TBD ms when NDI error exceeds threshold |
| Facility | FCC bench |
| Pass Criteria | Disconnect within TBD ms (LC03); correct alert generated; FD reverts correctly |
| Status | STUB |
| LC Gate | LC05 |

### TC-BWB-22-004: Auto-Thrust 4-Engine Symmetric Tracking

| Field | Value |
|---|---|
| Test Case ID | TC-BWB-22-004 |
| Delta Ref | DELTA-BWB-22-005 |
| Requirement | BWB-22-300-001 |
| Objective | Verify AT tracks commanded speed with all 4 engines operating |
| Facility | Simulator / flight test |
| Pass Criteria | Speed tracking within TBD kts (LC03) at all operating conditions |
| Status | STUB |
| LC Gate | LC05 |

### TC-BWB-22-005: Auto-Thrust Asymmetric Compensation

| Field | Value |
|---|---|
| Test Case ID | TC-BWB-22-005 |
| Delta Ref | DELTA-BWB-22-005 |
| Requirement | BWB-22-300-002 |
| Objective | Verify AT detects and compensates thrust asymmetry within TBD s (LC03) |
| Facility | Simulator / flight test |
| Pass Criteria | Yaw moment from residual asymmetry < TBD N·m (LC03) |
| Status | STUB |
| LC Gate | LC06 |

---

## 4. Open Items

| Item | Description | LC Gate |
|---|---|---|
| OI-TEST001-001 | Complete test case list from requirements traceability | LC04 |
| OI-TEST001-002 | Define pass criteria numerical values (depend on LC03 analysis) | LC03 |
| OI-TEST001-003 | Schedule iron-bird campaign with ATA 27 rig availability | LC04 |
| OI-TEST001-004 | Define flight test points for AT 4-engine verification | LC05 |
