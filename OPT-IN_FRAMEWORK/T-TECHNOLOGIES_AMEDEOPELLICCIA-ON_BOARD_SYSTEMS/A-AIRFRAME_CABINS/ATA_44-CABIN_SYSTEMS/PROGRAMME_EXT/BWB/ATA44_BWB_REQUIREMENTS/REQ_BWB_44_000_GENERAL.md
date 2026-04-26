---
id: REQ_BWB_44_000
subchapter: "44-000"
title: "General — BWB Applicability"
variant: BWB
revision: RevA
lc_gate: LC01
---

# REQ\_BWB\_44\_000 — General: BWB-Specific Applicability and Scope

**Subchapter:** 44-000  
**Variant:** BWB  
**Revision:** RevA  
**LC Gate:** LC01  

## Purpose

This requirement pack establishes the applicability boundary and architectural scope for the ATA 44 BWB Programme Extension overlay. All requirements herein are deltas to the ATA 44 SHARED baseline.

## Requirements

### BWB-44-000-001 — Variant Applicability

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-000-001 |
| **cs25_ref** | — |
| **verification** | analysis |
| **lc_gate** | LC01 |

**SHALL:** The ATA 44 BWB overlay SHALL apply only to the AMPEL360 BWB variant. All requirements herein are deltas to the ATA 44 SHARED baseline.

**Rationale:** Prevent misapplication to WTW variant. WTW uses a centralised CMC/CAC topology not applicable to BWB.

---

### BWB-44-000-002 — Distributed Zone Controller Topology

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-000-002 |
| **cs25_ref** | CS-25.1309 |
| **verification** | analysis |
| **lc_gate** | LC03 |

**SHALL:** The BWB cabin systems architecture SHALL use a per-spar-bay distributed Zone Controller (ZC) topology in lieu of a centralised CMC.

**Rationale:** BWB composite planform creates multiple spar bays that impose structural constraints on harness routing. Centralised CMC is impractical.

---

### BWB-44-000-003 — Bay Bridge Unit Requirement for Cross-Bay Harness

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-000-003 |
| **cs25_ref** | CS-25.1353 |
| **verification** | inspection |
| **lc_gate** | LC03 |

**SHALL:** No ATA 44 CMS harness SHALL bridge more than one spar bay structural boundary via a single uninterrupted run without a Bay Bridge Unit (BBU) at the boundary.

**Rationale:** Structural spar bay boundaries require grommet/doubler penetrations. Uninterrupted routing of large bundles across multiple boundaries is structurally impractical and maintenance-heavy.

---

## Cross-References

- ATA 44 SHARED baseline
- `../ATA44_BWB_INDEX.yaml` — overlay delta index
- `../ATA44_BWB_COMPLIANCE_MATRIX.md` — CS-25 traceability
