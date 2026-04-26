# ATA 44 WTW — Architecture

**Doc ID family:** T-A-ATA44-WTW-ARCH-###
**Lifecycle:** LC01 (scaffold — topology data at LC03)
**Parent:** [WTW README](../README.md)

---

## Scope

WTW-specific cabin systems architecture artefacts: topology overview, zone definition,
and machine-readable models (zone map, network topology, ICD endpoints).

The WTW Cabin Management System (CMS) uses a conventional longitudinal zone architecture
on a circular-fuselage platform. This folder captures the WTW variant deltas versus any
shared architecture baseline in the ATA 44 root.

---

## Files

| File | Description | Status |
|------|-------------|--------|
| `ARCH_WTW_TOPOLOGY_OVERVIEW.md` | CMS architecture narrative + block diagram description | DRAFT |
| `ARCH_WTW_ZONE_DEFINITION.md` | Zone boundary definitions and zone-to-LRU assignment | DRAFT |
| `MODELS/zone_map.yaml` | Machine-readable zone map (zone ID, BL/FS boundaries) | DRAFT |
| `MODELS/network_topology.graphml` | Network topology graph (stub) | DRAFT |
| `MODELS/icd_endpoints.yaml` | ICD endpoint register (ARINC 664 label/port allocation) | DRAFT |

---

## Related Documents

- [ATA44_WTW_INDEX.yaml](../ATA44_WTW_INDEX.yaml)
- [ICD_WTW_NETWORK_ENDPOINTS_001.md](../ATA44_WTW_INTERFACES/ICD_WTW_NETWORK_ENDPOINTS_001.md)
