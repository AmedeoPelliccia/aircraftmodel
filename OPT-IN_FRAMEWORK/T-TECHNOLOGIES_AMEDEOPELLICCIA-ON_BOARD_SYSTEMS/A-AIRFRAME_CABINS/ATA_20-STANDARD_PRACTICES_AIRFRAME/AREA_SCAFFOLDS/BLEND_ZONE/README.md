# AREA_SCAFFOLDS — BLEND_ZONE

**SNS context:** ATA 53-50 (Fuselage — Blend Zone / Centrebody Local Structural Implementation)
**Boundary:** BWB variant only
**Parent:** [ATA 20 README](../../README.md)

---

## Scope

Local area scaffold for the **fuselage-to-wing blend zone** on the BWB variant of the AMPEL360 Q100.

The blend zone is the structural transition region between the centrebody fuselage and the outboard wing torque box. It is governed by ATA 53 (Fuselage) at the local structural implementation level, with standard practices inherited from ATA 20 / ATA 51 (umbrella layer).

**SNS routing:**
- ATA 20 — umbrella / routing / shared-practice governance
- ATA 51 — structural standard practices (materials, fasteners, surface treatments, repair)
- ATA 53 — blend-zone / centrebody local structural implementation (this scaffold)
- ATA 57 — winglet / wing-tip local structural implementation (see `../WINGLETS/`)

**Subject assignments:**
- Subject 60 — Inspection and NDT
- Subject 70 — Repair and bonding integrity
- Subject 80 — Electrical bonding / lightning continuity (reserved; not CSDB mapping)

---

## Files in this scaffold

| File | SNS | Content |
|------|-----|---------|
| `ATA_53-50-00_APPLICABILITY.yaml` | 53-50-00 | Product conditions and variant applicability for blend-zone local structures |
| `ATA_53-50-00_TRACEABILITY.yaml` | 53-50-00 | Requirement-to-document traceability for this scaffold |
| `ATA_53-50-60_INSPECTION_NDT_TASKS.md` | 53-50-60 | Blend-zone-specific inspection tasks and NDT invocation rules |
| `ATA_53-50-70_REPAIR_BONDING_INTEGRITY.md` | 53-50-70 | Blend-zone-specific bonding integrity requirements (overlay on ATA 51-70-70) |
| `ATA_53-50-80_ELECTRICAL_BONDING_LIGHTNING_CONTINUITY.md` | 53-50-80 | Electrical bonding and lightning continuity requirements for this area |
| `CSDB_S1000D_MAP.yaml` | (admin) | Publication mapping administrative file (non-SNS; see file for attributes) |

---

## Cross-references

- ATA 51-70-60: [../../ATA_51-70-60_INSPECTION_NDT.md](../../ATA_51-70-60_INSPECTION_NDT.md)
- ATA 51-70-70: [../../ATA_51-70-70_REPAIR_BONDING_INTEGRITY.md](../../ATA_51-70-70_REPAIR_BONDING_INTEGRITY.md)
- WINGLETS scaffold: [../WINGLETS/README.md](../WINGLETS/README.md)
