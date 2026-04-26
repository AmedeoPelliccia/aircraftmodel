# AREA_SCAFFOLDS — WINGLETS

**SNS context:** ATA 57-30 (Wings — Winglets / Wing-Tip Local Structural Implementation)
**Boundary:** BWB and WTW variants (outboard wing-like region)
**Parent:** [ATA 20 README](../../README.md)

---

## Scope

Local area scaffold for the **winglets / outboard wing-tip region** on AMPEL360 Q100 variants.

Winglets are treated as outboard wing-like structural regions using neutral structural primitives (members, bays) with `region: outboard` aliasing to permit rib/stringer semantics where applicable. The governing ATA chapter is ATA 57 (Wings) at the local sub-area level.

**SNS routing:**
- ATA 20 — umbrella / routing / shared-practice governance
- ATA 51 — structural standard practices (materials, fasteners, surface treatments, repair)
- ATA 57 — winglet / wing-tip local structural implementation (this scaffold)
- ATA 53 — blend-zone / centrebody (see `../BLEND_ZONE/`)

**Subject assignments:**
- Subject 60 — Inspection and NDT
- Subject 70 — Repair and bonding integrity
- Subject 80 — Electrical bonding / lightning continuity (reserved; not CSDB mapping)

---

## Files in this scaffold

| File | SNS | Content |
|------|-----|---------|
| `ATA_57-30-00_APPLICABILITY.yaml` | 57-30-00 | Product conditions and variant applicability for winglet local structures |
| `ATA_57-30-00_TRACEABILITY.yaml` | 57-30-00 | Requirement-to-document traceability for this scaffold |
| `ATA_57-30-60_INSPECTION_NDT_TASKS.md` | 57-30-60 | Winglet-specific inspection tasks and NDT invocation rules |
| `ATA_57-30-70_REPAIR_BONDING_INTEGRITY.md` | 57-30-70 | Winglet-specific bonding integrity requirements (overlay on ATA 51-70-70) |
| `ATA_57-30-80_ELECTRICAL_BONDING_LIGHTNING_CONTINUITY.md` | 57-30-80 | Electrical bonding and lightning continuity requirements for winglets |
| `CSDB_S1000D_MAP.yaml` | (admin) | Publication mapping administrative file (non-SNS; see file for attributes) |

---

## Cross-references

- ATA 51-70-60: [../../ATA_51-70-60_INSPECTION_NDT.md](../../ATA_51-70-60_INSPECTION_NDT.md)
- ATA 51-70-70: [../../ATA_51-70-70_REPAIR_BONDING_INTEGRITY.md](../../ATA_51-70-70_REPAIR_BONDING_INTEGRITY.md)
- BLEND_ZONE scaffold: [../BLEND_ZONE/README.md](../BLEND_ZONE/README.md)
