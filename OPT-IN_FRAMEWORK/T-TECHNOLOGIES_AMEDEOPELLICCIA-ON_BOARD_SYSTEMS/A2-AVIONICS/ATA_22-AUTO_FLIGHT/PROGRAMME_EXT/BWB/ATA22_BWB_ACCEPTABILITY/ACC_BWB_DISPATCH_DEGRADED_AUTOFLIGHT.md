# ACC — BWB Dispatch in Degraded Autoflight States

**Doc ID:** T-A2-ATA22-BWB-ACC-001
**Delta Refs:** DELTA-BWB-22-001, DELTA-BWB-22-002
**Variant:** AMPEL360 Q100 BWB
**Status:** DRAFT
**Lifecycle:** Standard (LC01–LC13)
**Baseline Ref:** `../../..` (ATA 22 SHARED)

---

## 1. Delta Statement

The SHARED baseline dispatch acceptability criteria for degraded autoflight cover conventional failure modes (single FCC failure, single surface failure). The BWB has additional degraded-mode considerations arising from the distributed effector array (DELTA-BWB-22-001) and NDI control law (DELTA-BWB-22-002). This document defines BWB-specific dispatch acceptability criteria as deltas to the SHARED baseline.

---

## 2. Degraded Autoflight Dispatch Scenarios — BWB Delta (Stub)

### 2.1 Effector Group Failure

| Scenario | Autoflight Availability | Dispatch Permitted? | Conditions | LC Gate |
|---|---|---|---|---|
| Single elevon surface failed (one side) | Limited — reduced roll authority | TBD | Must demonstrate adequate roll authority via control allocation reconfiguration | LC04 |
| Single elevon group failed (e.g., all OE one side) | Degraded roll channel | TBD | FHA-determined acceptability — TBD (LC04) | LC04 |
| Spoileron failed one side | Limited — roll and speed brake | TBD | TBD | LC04 |
| Dual elevon group failure (both sides) | Severely degraded | Likely NO — TBD | Catastrophic classification expected | LC04 |

**Minimum effector availability for autoflight engagement:** TBD (LC04) — subject to BWB FHA.

### 2.2 NDI Control Law Degradation

| Scenario | Autoflight Availability | Dispatch Permitted? | Conditions | LC Gate |
|---|---|---|---|---|
| NDI aerodynamic model error flag active | Degraded performance | TBD | Reversion to linear fallback mode (if defined — TBD LC03) | LC03 |
| NDI inner loop divergence detected (pre-flight BIT) | None | NO | Autopilot inoperative — MEL item | LC04 |
| Robustness augmentation unavailable | Degraded robustness | TBD | Reduced flight envelope restrictions — TBD | LC04 |

### 2.3 FCC Partial Failure (NDI Channel)

| Scenario | Autoflight Availability | Dispatch Permitted? | Conditions | LC Gate |
|---|---|---|---|---|
| Single NDI processing channel failed | Reduced redundancy | TBD (MEL) | TBD — FCC redundancy architecture TBD LC04 | LC04 |

---

## 3. Minimum Equipment List (MEL) Hooks

MEL items for BWB-specific degraded autoflight states shall be defined in the BWB MEL supplement at LC05. The following BWB items are expected to require MEL definition:

| MEL Item Ref | System | Condition | Expected Dispatch Status |
|---|---|---|---|
| MEL-BWB-22-01 | Inboard Elevon Actuator (one surface) | Failed neutral | TBD (LC05) |
| MEL-BWB-22-02 | NDI Channel (one of N) | Failed | TBD (LC05) |
| MEL-BWB-22-03 | Control Allocation Module (one channel) | Failed | TBD (LC05) |
| MEL-BWB-22-04 | Auto-Thrust ENG1 or ENG4 channel | Failed | TBD (LC05) |

---

## 4. Open Items

| Item | Description | LC Gate |
|---|---|---|
| OI-ACC001-001 | Minimum effector availability for autoflight engagement (FHA required) | LC04 |
| OI-ACC001-002 | NDI fallback mode definition (linear reversion) | LC03 |
| OI-ACC001-003 | MEL items for all BWB autoflight degraded states | LC05 |
| OI-ACC001-004 | Reduced flight envelope for degraded dispatch (speed/altitude restrictions) | LC04 |
