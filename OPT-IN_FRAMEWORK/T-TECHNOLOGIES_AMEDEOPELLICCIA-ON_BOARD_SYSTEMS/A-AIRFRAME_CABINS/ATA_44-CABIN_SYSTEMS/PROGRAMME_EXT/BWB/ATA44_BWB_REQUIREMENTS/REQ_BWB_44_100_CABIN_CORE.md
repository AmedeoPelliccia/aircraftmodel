---
id: REQ_BWB_44_100
subchapter: "44-10"
title: "Cabin Core System — BWB Distributed ZC and Bay Bridge Architecture"
variant: BWB
revision: RevA
lc_gate: LC01
---

# REQ\_BWB\_44\_100 — Cabin Core: Distributed ZC, Bay Segmentation, BBU, Zone Topology

**Subchapter:** 44-10  
**Variant:** BWB  
**Revision:** RevA  
**LC Gate:** LC01  

## Purpose

Defines the cabin core system architecture for the AMPEL360 BWB variant, covering the distributed Zone Controller (ZC) topology, bay segmentation rules, Bay Bridge Unit (BBU) deployment, and zone topology constraints imposed by the BWB multi-spar-bay planform.

## Requirements

### BWB-44-100-001 — Per-Bay ZC Pair

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-100-001 |
| **cs25_ref** | CS-25.1309 |
| **verification** | analysis |
| **lc_gate** | LC04 |

**SHALL:** Each spar bay SHALL have at least one independent Zone Controller (ZC) pair installed within that bay.

**Rationale:** ZC failure must not affect cabin management in adjacent bays. Bay-autonomous operation required.

---

### BWB-44-100-002 — Bay-Local ZC Autonomous Function

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-100-002 |
| **cs25_ref** | CS-25.1309, CS-25.854 |
| **verification** | test |
| **lc_gate** | LC06 |

**SHALL:** Each ZC SHALL maintain bay-local PA announcement, smoke event detection, and cabin call routing independently of Bay Bridge Unit (BBU) availability.

**Rationale:** BBU loss must not degrade safety-essential CMS functions. Fire/smoke alarms must be locally processed.

---

### BWB-44-100-003 — Inter-Bay BBU Deployment

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-100-003 |
| **cs25_ref** | CS-25.1309 |
| **verification** | analysis |
| **lc_gate** | LC04 |

**SHALL:** Adjacent spar bays SHALL be connected by a Bay Bridge Unit (BBU) providing ARINC 664 inter-domain bridging. Maximum one BBU per bay boundary.

**Rationale:** CMS status propagation and PA synchronisation across bays requires inter-bay bridging. Prohibits daisy-chain amplification of latency.

---

### BWB-44-100-004 — PA Announcement Latency Budget

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-100-004 |
| **cs25_ref** | CS-25.1309 |
| **verification** | analysis |
| **lc_gate** | LC04 |

**SHALL:** The end-to-end latency from smoke event trigger to all-bay PA announcement initiation SHALL be less than TBD ms [LC04 gate].

**Rationale:** PA synchronisation across bays required for emergency announcements. Latency budget TBD from BBU and AFDX bridge characterisation.

---

### BWB-44-100-005 — ZC Bonding Resistance

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-100-005 |
| **cs25_ref** | CS-25.1353 |
| **verification** | inspection |
| **lc_gate** | LC06 |

**SHALL:** Each ZC SHALL be electrically bonded to the local bay structure with a resistance of ≤2.5 mΩ.

**Rationale:** EMC bonding requirement per ATA 20 standard practices. Distributed ZC topology requires per-bay bonding verification.

---

## Cross-References

- `REQ_BWB_44_000_GENERAL.yaml` — applicability and scope
- `../ATA44_BWB_INTERFACES/ICD_BWB_NETWORK_SEGMENTATION_001.md` — AFDX segmentation and BBU ICD
- `../ATA44_BWB_COMPLIANCE_MATRIX.md` — CS-25.1309 traceability row
