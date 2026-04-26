# ATA 44 BWB — Architecture

**Doc ID family:** T-A-ATA44-BWB-ARCH-###
**Lifecycle:** LC01 (scaffold — topology data at LC03)
**Parent:** [BWB README](../README.md)

---

## Scope

BWB-specific cabin systems architecture artefacts: distributed topology overview,
zonal distribution, network segmentation, and machine-readable models.

The BWB Cabin Management System uses a **distributed per-bay Zone Controller (ZC)**
architecture driven by the composite wide-body planform. Spar bay structural boundaries
partition the cabin into independently controlled zones connected via inter-bay bridges.

---

## Files

| File | Description | Status |
|------|-------------|--------|
| `ARCH_BWB_TOPOLOGY_OVERVIEW.md` | CMS architecture narrative — distributed ZC topology | DRAFT |
| `ARCH_BWB_ZONAL_DISTRIBUTION.md` | Zone definition, bay-to-zone mapping, ZC assignment | DRAFT |
| `ARCH_BWB_NETWORK_SEGMENTATION.md` | Per-bay AFDX segments, inter-bay bridge switch topology | DRAFT |
| `MODELS/zone_map.yaml` | Machine-readable zone map (zone ID, bay ID, spar bay boundaries) | DRAFT |
| `MODELS/node_placement.yaml` | ZC and IFE node placement register | DRAFT |
| `MODELS/endpoint_map.yaml` | ARINC 664 endpoint register (VL/port per bay segment) | DRAFT |
| `MODELS/network_topology.graphml` | Network topology graph (per-bay AFDX + bridges) | DRAFT |

---

## Related Documents

- [ATA44_BWB_INDEX.yaml](../ATA44_BWB_INDEX.yaml)
- [ICD_BWB_NETWORK_SEGMENTATION_001.md](../ATA44_BWB_INTERFACES/ICD_BWB_NETWORK_SEGMENTATION_001.md)
- [WTW parallel architecture](../../WTW/ATA44_WTW_ARCHITECTURE/README.md)
