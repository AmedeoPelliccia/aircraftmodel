# ICD-BWB-44-003 — BWB ARINC 664 Endpoint Register (per-bay segment)

**Doc ID:** T-A-ATA44-BWB-ICD-003
**Delta Ref:** DELTA-BWB-44-005
**ATA Subchapter:** 44-10 Cabin Core System
**Status:** DRAFT (LC01 — VL/port allocation at LC03)
**Parent:** [Interfaces README](README.md)

---

## 1) Purpose

Per-bay ARINC 664 VL allocation and port register. All values TBD at LC03
from the ARINC 664 network design tool output.

See also: [endpoint_map.yaml](../ATA44_BWB_ARCHITECTURE/MODELS/endpoint_map.yaml)

## 2) Endpoint Register (placeholder)

| Segment | Node ID | Role | VL ID | Src port | Dst port(s) | Bandwidth (Mbit/s) | Notes |
|---------|---------|------|-------|---------|------------|-------------------|-------|
| SEG-01 | ZC-01 | ZoneController | TBD | TBD | TBD | TBD | — |
| SEG-01 | CSU-01A | CabinSatelliteUnit | TBD | TBD | TBD | TBD | — |
| SEG-01 | CSU-01B | CabinSatelliteUnit | TBD | TBD | TBD | TBD | — |
| SEG-01 | IBN-01 | IFE_BayNode | TBD | TBD | TBD | TBD | — |
| SEG-01 | BBU-01 (port) | BridgeUnit | TBD | TBD | TBD | TBD | Bridge link |
| SEG-02 | ZC-02 | ZoneController | TBD | TBD | TBD | TBD | — |
| SEG-02 | CSU-02A | CabinSatelliteUnit | TBD | TBD | TBD | TBD | — |
| SEG-02 | CSU-02B | CabinSatelliteUnit | TBD | TBD | TBD | TBD | — |
| SEG-02 | IBN-02 | IFE_BayNode | TBD | TBD | TBD | TBD | — |
| SEG-02 | BBU-01 (port) | BridgeUnit | TBD | TBD | TBD | TBD | Bridge link |
| SEG-02 | BBU-02 (port) | BridgeUnit | TBD | TBD | TBD | TBD | Bridge link |
| SEG-03 | ZC-03 | ZoneController | TBD | TBD | TBD | TBD | — |
| SEG-03 | CSU-03A | CabinSatelliteUnit | TBD | TBD | TBD | TBD | — |
| SEG-03 | CSU-03B | CabinSatelliteUnit | TBD | TBD | TBD | TBD | — |
| SEG-03 | IBN-03 | IFE_BayNode | TBD | TBD | TBD | TBD | — |
| SEG-03 | BBU-02 (port) | BridgeUnit | TBD | TBD | TBD | TBD | Bridge link |

## 3) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Allocate VL IDs from global VL register | Systems Integration | LC03 |
| Confirm bandwidth allocation from network analysis | Avionics | LC04 |
