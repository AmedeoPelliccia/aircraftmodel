# ATA 57-30-80 — Winglets Electrical Bonding and Lightning Continuity

**SNS:** ATA 57-30-80 (Wings — Winglets — Electrical Bonding / Lightning Continuity)
**Doc ID:** T-A-ATA57-30-80-001
**Lifecycle:** LC04 (planned increment)
**Applicability:** WTW and BWB variants
**Parent:** [WINGLETS README](README.md)

> **SNS reservation note:** Subject 80 at ATA 57-30 is reserved exclusively for Electrical Bonding / Lightning Continuity. CSDB/S1000D publication mapping artefacts shall not be assigned to this subject. See `CSDB_S1000D_MAP.yaml` (administrative file, `not_ata_subject: true`).

---

## 1) Scope

Defines electrical bonding and lightning continuity requirements specific to the winglet / wing-tip region on AMPEL360 Q100 (WTW and BWB variants).

Winglets are a primary attachment point zone for lightning strikes (Zone 1A). Ensuring the lightning protection mesh and all structural bonding paths are intact is safety-critical.

---

## 2) Bonding Requirements

| Requirement ID | Location | Bonding method | Resistance limit | Verification |
|---------------|----------|----------------|-----------------|--------------|
| WG-80-001 | Winglet tip lightning receptor | Direct connect to primary bonding network via tip receptor assembly | ≤ 1.0 mΩ receptor-to-main spar | DC resistance measurement |
| WG-80-002 | Composite winglet skin — lightning mesh continuity | Expanded copper mesh or conductive primer ply co-cured into skin | Continuity per approved acceptance standard | End-to-end resistance test per Bonding Continuity AMM task |
| WG-80-003 | Winglet attachment lug — structure-to-structure | Direct metal-to-metal contact at attachment interface; isolation liner removal where applicable | ≤ 2.5 mΩ structure-to-structure | Resistance measurement after installation |
| WG-80-004 | Post-repair bonding restoration | Any repair disturbing conductive mesh, bonding braid, or attachment contact shall restore electrical continuity | Per original limits | Post-repair bonding check per applicable SRM task |
| WG-80-005 | BWB: winglet-to-blend-zone boundary | Bonding continuity across the winglet inboard attachment boundary to blend-zone network | ≤ 2.5 mΩ across boundary | Combined measurement per AMM bonding continuity task |

---

## 3) Lightning Strike Zone

Winglets occupy Zone 1A (direct attachment, initial) per the AMPEL360 Q100 Lightning Protection Design Document. All bonding and mesh specifications shall satisfy Zone 1A requirements.

---

## Related Documents

- [ATA_57-30-70_REPAIR_BONDING_INTEGRITY.md](ATA_57-30-70_REPAIR_BONDING_INTEGRITY.md) — Repair bonding integrity (structural)
- [ATA_57-30-60_INSPECTION_NDT_TASKS.md](ATA_57-30-60_INSPECTION_NDT_TASKS.md) — NDT tasks
- [CSDB_S1000D_MAP.yaml](CSDB_S1000D_MAP.yaml) — Publication mapping (administrative file, non-SNS)
- [../BLEND_ZONE/ATA_53-50-80_ELECTRICAL_BONDING_LIGHTNING_CONTINUITY.md](../BLEND_ZONE/ATA_53-50-80_ELECTRICAL_BONDING_LIGHTNING_CONTINUITY.md) — Blend zone electrical bonding
