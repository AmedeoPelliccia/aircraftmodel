# ARCH-002 — WTW Cabin Zone Definition

**Doc ID:** T-A-ATA44-WTW-ARCH-002
**Delta Ref:** DELTA-WTW-44-002
**ATA Subchapter:** 44-10 Cabin Core System
**Status:** DRAFT (LC01 — zone boundaries at LC03)
**Parent:** [Architecture README](README.md)

---

## 1) Purpose

Defines the WTW cabin zones used for CMS addressing, PA routing, IFE group assignment,
and monitoring topology. Zones are bounded by fuselage station (FS) positions and
aligned with structural bulkheads or seat-row breaks.

---

## 2) WTW Cabin Zone Map (placeholder — populate at LC03)

| Zone ID | Name | FWD Boundary (FS) | AFT Boundary (FS) | CSU ID | Pax count (nominal) | Notes |
|---------|------|--------------------|-------------------|--------|---------------------|-------|
| Z1 | Forward Cabin | TBD mm | TBD mm | CSU-01 | TBD | Incl. FWD galley/lav |
| Z2 | Mid-Forward Cabin | TBD mm | TBD mm | CSU-02 | TBD | — |
| Z3 | Mid-Aft Cabin | TBD mm | TBD mm | CSU-03 | TBD | — |
| Z4 | Aft Cabin | TBD mm | TBD mm | CSU-04 | TBD | Incl. AFT galley/lav |

---

## 3) Zone-to-LRU Assignment

| Zone | CSU | Controller | PA amp | IFE node |
|------|-----|-----------|--------|---------|
| Z1 | CSU-01 | CMC (primary) | AMP-01 | IFE-Z1 |
| Z2 | CSU-02 | CMC (primary) | AMP-02 | IFE-Z2 |
| Z3 | CSU-03 | CAC (secondary) | AMP-03 | IFE-Z3 |
| Z4 | CSU-04 | CAC (secondary) | AMP-04 | IFE-Z4 |

---

## 4) Zone Boundary Rules

> Δ WTW-specific:

- Zone boundary shall align with a structural bulkhead or a defined seat-row break per WTW cabin plan.
- Zone boundary does **not** align with spar bays (no spar structure in WTW fuselage).
- Harness routing is continuous through zone boundaries (no structural penetration required).
- IFE group boundary shall coincide with CMS zone boundary.

---

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Define zone FS boundaries from cabin layout drawing | Cabin Engineering | LC03 |
| Confirm pax count per zone for CMS addressing | Cabin Engineering | LC03 |
| Publish zone_map.yaml (machine-readable) | Systems Integration | LC03 |

---

## Related Documents

- [MODELS/zone_map.yaml](MODELS/zone_map.yaml)
- [ARCH_WTW_TOPOLOGY_OVERVIEW.md](ARCH_WTW_TOPOLOGY_OVERVIEW.md)
