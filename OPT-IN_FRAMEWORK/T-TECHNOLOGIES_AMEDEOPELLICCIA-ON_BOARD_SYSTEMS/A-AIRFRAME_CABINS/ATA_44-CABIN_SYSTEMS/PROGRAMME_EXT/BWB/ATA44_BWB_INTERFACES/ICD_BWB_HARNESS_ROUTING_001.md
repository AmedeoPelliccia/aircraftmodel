# ICD-BWB-44-004 — BWB Inter-Bay Harness Routing Envelope (Spar Bay Penetrations)

**Doc ID:** T-A-ATA44-BWB-ICD-004
**Delta Ref:** DELTA-BWB-44-004
**ATA Subchapter:** 44-10 Cabin Core System
**Status:** DRAFT (LC01 — routing data at LC03)
**Parent:** [Interfaces README](README.md)

---

## 1) Purpose

Defines the approved routing envelope and structural penetration constraints for
ATA 44 CMS harnesses crossing spar bay structural boundaries in the AMPEL360 BWB.

> Δ BWB vs WTW: WTW uses a single longitudinal harness run with no structural interruptions.
> BWB harness MUST cross spar bay structural walls via dedicated doubler/grommet
> installations defined in co-ordination with ATA 53 (Structures).

---

## 2) Penetration Requirements

| Parameter | Value | Standard / Notes |
|-----------|-------|-----------------|
| Penetration type | Firewall grommet or composite doubler with edged hole | ATA 53 repair manual |
| Bundle diameter limit (per penetration) | TBD mm | From ATA 53 hole rework table — LC03 |
| Min clearance (harness to structure) | 10 mm nominal (TBD from ATA 20) | ATA 20 standard practices |
| Backshell / strain relief | Mandatory within 50 mm of grommet on each side | ATA 20 |
| Segregation (power vs signal) | ≥25 mm separation at penetration | ED-14G / CS-25.1353 |
| Fire containment | Harness seal compound per ATA 26 if FW boundary | TBD — fire boundary definition LC03 |

---

## 3) Penetration Register (placeholder — from 3D model at LC03)

| Penetration ID | Bay boundary | FS | BL | Hole diameter (mm) | Bundle contents | Structural reference |
|---------------|-------------|----|----|-------------------|----------------|---------------------|
| PEN-BAY12-001 | Bay 1 / Bay 2 | TBD | TBD | TBD | ZC/BBU data harness | ATA 53 / LC03 |
| PEN-BAY23-001 | Bay 2 / Bay 3 | TBD | TBD | TBD | ZC/BBU data harness | ATA 53 / LC03 |
| PEN-BAY12-002 | Bay 1 / Bay 2 | TBD | TBD | TBD | PA audio bus extension | ATA 53 / LC03 |
| PEN-BAY23-002 | Bay 2 / Bay 3 | TBD | TBD | TBD | PA audio bus extension | ATA 53 / LC03 |

---

## 4) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Define penetration locations from 3D model | Avionics Installation + Structures | LC03 |
| Confirm fire boundary classification of spar walls | Systems / Fire Protection | LC03 |
| Review harness seal compound applicability | ATA 26 / Structures | LC04 |

---

## Related Documents

- [ATA 20 Standard Practices](../../../../ATA_20-STANDARD_PRACTICES/README.md)
- [ATA 53 Structures ICD] (TBD, ATA 53)
