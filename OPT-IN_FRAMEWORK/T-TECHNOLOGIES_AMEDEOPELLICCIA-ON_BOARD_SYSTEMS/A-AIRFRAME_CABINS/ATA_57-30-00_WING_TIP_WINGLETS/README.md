# ATA 57-30-00 — Wing-Tip / Winglets

**SNS:** ATA 57-30-00 (Wings — Wing-Tip / Winglets Local Structural Implementation)
**Domain:** T-TECHNOLOGIES / A-AIRFRAME_CABINS
**Boundary:** WTW and BWB variants
**Doc ID:** T-A-ATA57-30-00-001
**Lifecycle:** LC01–LC13

---

## Scope

ATA 57 owns the **wings** chapter. This directory is the ATA 57-30 scaffold for the
**winglet / wing-tip region** — the outboard wing-like structural region on both WTW and BWB
variants of the AMPEL360 Q100.

For the BWB variant, winglets are treated using neutral structural primitives (`region: outboard`)
with rib/stringer semantics where applicable. For the WTW variant, winglets are the conventional
outboard extension of the circular-section wing box.

Standard practices are inherited from **ATA 51** (`ATA_51-00-00_STANDARD_PRACTICES_STRUCTURES_GENERAL/`).
This directory adds only the **local structural implementation overlay** — area-specific
inspection tasks, repair bonding requirements, and electrical bonding/lightning continuity rules.

**SNS routing principle:**
- ATA 20 — umbrella governance (no technical files)
- ATA 51 — shared standard practices (materials, repair, NDT, bonding integrity baseline)
- ATA 53-50 — blend zone local structural implementation (see `../ATA_53-50-00_BLEND_ZONE_CENTREBODY_INTERFACE/`)
- **ATA 57-30** — winglet local structural implementation (this directory)

**Subject assignments (this directory only):**
| Subject | SNS | File |
|---------|-----|------|
| Applicability | 57-30-00 | `ATA_57-30-00_APPLICABILITY.yaml` |
| Traceability | 57-30-00 | `ATA_57-30-00_TRACEABILITY.yaml` |
| Inspection and NDT | 57-30-60 | `ATA_57-30-60_INSPECTION_NDT_TASKS.md` |
| Repair and bonding integrity | 57-30-70 | `ATA_57-30-70_REPAIR_BONDING_INTEGRITY.md` |
| Electrical bonding / lightning continuity | 57-30-80 | `ATA_57-30-80_ELECTRICAL_BONDING_LIGHTNING_CONTINUITY.md` |
| CSDB/S1000D publication mapping (admin) | non-SNS | `CSDB_S1000D_MAP.yaml` |

> **SNS reservation — Subject 80:** Reserved exclusively for Electrical Bonding / Lightning
> Continuity. `CSDB_S1000D_MAP.yaml` is an administrative file with `not_ata_subject: true`
> and shall not be assigned SNS 57-30-80.

---

## Cross-references

- ATA 20 governance: [../ATA_20-00-00_STANDARD_PRACTICES_AIRFRAME_SHARED/README.md](../ATA_20-00-00_STANDARD_PRACTICES_AIRFRAME_SHARED/README.md)
- ATA 51 baseline: [../ATA_51-00-00_STANDARD_PRACTICES_STRUCTURES_GENERAL/README.md](../ATA_51-00-00_STANDARD_PRACTICES_STRUCTURES_GENERAL/README.md)
- ATA 53 blend zone: [../ATA_53-50-00_BLEND_ZONE_CENTREBODY_INTERFACE/README.md](../ATA_53-50-00_BLEND_ZONE_CENTREBODY_INTERFACE/README.md)
