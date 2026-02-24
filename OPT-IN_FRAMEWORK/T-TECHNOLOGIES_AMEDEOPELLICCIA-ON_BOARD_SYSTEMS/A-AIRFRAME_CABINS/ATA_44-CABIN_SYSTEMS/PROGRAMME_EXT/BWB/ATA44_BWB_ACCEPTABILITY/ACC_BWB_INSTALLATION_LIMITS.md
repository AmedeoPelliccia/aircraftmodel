# ACC-BWB-44-001 — BWB CMS LRU Installation Limits

**Doc ID:** T-A-ATA44-BWB-ACC-001
**Status:** DRAFT (LC01 — numeric limits at LC04)
**Parent:** [Acceptability README](README.md)

---

## Scope

Installation acceptance limits for ATA 44 CMS LRUs installed in BWB spar bays:
Zone Controllers (ZC), Bay Bridge Units (BBU), IFE Bay Nodes (IBN).
These are deltas to the ATA 44 SHARED baseline limits where the BWB bay environment
differs.

---

## LRU Torque and Fastener Limits

| LRU | Fastener | Torque (dry) | Torque (lubricated) | Standard |
|-----|---------|-------------|--------------------|---------| 
| Zone Controller (ZC) | M5 tray-mount | TBD N·m [LC04] | TBD N·m | ATA 20 / ARINC 404A |
| Bay Bridge Unit (BBU) | M4 structural bracket | TBD N·m [LC04] | TBD N·m | ATA 20 |
| IFE Bay Node (IBN) | M5 tray-mount | TBD N·m [LC04] | TBD N·m | ARINC 404A |

---

## Clearance Requirements

| Parameter | Min | Notes |
|-----------|-----|-------|
| ZC to adjacent structure | 10 mm | From ATA 20 standard practices |
| BBU to spar bay wall surface | 5 mm | Access for inspection tool |
| IBN to furnishing/monument | 25 mm | Ventilation clearance |
| Harness bend radius (CMS data cable) | ≥10× cable OD | ATA 20 |
| Harness to spar web clearance | ≥10 mm | ATA 20 |

---

## Bonding Limits (per ZC / BBU / IBN)

| LRU | Max bond resistance | Test point | Standard |
|-----|-------------------|-----------|---------|
| ZC pair (per bay) | ≤2.5 mΩ | ZC chassis to bay structure point | ATA 20 / ATA 24 |
| BBU | ≤2.5 mΩ | BBU chassis to spar boundary structure | ATA 20 |
| IBN | ≤5.0 mΩ | IBN chassis to local structure | ATA 20 |

---

## Delta Notes

> Δ BWB vs WTW:
> - WTW has a single CMC/CAC in the FWD E/E bay; bonding test is straightforward.
> - BWB requires per-bay bonding verification at each ZC and BBU installation site.
> - Bay environments may differ in vibration and temperature — per-bay qualification applies.

---

## Related Documents

- [ATA 20 Standard Practices](../../../../ATA_20-STANDARD_PRACTICES/README.md)
- [ICD_BWB_CONTROLLER_PLACEMENT_001.md](../ATA44_BWB_INTERFACES/ICD_BWB_CONTROLLER_PLACEMENT_001.md)
