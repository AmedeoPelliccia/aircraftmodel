# ICD-BWB-44-005 — BWB Distributed IFE Bay Node Placement

**Doc ID:** T-A-ATA44-BWB-ICD-005
**Delta Ref:** DELTA-BWB-44-006
**ATA Subchapter:** 44-20 In-Flight Entertainment
**Status:** DRAFT (LC01 — IBN position data at LC03)
**Parent:** [Interfaces README](README.md)

---

## 1) Purpose

Defines the placement envelope for per-bay IFE Bay Nodes (IBN) in the AMPEL360 BWB.
IBNs replace the single IFE server used in the WTW variant.

> Δ BWB: No single IFE server bay. Each spar bay has an independent IBN to avoid
> high-bandwidth IFE content streaming across the inter-bay bridge (BBU).

---

## 2) IBN Placement Constraints

| Bay | IBN ID | Nominal FS | Nominal BL | Nominal WL | Volume (mm³) | Access panel | Notes |
|-----|--------|-----------|-----------|-----------|-------------|-------------|-------|
| Bay 1 | IBN-01 | TBD | TBD | TBD | TBD | TBD | FWD bay |
| Bay 2 | IBN-02 | TBD | TBD | TBD | TBD | TBD | Mid bay |
| Bay 3 | IBN-03 | TBD | TBD | TBD | TBD | TBD | AFT bay |

---

## 3) Physical Constraints

| Parameter | Requirement | Notes |
|-----------|------------|-------|
| Flammability | FAR/CS-25.853 compliant | All IBN LRU materials |
| Mounting | ARINC 404A tray (size TBD) | Confirm at LC03 |
| Cooling | Forced-air or conduction (TBD per bay) | From thermal model LC04 |
| EMI | ED-14G Section 21 (EMI emissions) | Per bay environment |
| Pax network I/F | 802.11ax cabin Wi-Fi access per bay | ICD with ATA 46 TBD |
| Inter-bay sync | Low-bandwidth synchronisation link via BBU | Not high-bandwidth — content pre-loaded per bay |

---

## 4) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Select IBN LRU and confirm form factor | IFE Engineering | LC03 |
| Locate IBN in each bay from 3D model | Avionics Installation | LC03 |
| Confirm thermal load per bay | Systems / Thermal | LC04 |

---

## Related Documents

- [MODELS/node_placement.yaml](../ATA44_BWB_ARCHITECTURE/MODELS/node_placement.yaml)
- [ATA 25 BWB overlay — seat/IFE interface](../../../ATA_25-EQUIPMENT_FURNISHINGS/PROGRAMME_EXT/BWB/README.md)
