# ICD-BWB-44-002 — BWB ARINC 664 Network Segmentation + BBU Topology

**Doc ID:** T-A-ATA44-BWB-ICD-002
**Delta Ref:** DELTA-BWB-44-003, DELTA-BWB-44-005
**ATA Subchapter:** 44-10 Cabin Core System
**Status:** DRAFT (LC01 — network design data at LC03)
**Parent:** [Interfaces README](README.md)

---

## 1) Purpose

Interface control document for the ARINC 664 Part 7 (AFDX) cabin network in the BWB.
Each spar bay hosts an independent AFDX switch pair; bays are bridged via Bay Bridge
Units (BBU) mounted at structural spar bay boundaries.

## 2) Per-Bay Segment Summary

> Δ BWB vs WTW: WTW uses a single cabin AFDX switch pair. BWB requires one per bay.

| Segment | Bay | Switch A ID | Switch B ID | VLs allocated | Notes |
|---------|-----|------------|------------|--------------|-------|
| SEG-01 | Bay 1 | SW-01A | SW-01B | TBD | ZC-01, CSU-01A/B, IBN-01 |
| SEG-02 | Bay 2 | SW-02A | SW-02B | TBD | ZC-02, CSU-02A/B, IBN-02 |
| SEG-03 | Bay 3 | SW-03A | SW-03B | TBD | ZC-03, CSU-03A/B, IBN-03 |

## 3) Bay Bridge Unit (BBU) Interface

| BBU ID | Segment A | Segment B | BBU FS (at spar boundary) | Bridge protocol | Notes |
|--------|---------|---------|--------------------------|----------------|-------|
| BBU-01 | SEG-01 | SEG-02 | TBD | ARINC 664 inter-domain bridge | Mounted at Bay 1/2 spar boundary |
| BBU-02 | SEG-02 | SEG-03 | TBD | ARINC 664 inter-domain bridge | Mounted at Bay 2/3 spar boundary |

## 4) Latency Budget (TBD at LC04)

| Path | Hops | Budget (ms) | Constraint |
|------|------|------------|-----------|
| ZC-01 → ZC-02 (via BBU-01) | 2 switches + 1 bridge | TBD | PA announcement sync |
| ZC-01 → ZC-03 (via BBU-01 + BBU-02) | 4 switches + 2 bridges | TBD | Must not delay smoke alarm |
| IBN-01 → IBN-02 (content sync) | Via BBU-01 | TBD | Background traffic, low priority |

## 5) Fault Containment

| Failure | CMS effect | Recovery |
|---------|-----------|---------|
| BBU-01 failure | SEG-01 and SEG-02 cannot exchange CMS status | ZC-01 operates in bay-autonomous mode; local PA/monitoring maintained |
| SW-01A failure | SW-01B maintains SEG-01 operation | No cabin system loss expected |
| SEG-02 switch pair loss | Bay 2 ZC unreachable from other bays | Bay 2 ZC operates standalone; crew alarm |

## 6) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Confirm N_bays from structural design | Systems | LC03 |
| Define BBU placement at each spar boundary | Avionics Installation | LC03 |
| Complete latency analysis | Systems Safety / Avionics | LC04 |
| Produce network_topology.graphml from design tool | Systems Integration | LC03 |

---

## Related Documents

- [ARCH_BWB_NETWORK_SEGMENTATION.md](../ATA44_BWB_ARCHITECTURE/ARCH_BWB_NETWORK_SEGMENTATION.md)
- [MODELS/network_topology.graphml](../ATA44_BWB_ARCHITECTURE/MODELS/network_topology.graphml)
- [ICD_BWB_NETWORK_ENDPOINTS_001.md](ICD_BWB_NETWORK_ENDPOINTS_001.md)
