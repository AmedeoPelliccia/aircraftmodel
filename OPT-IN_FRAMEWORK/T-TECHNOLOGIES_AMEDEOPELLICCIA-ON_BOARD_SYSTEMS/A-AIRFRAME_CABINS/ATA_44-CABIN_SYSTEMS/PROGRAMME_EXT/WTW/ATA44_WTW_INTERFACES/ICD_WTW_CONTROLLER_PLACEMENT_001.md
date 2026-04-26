# ICD-001 — WTW CMS Controller Placement

**ICD ID:** T-A-ATA44-WTW-ICD-001
**Delta Ref:** DELTA-WTW-44-001
**ATA Subchapter:** 44-10 Cabin Core System
**Status:** DRAFT (LC01 — quantitative data at LC03)
**Parent:** [Interfaces README](README.md)

---

## 1) Purpose

Defines the placement envelope, mounting provisions, and connector-face orientation for:

- **CMC** — CMS Main Controller (primary) — FWD E/E bay
- **CAC** — CMS AFT Controller (secondary/failover) — AFT equipment bay

---

## 2) Interface Summary

| Item | Description | Value / Location |
|------|-------------|-----------------|
| CMC fuselage station | FWD E/E bay LRU cabinet | TBD FS — populate at LC03 |
| CMC buttock line | Centre-line of LRU cabinet row | TBD BL |
| CMC waterline | Equipment bay floor level + TBD mm | TBD WL |
| CAC fuselage station | AFT equipment bay | TBD FS |
| CAC BL | TBD | TBD |
| CMC LRU form factor | ARINC 600 3MCU or TBD | TBD at LC03 |
| Connector face | Aft-facing (CMC) / Fwd-facing (CAC) | TBD at LC03 |
| Cooling airflow | From E/E bay cooling duct | Min TBD m³/min at LC04 |

---

## 3) WTW-Specific Constraints

> Δ WTW-only:

- CMC in FWD E/E bay (conventional position) — **no** distributed bay-by-bay arrangement.
- CAC in AFT equipment bay — single longitudinal cable run to interconnect CMC/CAC.
- Both units accessible via conventional E/E bay access panels (no spar-bay access required).

---

## 4) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Define CMC/CAC FS/BL/WL coordinates from 3D model | Avionics Inst. Eng | LC03 |
| Confirm LRU form-factor and cooling airflow requirement | LRU supplier | LC03 |
| Publish CATIA installation drawing ref | Avionics Inst. Eng | LC04 |

---

## Related Documents

- [ARCH_WTW_TOPOLOGY_OVERVIEW.md](../ATA44_WTW_ARCHITECTURE/ARCH_WTW_TOPOLOGY_OVERVIEW.md)
- [REQ_WTW_44_100_CABIN_CORE.yaml](../ATA44_WTW_REQUIREMENTS/REQ_WTW_44_100_CABIN_CORE.yaml)
