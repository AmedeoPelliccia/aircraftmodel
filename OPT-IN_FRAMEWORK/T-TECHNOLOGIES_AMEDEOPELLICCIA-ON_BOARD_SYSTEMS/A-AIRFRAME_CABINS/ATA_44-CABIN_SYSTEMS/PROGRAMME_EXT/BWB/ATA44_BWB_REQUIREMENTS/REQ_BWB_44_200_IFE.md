---
id: REQ_BWB_44_200
subchapter: "44-20"
title: "In-Flight Entertainment — BWB Per-Bay IFE Bay Node Requirements"
variant: BWB
revision: RevA
lc_gate: LC01
---

# REQ\_BWB\_44\_200 — IFE: Per-Bay IFE Bay Node Requirements

**Subchapter:** 44-20  
**Variant:** BWB  
**Revision:** RevA  
**LC Gate:** LC01  

## Purpose

Defines the per-bay In-Flight Entertainment (IFE) architecture for the AMPEL360 BWB variant, covering IFE Bay Node (IBN) deployment, inter-bay synchronisation constraints, and flammability compliance for distributed IFE LRUs.

## Requirements

### BWB-44-200-001 — Per-Bay IBN Deployment

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-200-001 |
| **cs25_ref** | CS-25.853 |
| **verification** | analysis |
| **lc_gate** | LC03 |

**SHALL:** Each spar bay SHALL have at least one IFE Bay Node (IBN) providing local content distribution to seats within that bay.

**Rationale:** BWB per-bay IFE topology eliminates high-bandwidth content streaming across inter-bay bridges (BBU), which have limited bandwidth budgets.

---

### BWB-44-200-002 — Inter-Bay Metadata Synchronisation Bandwidth

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-200-002 |
| **cs25_ref** | CS-25.1309 |
| **verification** | analysis |
| **lc_gate** | LC04 |

**SHALL:** IFE Bay Nodes SHALL synchronise content metadata across bays via the BBU at a bandwidth not exceeding TBD Mbit/s [LC04 gate].

**Rationale:** Inter-bay bridge bandwidth is shared with CMS safety-essential data. IFE sync must be low-bandwidth (metadata only) to avoid congestion.

---

### BWB-44-200-003 — IBN Flammability Compliance

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-200-003 |
| **cs25_ref** | CS-25.853 |
| **verification** | test |
| **lc_gate** | LC07 |

**SHALL:** All IFE Bay Node materials and LRU enclosures SHALL comply with CS-25.853(a) flammability requirements.

**Rationale:** Distributed IBN LRUs are inside the pressure vessel. Flammability compliance required for all materials per certification basis.

---

## Cross-References

- `REQ_BWB_44_100_CABIN_CORE.yaml` — BBU bandwidth budget (BWB-44-100-003/004)
- `../ATA44_BWB_INTERFACES/ICD_BWB_IFE_PLACEMENT_001.md` — IFE placement ICD
- `../ATA44_BWB_COMPLIANCE_MATRIX.md` — CS-25.853 traceability row
