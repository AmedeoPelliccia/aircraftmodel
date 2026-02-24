# ICD-BWB-44-001 — BWB Zone Controller Placement Envelope

**Doc ID:** T-A-ATA44-BWB-ICD-001
**Delta Ref:** DELTA-BWB-44-001
**ATA Subchapter:** 44-10 Cabin Core System
**Status:** DRAFT (LC01 — position data at LC03)
**Parent:** [Interfaces README](README.md)

---

## 1) Purpose

Defines the structural and spatial envelope constraints for Zone Controller (ZC) LRU
installation in each spar bay of the AMPEL360 BWB cabin.

## 2) BWB ZC Placement Constraint Table

> Δ BWB: One ZC redundant pair per spar bay replaces the WTW single CMC/CAC pair.

| Bay | ZC ID | Nominal FS | Nominal BL | Nominal WL | Volume envelope (mm³) | Access panel | Notes |
|-----|-------|-----------|-----------|-----------|----------------------|-------------|-------|
| Bay 1 | ZC-01 | TBD | TBD | TBD | TBD × TBD × TBD | TBD | FWD bay; near crew station |
| Bay 2 | ZC-02 | TBD | TBD | TBD | TBD × TBD × TBD | TBD | Mid bay |
| Bay 3 | ZC-03 | TBD | TBD | TBD | TBD × TBD × TBD | TBD | AFT bay |

## 3) Installation Constraints

| Parameter | Constraint | Standard / Notes |
|-----------|-----------|-----------------|
| ARINC 600 tray | Size TBD (confirmed at LC03) | ARINC 404A |
| Connector orientation | TBD from access panel direction | — |
| Vibration isolation | 6 dB attenuation min at ≥50 Hz | ED-14G Section 8 |
| Temperature environment | −55°C to +85°C; derating per airflow TBD | ED-14G Section 4 |
| Electrical bonding | ≤2.5 mΩ to airframe ground point | ATA 20 / ATA 24 |
| Bay wall penetration (BBU cable) | Grommet/doubler per ATA 53 interface | ICD-BWB-44-004 |

## 4) Coordinate Reference

- All FS/BL/WL values per BWB Design Reference Datum (TBD, LC03).
- Structural interference check against spar bay web geometry: LC04.

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Confirm ZC LRU form factor from supplier | Avionics Engineering | LC03 |
| Locate ZC position from 3D zone model | Avionics Installation | LC03 |
| Structural clearance check at bay wall | Structures | LC04 |

---

## Related Documents

- [ARCH_BWB_TOPOLOGY_OVERVIEW.md](../ATA44_BWB_ARCHITECTURE/ARCH_BWB_TOPOLOGY_OVERVIEW.md)
- [MODELS/node_placement.yaml](../ATA44_BWB_ARCHITECTURE/MODELS/node_placement.yaml)
- [ATA 24 (Electrical Power) interface data](TBD)
