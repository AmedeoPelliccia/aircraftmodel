# ARCH-001 — BWB Cabin Systems Topology Overview

**Doc ID:** T-A-ATA44-BWB-ARCH-001
**Delta Ref:** DELTA-BWB-44-001, DELTA-BWB-44-002
**ATA Subchapter:** 44-10 Cabin Core System
**Status:** DRAFT (LC01 — topology data at LC03)
**Parent:** [Architecture README](README.md)

---

## 1) BWB CMS Architecture Summary

The AMPEL360 BWB Cabin Management System (CMS) is a **fully distributed per-bay Zone
Controller (ZC)** architecture driven by the composite wide-body multi-spar planform:

| Layer | Component | Location | Notes |
|-------|-----------|----------|-------|
| Per-bay zone controller | Zone Controller (ZC) | One per spar bay (N bays TBD) | Redundant pair per bay |
| Inter-bay bus controller | Bay Bridge Unit (BBU) | At spar bay structural boundary | Provides AFDX inter-segment bridge |
| IFE distribution node | IFE Bay Node (IBN) | One per spar bay | Per-bay content server/repeater |
| Zone satellite units | Cabin Satellite Units (CSU) | Per zone within bay | ARINC 664 per-bay AFDX segment |
| Seat electronics | ISDU / SEB | Per seat row | Passenger power + IFE |
| Network backbone | Per-bay ARINC 664 (AFDX) | Bay-internal | 100 Mbit/s per segment |
| Inter-bay network | ARINC 664 bridge links | Via BBU at each spar boundary | Latency budget TBD at LC04 |
| PA/Crew call | Dedicated audio bus | Bay-internal + inter-bay extension | ATA 23 interface |

---

## 2) BWB vs WTW Architecture Delta

> Δ BWB-specific (versus WTW):

- **No single centralised CMC** — each spar bay has an independent ZC pair.
- **Bay-boundary harness penetrations** — harness must cross spar bay walls through structural doublers/grommets.
- **Inter-bay bridge switches (BBU)** — required to allow CMS status propagation across bays.
- **Radial + bay zone topology** — zones defined by both spar bay (longitudinal) and angular position (radial aisle flow).
- **IFE per-bay distribution** — eliminates high-bandwidth content streaming across inter-bay bridge.

---

## 3) System Boundary

| Interface | Connecting System | ATA |
|-----------|------------------|-----|
| Electrical power (per bay) | 115V AC / 28V DC per-bay bus | ATA 24 |
| PA audio | Audio management system | ATA 23 |
| Fire/smoke sensors (per bay) | Per-bay smoke detection loops | ATA 26 |
| Cabin lighting | Per-bay lighting control | ATA 33 |
| Emergency equipment signals | Slide/exit status | ATA 25 / ATA 52 |
| Water/waste | Lavatory water level | ATA 38 |
| Passenger network | On-board Internet | ATA 46 |
| Structure (spar bays) | Bay boundary doublers/grommets | ATA 53 |

---

## 4) Number of Bays (placeholder)

| Parameter | Value | Notes |
|-----------|-------|-------|
| Number of spar bays (N_bays) | TBD | From BWB structural design — LC03 |
| ZC pairs (total) | TBD = N_bays | One redundant pair per bay |
| BBU count | TBD = N_bays − 1 | One bridge per inter-bay boundary |
| IFE nodes | TBD = N_bays | One node per bay |

---

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Confirm N_bays from structural design | Structures / Cabin Eng | LC03 |
| Define ZC position from 3D model per bay | Avionics Inst. Eng | LC03 |
| Confirm inter-bay bridge (BBU) latency budget | Systems | LC04 |

---

## Related Documents

- [ARCH_BWB_ZONAL_DISTRIBUTION.md](ARCH_BWB_ZONAL_DISTRIBUTION.md)
- [ARCH_BWB_NETWORK_SEGMENTATION.md](ARCH_BWB_NETWORK_SEGMENTATION.md)
- [MODELS/network_topology.graphml](MODELS/network_topology.graphml)
