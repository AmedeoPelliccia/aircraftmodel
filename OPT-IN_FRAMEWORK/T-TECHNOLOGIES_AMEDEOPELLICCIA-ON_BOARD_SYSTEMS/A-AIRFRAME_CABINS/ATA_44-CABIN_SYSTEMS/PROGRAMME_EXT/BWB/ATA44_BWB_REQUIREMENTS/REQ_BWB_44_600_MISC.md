---
id: REQ_BWB_44_600
subchapter: "44-60"
title: "Miscellaneous — BWB CMS Deltas"
variant: BWB
revision: RevA
lc_gate: LC01
---

# REQ\_BWB\_44\_600 — Miscellaneous: BWB CMS System Deltas

**Subchapter:** 44-60  
**Variant:** BWB  
**Revision:** RevA  
**LC Gate:** LC01  

## Purpose

Captures miscellaneous BWB-specific CMS deltas not covered by the core subchapter packs (44-10 through 44-50), including dynamic ZC zone reconfiguration capability and environmental qualification requirements for per-bay LRUs.

## Requirements

### BWB-44-600-001 — Dynamic Zone Reconfiguration via BBU

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-600-001 |
| **cs25_ref** | CS-25.1309 |
| **verification** | analysis |
| **lc_gate** | LC05 |

**SHALL:** CMS software SHALL support dynamic zone reconfiguration to reassign sensor monitoring from a failed ZC to an adjacent bay ZC via BBU, without requiring physical access.

**Rationale:** Distributed ZC architecture increases the likelihood of partial system degradation. Software reconfiguration reduces crew workload and maintenance costs.

---

### BWB-44-600-002 — Environmental Qualification of BWB CMS LRUs

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-600-002 |
| **cs25_ref** | — |
| **standard_ref** | ED-14G (DO-160G) |
| **verification** | test |
| **lc_gate** | LC07 |

**SHALL:** All BWB CMS LRUs (ZC, BBU, IBN) SHALL be compliant with ED-14G (DO-160G) environmental conditions applicable to the installed bay environment.

**Rationale:** Per-bay environmental conditions may differ from centralised E/E bay used in WTW. Environmental qualification per bay required.

---

## Cross-References

- `REQ_BWB_44_100_CABIN_CORE.yaml` — ZC and BBU architecture (BWB-44-100-001–005)
- `../ATA44_BWB_ACCEPTABILITY/` — dispatch rules for degraded ZC/BBU/IBN mode
- `../ATA44_BWB_COMPLIANCE_MATRIX.md` — CS-25.1309 and ED-14G traceability rows
