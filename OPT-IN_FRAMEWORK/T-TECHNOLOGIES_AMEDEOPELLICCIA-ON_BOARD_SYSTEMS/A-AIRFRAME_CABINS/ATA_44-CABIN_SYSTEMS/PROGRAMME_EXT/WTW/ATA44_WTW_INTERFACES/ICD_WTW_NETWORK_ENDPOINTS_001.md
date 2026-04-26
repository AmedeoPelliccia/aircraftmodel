# ICD-003 — WTW Network Endpoints (ARINC 664 / AFDX)

**ICD ID:** T-A-ATA44-WTW-ICD-003
**Delta Ref:** DELTA-WTW-44-004
**ATA Subchapter:** 44-10 Cabin Core System
**Status:** DRAFT (LC01 — VL/port numbers at LC03)
**Parent:** [Interfaces README](README.md)

---

## 1) Purpose

Narrative description of the WTW ARINC 664 Part 7 (AFDX) cabin domain network endpoints.
Machine-readable register: see [MODELS/icd_endpoints.yaml](../ATA44_WTW_ARCHITECTURE/MODELS/icd_endpoints.yaml).

---

## 2) Network Domain

| Parameter | Value |
|-----------|-------|
| Network | ARINC 664 Part 7 (AFDX) Cabin Domain |
| Backbone speed | 100 Mbit/s full-duplex |
| Addressing scheme | Virtual Link (VL) per sender |
| IP addressing | TBD — cabin domain subnet TBD at LC03 |
| Physical layer | Ethernet 100BASE-TX (STP Cat 5e or ARINC equivalent) |

---

## 3) WTW Endpoint Register Summary

| Node | Role | VL range | Port | Notes |
|------|------|----------|------|-------|
| CMC | Primary controller | TBD | TBD | AFDX switch A (primary) |
| CAC | Secondary controller | TBD | TBD | AFDX switch B (secondary) |
| IFE_SVR | IFE media server | TBD | TBD | Content server + streaming |
| CSU-01 | Zone 1 satellite unit | TBD | TBD | — |
| CSU-02 | Zone 2 satellite unit | TBD | TBD | — |
| CSU-03 | Zone 3 satellite unit | TBD | TBD | — |
| CSU-04 | Zone 4 satellite unit | TBD | TBD | — |

---

## 4) WTW-Specific Constraints

> Δ WTW-only:

- WTW uses a **single AFDX switch redundant pair** (no inter-bay switch segmentation).
- Zone units connect to the same switch pair; no need for inter-switch links (BWB uses bridge units).
- Passenger-network (ATA 46) and CMS (ATA 44) share the same physical Ethernet cable run
  but are logically isolated by separate VL sets and QoS priority.

---

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Run ARINC 664 network design tool to allocate VL IDs and ports | Systems Integration | LC03 |
| Confirm IP subnet assignment with avionics network team | Avionics / IT | LC03 |
| Publish icd_endpoints.yaml (populated) | Systems Integration | LC03 |

---

## Related Documents

- [MODELS/icd_endpoints.yaml](../ATA44_WTW_ARCHITECTURE/MODELS/icd_endpoints.yaml)
- [ARCH_WTW_TOPOLOGY_OVERVIEW.md](../ATA44_WTW_ARCHITECTURE/ARCH_WTW_TOPOLOGY_OVERVIEW.md)
