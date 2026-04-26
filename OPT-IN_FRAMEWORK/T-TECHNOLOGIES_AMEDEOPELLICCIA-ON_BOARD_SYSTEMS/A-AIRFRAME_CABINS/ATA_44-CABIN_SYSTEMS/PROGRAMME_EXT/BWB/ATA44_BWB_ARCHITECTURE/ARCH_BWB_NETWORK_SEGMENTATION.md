# ARCH-003 — BWB ARINC 664 Network Segmentation

**Doc ID:** T-A-ATA44-BWB-ARCH-003
**Delta Ref:** DELTA-BWB-44-003, DELTA-BWB-44-005
**ATA Subchapter:** 44-10 Cabin Core System
**Status:** DRAFT (LC01 — network design at LC03)
**Parent:** [Architecture README](README.md)

---

## 1) Purpose

Defines the BWB ARINC 664 Part 7 (AFDX) cabin network segmentation strategy driven
by the spar bay structural boundaries. Each spar bay has an independent AFDX switch
pair; bays are connected via dedicated inter-bay Bay Bridge Units (BBU).

---

## 2) Network Segmentation Architecture

> Δ BWB vs WTW:
> WTW uses a single AFDX switch pair for the entire cabin (no inter-bay segmentation).
> BWB MUST segment per bay due to structural harness routing constraints.

| Segment | Scope | Switch pair | Bridge to adjacent segment |
|---------|-------|-------------|---------------------------|
| SEG-01 | Bay 1 | SW-01A / SW-01B | BBU-01 (to SEG-02) |
| SEG-02 | Bay 2 | SW-02A / SW-02B | BBU-01 (to SEG-01), BBU-02 (to SEG-03) |
| SEG-03 | Bay 3 | SW-03A / SW-03B | BBU-02 (to SEG-02), BBU-03 (to SEG-04) |
| ... | ... | ... | ... |

---

## 3) Bay Bridge Unit (BBU) Specification

| Parameter | Value | Notes |
|-----------|-------|-------|
| BBU form factor | TBD | 1 ATR or embedded in ZC — LC03 |
| Bridging protocol | ARINC 664 Part 7 inter-domain bridge | VL translation at boundary |
| Inter-bay latency | TBD ms | Budget TBD at LC04; affects PA announcement sync |
| Fault containment | BBU loss isolates two adjacent segments | Must not propagate fault across more than 2 bays |
| Physical interface | Hardened connector at spar bay doubler | ATA 53 structural interface |

---

## 4) Latency Budget Framework

| Traffic class | Source | Destination | Latency budget | Notes |
|--------------|--------|-------------|---------------|-------|
| Smoke/fire alarm | ZC-n (local) | All ZCs | TBD ms end-to-end | Must not require BBU (local detection) |
| PA announcement sync | ZC-01 | ZC-N (all) | TBD ms | Acceptability TBD at LC04 |
| IFE content sync | IBN-n | Adjacent IBN | TBD ms | Per-bay distribution reduces cross-bay load |
| CMS heartbeat | ZC-n → ZC-n+1 | Via BBU | TBD ms | Monitoring only — not safety-essential |

---

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Confirm N_bays and BBU count from structural design | Systems | LC03 |
| Define BBU form factor and FS/BL/WL placement | Avionics Inst. Eng | LC03 |
| Define latency budgets from PA / smoke alarm analysis | Systems Safety | LC04 |
| Produce network_topology.graphml from AFDX network design tool | Systems Integration | LC03 |

---

## Related Documents

- [MODELS/network_topology.graphml](MODELS/network_topology.graphml)
- [MODELS/endpoint_map.yaml](MODELS/endpoint_map.yaml)
- [ICD_BWB_NETWORK_SEGMENTATION_001.md](../ATA44_BWB_INTERFACES/ICD_BWB_NETWORK_SEGMENTATION_001.md)
