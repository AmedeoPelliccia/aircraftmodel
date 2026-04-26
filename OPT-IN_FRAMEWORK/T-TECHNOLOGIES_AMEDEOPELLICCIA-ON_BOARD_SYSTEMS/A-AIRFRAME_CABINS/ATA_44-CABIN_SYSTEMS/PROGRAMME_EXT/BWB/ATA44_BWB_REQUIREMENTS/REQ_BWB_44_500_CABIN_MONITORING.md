---
id: REQ_BWB_44_500
subchapter: "44-50"
title: "Cabin Monitoring — BWB Bay-Partitioned Monitoring Topology"
variant: BWB
revision: RevA
lc_gate: LC01
---

# REQ\_BWB\_44\_500 — Cabin Monitoring: Bay-Partitioned Monitoring and Smoke Detection

**Subchapter:** 44-50  
**Variant:** BWB  
**Revision:** RevA  
**LC Gate:** LC01  

## Purpose

Defines the cabin monitoring requirements for the AMPEL360 BWB variant, covering bay-partitioned sensor loops, autonomous per-bay smoke and temperature detection, inter-bay alert propagation via BBU, and crew display identification of event origin.

## Requirements

### BWB-44-500-001 — Bay-Partitioned Sensor Loops (Autonomous Detection)

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-500-001 |
| **cs25_ref** | CS-25.854, CS-25.1309 |
| **verification** | test |
| **lc_gate** | LC06 |

**SHALL:** Smoke and temperature sensor loops SHALL be partitioned per spar bay. A sensor event in Bay N SHALL be locally processed by ZC-N without requiring BBU availability.

**Rationale:** Fire/smoke detection is safety-essential. BBU failure must not prevent detection or alert in the affected bay.

---

### BWB-44-500-002 — Inter-Bay Smoke Alert Propagation

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-500-002 |
| **cs25_ref** | CS-25.854 |
| **verification** | test |
| **lc_gate** | LC06 |

**SHALL:** Upon detection of a smoke event in Bay N, ZC-N SHALL transmit an inter-bay alert to all other ZCs via BBU within TBD ms [LC04 gate] when BBU is available.

**Rationale:** Crew situational awareness requires multi-bay smoke alert even if source bay is identified. Inter-bay propagation is best-effort (not safety-essential path).

---

### BWB-44-500-003 — Bay and Zone Identification on Crew Display

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-500-003 |
| **cs25_ref** | CS-25.854 |
| **verification** | test |
| **lc_gate** | LC07 |

**SHALL:** The cabin monitoring system SHALL uniquely identify the bay and zone of origin for all smoke and temperature events to crew display.

**Rationale:** Crew must be able to identify the physical location of a cabin event for effective fire/smoke response in the multi-bay BWB layout.

---

## Cross-References

- `REQ_BWB_44_100_CABIN_CORE.yaml` — ZC autonomous operation (BWB-44-100-002)
- `../ATA44_BWB_COMPLIANCE_MATRIX.md` — CS-25.854 traceability row
- `../ATA44_BWB_VERIFICATION_EVIDENCE/` — CMS functional test stub
