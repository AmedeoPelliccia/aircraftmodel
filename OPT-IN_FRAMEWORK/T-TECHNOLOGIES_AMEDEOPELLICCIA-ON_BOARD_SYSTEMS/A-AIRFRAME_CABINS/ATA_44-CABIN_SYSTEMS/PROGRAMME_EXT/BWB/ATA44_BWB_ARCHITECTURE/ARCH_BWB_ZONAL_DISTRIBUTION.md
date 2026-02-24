# ARCH-002 — BWB Cabin Zonal Distribution

**Doc ID:** T-A-ATA44-BWB-ARCH-002
**Delta Ref:** DELTA-BWB-44-002
**ATA Subchapter:** 44-10 Cabin Core System
**Status:** DRAFT (LC01 — zone boundaries at LC03)
**Parent:** [Architecture README](README.md)

---

## 1) Purpose

Defines the BWB cabin zones used for CMS addressing, PA routing, IFE group assignment,
monitoring topology, and evacuation route management. Zones are partitioned by both:

1. **Spar bay boundaries** (structural, longitudinal) — primary zone separator
2. **Radial angular segments** (if applicable within a bay) — for wide bays with multiple aisles

---

## 2) Zone Definition Principle

> Δ BWB-specific vs WTW:

- WTW zones are purely longitudinal (fore-to-aft linear).
- BWB zones are **spar-bay-primary, with optional radial subdivision** within a wide bay.
- Zone ID format: `Z<bay_id>-<radial_sector>` (e.g., Z1-A, Z1-B for bay 1 port/starboard).

---

## 3) BWB Cabin Zone Map (placeholder — populate at LC03)

| Zone ID | Spar Bay | Radial Sector | ZC ID | CSU ID | Pax nominal | Notes |
|---------|---------|--------------|-------|--------|-------------|-------|
| Z1-A | Bay 1 | Port | ZC-01 | CSU-01A | TBD | FWD zone, port aisle |
| Z1-B | Bay 1 | Starboard | ZC-01 | CSU-01B | TBD | FWD zone, stbd aisle |
| Z2-A | Bay 2 | Port | ZC-02 | CSU-02A | TBD | — |
| Z2-B | Bay 2 | Starboard | ZC-02 | CSU-02B | TBD | — |
| Z3-A | Bay 3 | Port | ZC-03 | CSU-03A | TBD | — |
| Z3-B | Bay 3 | Starboard | ZC-03 | CSU-03B | TBD | — |
| ... | ... | ... | ... | ... | ... | N_bays TBD |

---

## 4) Zone-to-ZC Assignment Rules

> Δ BWB:

- All radial sectors within a spar bay are served by the same ZC pair for that bay.
- ZC failure in a bay affects all radial sectors in that bay simultaneously.
- Inter-bay ZC failover does **not** propagate across spar bay boundaries without BBU availability.
- Smoke event detected in Z2-A must be reported locally (ZC-02) without dependency on BBU.

---

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Define spar bay boundaries (structural FS) from 3D model | Structures | LC03 |
| Confirm radial sector definition per bay (1 or 2 per bay) | Cabin Engineering | LC03 |
| Publish zone_map.yaml (populated) | Systems Integration | LC03 |

---

## Related Documents

- [MODELS/zone_map.yaml](MODELS/zone_map.yaml)
- [ARCH_BWB_TOPOLOGY_OVERVIEW.md](ARCH_BWB_TOPOLOGY_OVERVIEW.md)
