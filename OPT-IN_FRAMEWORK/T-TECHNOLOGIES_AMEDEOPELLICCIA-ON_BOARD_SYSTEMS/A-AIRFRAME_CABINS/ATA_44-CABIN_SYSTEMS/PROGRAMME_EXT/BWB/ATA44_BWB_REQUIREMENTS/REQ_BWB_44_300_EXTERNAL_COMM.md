---
id: REQ_BWB_44_300
subchapter: "44-30"
title: "External Communication — BWB Antenna Placement"
variant: BWB
revision: RevA
lc_gate: LC01
---

# REQ\_BWB\_44\_300 — External Comm: Antenna Placement (BWB Fuselage)

**Subchapter:** 44-30  
**Variant:** BWB  
**Revision:** RevA  
**LC Gate:** LC01  

## Purpose

Defines the external communication antenna placement requirements specific to the AMPEL360 BWB variant, reflecting the distinct outer mould line (OML), composite lower surface, and spar bay structural attachment constraints of the BWB planform.

## Requirements

### BWB-44-300-001 — Antenna Placement on BWB Lower Surface

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-300-001 |
| **cs25_ref** | CS-25.1353 |
| **verification** | inspection |
| **lc_gate** | LC05 |

**SHALL:** External communication antennas SHALL be placed on the BWB lower surface consistent with BWB fuselage envelope constraints. Placement SHALL avoid structural spar bay attachment points.

**Rationale:** BWB outer mould line differs from WTW circular fuselage. Antenna positions must be derived from BWB structural and aerodynamic surface definitions.

---

### BWB-44-300-002 — RF Compliance at BWB Antenna Positions

| Field | Value |
|-------|-------|
| **req_id** | BWB-44-300-002 |
| **cs25_ref** | — |
| **standard_ref** | ETSI EN 303 360 |
| **verification** | test |
| **lc_gate** | LC07 |

**SHALL:** RF emissions from external communication antennas SHALL comply with ETSI EN 303 360 at all BWB antenna installation positions.

**Rationale:** BWB composite skin may have different shielding effectiveness than WTW metallic fuselage. RF compliance must be re-verified for BWB geometry.

---

## Cross-References

- `../ATA44_BWB_COMPLIANCE_MATRIX.md` — ETSI EN 303 360 / CS-25.1353 traceability rows
- ATA 57 BWB structural envelope — spar bay attachment zone exclusions
