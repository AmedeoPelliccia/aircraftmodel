# ACC — BWB Mode Reversion and Alerting

**Doc ID:** T-A2-ATA22-BWB-ACC-002
**Delta Refs:** DELTA-BWB-22-002, DELTA-BWB-22-003
**Variant:** AMPEL360 Q100 BWB
**Status:** DRAFT
**Lifecycle:** Standard (LC01–LC13)
**Baseline Ref:** `../../..` (ATA 22 SHARED)

---

## 1. Delta Statement

The SHARED baseline mode reversion and alerting criteria cover conventional autopilot disconnect, mode transitions, and envelope cautions. The BWB introduces additional mode reversion triggers specific to NDI control law monitoring (DELTA-BWB-22-002) and BWB-specific envelope protection (DELTA-BWB-22-003). This document defines the delta criteria only.

---

## 2. BWB-Specific Mode Reversion Triggers (Stub)

The following triggers are in addition to SHARED baseline reversion triggers:

| Trigger ID | Condition | Reversion Action | Alert | LC Gate |
|---|---|---|---|---|
| REV-BWB-001 | NDI inversion error > TBD threshold | AP disconnects; FD reverts to raw data | MASTER WARNING + EICAS "AP NDI FAULT" | LC03 |
| REV-BWB-002 | Control allocation infeasibility (no solution within TBD iter) | AP disconnects; surface demands freeze then null | MASTER WARNING + EICAS "AP CA FAULT" | LC03 |
| REV-BWB-003 | Envelope protection HARD limit engaged | AP remains engaged; guidance target modified to exit envelope | MASTER CAUTION + EICAS "ENV PROT ACTIVE" | LC03 |
| REV-BWB-004 | Envelope protection HARD limit exceeded for > TBD s | AP disconnects if envelope not recovering | MASTER WARNING + EICAS "ENV PROT EXCEEDED" | LC03 |
| REV-BWB-005 | Effector group loss reduces roll authority below TBD % | AP degrades to limited mode (CA-RECONFIG) | EICAS "AP DEGRADED — CA RECONFIG" | LC04 |
| REV-BWB-006 | 2× engine failure on same wing during autoflight | AP requests crew acknowledgement within TBD s; disconnects if not acknowledged | MASTER WARNING + EICAS "AT ASYM LIMIT" | LC04 |

---

## 3. Mode Reversion Sequence Philosophy (Stub)

For BWB, the mode reversion philosophy follows a **graceful degradation** approach:

1. **Soft limit warning** → Autoflight modifies guidance target to recover (transparent to crew unless they notice guidance change)
2. **Hard limit engagement** → Autoflight actively limits guidance; EICAS caution; crew aware but not required to act immediately
3. **Hard limit sustained / unrecoverable** → Autoflight disconnects with MASTER WARNING; crew takes manual control
4. **Post-disconnect** → FD provides guidance cues to assist manual recovery; cue scaling as defined in REQ_BWB_22_100_AUTOPILOT_AND_FD.yaml (BWB-22-100-006)

**Detailed timing values and mode transition logic:** TBD (LC03).

---

## 4. Alerting Priority and EICAS Message Design (Stub)

| Message | Level | Conditions | Action Required | LC Gate |
|---|---|---|---|---|
| `AP NDI FAULT` | WARNING | NDI divergence | Immediate manual takeover | LC04 |
| `AP CA FAULT` | WARNING | Control allocation fail | Immediate manual takeover | LC04 |
| `ENV PROT ACTIVE` | CAUTION | Any hard limit engaged | Crew awareness; monitor | LC04 |
| `ENV PROT EXCEEDED` | WARNING | Hard limit persistent | Manual takeover | LC04 |
| `AP DEGRADED — CA RECONFIG` | CAUTION | Effector loss, limited autoflight | Check MEL; accept or reject | LC05 |
| `AT ASYM LIMIT` | WARNING | Thrust asymmetry exceeds limit | Manual AT management | LC04 |

EICAS message text, colours, and audio tones are **TBD (LC04)** — subject to human factors review.

---

## 5. Open Items

| Item | Description | LC Gate |
|---|---|---|
| OI-ACC002-001 | NDI divergence threshold for mode reversion trigger | LC03 |
| OI-ACC002-002 | Timing of HARD limit sustained reversion | LC03 |
| OI-ACC002-003 | EICAS message text, colour, audio design (human factors review) | LC04 |
| OI-ACC002-004 | Flight deck alerting integration with ATA 31/45 | LC04 |
| OI-ACC002-005 | Crew procedures for all BWB autoflight alert types | LC05 |
