# ARCH-001 — WTW Cabin Systems Topology Overview

**Doc ID:** T-A-ATA44-WTW-ARCH-001
**Delta Ref:** DELTA-WTW-44-001, DELTA-WTW-44-002
**ATA Subchapter:** 44-10 Cabin Core System
**Status:** DRAFT (LC01 — topology data at LC03)
**Parent:** [Architecture README](README.md)

---

## 1) WTW CMS Architecture Summary

The AMPEL360 WTW Cabin Management System (CMS) is a **centralised-with-distributed-nodes**
architecture tailored to the conventional circular-fuselage layout:

| Layer | Component | Location | Notes |
|-------|-----------|----------|-------|
| Central controller | CMS Main Controller (CMC) | FWD E/E bay (LRU cabinet row TBD) | Redundant pair |
| Secondary controller | CMS AFT Controller (CAC) | AFT equipment bay | Failover / zone 3–4 |
| IFE server | IFE Media Server | FWD avionics bay | See ICD_WTW_IFE_PLACEMENT_001.md |
| Zone satellite units | Cabin Satellite Units (CSU) | Per zone (4 max for WTW Q100) | ARINC 629 / RS-485 bus |
| Seat electronics | ISDU / SEB | Per seat row | Passenger power + IFE |
| Network backbone | ARINC 664 Part 7 (AFDX) | Crown harness run fore-to-aft | 100 Mbit/s cabin domain |
| PA/Crew call | Dedicated audio bus | Sidewall harness run | ATA 23 interface |

---

## 2) WTW vs SHARED Architecture Delta

> Δ WTW-specific (versus SHARED or BWB):

- **Single longitudinal backbone harness** running crown/sidewall fore-to-aft (not spar-bay routing).
- **2–4 cabin zones** (linear, not radial) — zone boundary at bulkhead or seat row.
- **FWD + AFT LRU cabinets** in conventional E/E bay locations.
- **No bay-bridging constraints** — harness runs continuously without structural interruption.

---

## 3) System Boundary

| Interface | Connecting System | ATA |
|-----------|------------------|-----|
| Electrical power | 115V AC / 28V DC bus | ATA 24 |
| PA audio | Audio management system | ATA 23 |
| Fire/smoke sensors | Smoke detection loops | ATA 26 |
| Cabin lighting | Cabin lighting control | ATA 33 |
| Emergency equipment signals | Slide/exit status | ATA 25 / ATA 52 |
| Water/waste status | Lavatory water level | ATA 38 |
| Passenger network | On-board Internet | ATA 46 |

---

## 4) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Define LRU cabinet position from Type Design | Avionics / Cabin Eng | LC03 |
| Confirm zone boundary fuselage station positions | Cabin Engineering | LC03 |
| Produce network topology graphml from system architect | Systems | LC03 |

---

## Related Documents

- [ARCH_WTW_ZONE_DEFINITION.md](ARCH_WTW_ZONE_DEFINITION.md)
- [MODELS/network_topology.graphml](MODELS/network_topology.graphml)
- [ICD_WTW_CONTROLLER_PLACEMENT_001.md](../ATA44_WTW_INTERFACES/ICD_WTW_CONTROLLER_PLACEMENT_001.md)
