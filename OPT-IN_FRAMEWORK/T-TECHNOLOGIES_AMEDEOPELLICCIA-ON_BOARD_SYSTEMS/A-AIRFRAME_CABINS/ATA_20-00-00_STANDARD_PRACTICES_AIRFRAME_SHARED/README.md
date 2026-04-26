# ATA 20-00-00 — Standard Practices – Airframe (Shared Governance)

**SNS:** ATA 20-00-00 (Standard Practices — Airframe)
**Domain:** T-TECHNOLOGIES / A-AIRFRAME_CABINS
**Boundary:** SHARED (umbrella governance, WTW and BWB)
**Doc ID:** T-A-ATA20-00-00-001
**Lifecycle:** LC01–LC13

---

## Scope

ATA 20 is the **umbrella, routing, and shared-practice governance** layer for airframe standard
practices on the AMPEL360 Q100. It does **not** own technical content for ATA 51/53/57 —
those chapters own their own file trees.

**Containment rule (normative):**
> No file inside `ATA_20-00-00_STANDARD_PRACTICES_AIRFRAME_SHARED/` shall carry
> `ata_chapter` ∈ {`"51"`, `"53"`, `"57"`}. Cross-references are permitted; cross-containment is not.

---

## 1) Normative precedence hierarchy

| Level | Document | Governs |
|-------|----------|---------|
| 1 | Type certification basis / CS-25 / Special Conditions | Airworthiness |
| 2 | AMPEL360 Q100 Structural Repair Manual (SRM) | Approved repair data |
| 3 | ATA 51-00-00 Standard Practices and Structures – General | Common methods, materials, workmanship |
| 4 | Component / vendor CMM and process specs (when invoked) | Part-level |
| 5 | Local MRO work instructions | Shall not relax levels above |

---

## 2) ATA chapter ownership map

| Chapter | Owns | Path |
|---------|------|------|
| ATA 20 | Umbrella governance, routing, shared-practice policy | `ATA_20-00-00_STANDARD_PRACTICES_AIRFRAME_SHARED/` (this directory) |
| ATA 51 | Standard Practices and Structures – General: materials, fasteners, surface treatments, repair, NDT, bonding integrity | `ATA_51-00-00_STANDARD_PRACTICES_STRUCTURES_GENERAL/` |
| ATA 53 | Fuselage — blend zone / centrebody local structural implementation | `ATA_53-50-00_BLEND_ZONE_CENTREBODY_INTERFACE/` |
| ATA 57 | Wings — winglet / wing-tip local structural implementation | `ATA_57-30-00_WING_TIP_WINGLETS/` |

---

## 3) Applicability model (WTW vs BWB)

Standard practices are **common** unless the owning chapter document explicitly declares:

- **WTW-only** — applies to conventional fuselage / circular-section wing box
- **BWB-only** — applies to blended wing body / distributed spar-bay planform
- **BOTH** (default)

Applicability is tagged at section level in each owning chapter document.

---

## 4) Cross-references (read-only from ATA 20)

These are **reference links only**. ATA 20 does not contain these files.

- **ATA 51 baseline:** [../ATA_51-00-00_STANDARD_PRACTICES_STRUCTURES_GENERAL/README.md](../ATA_51-00-00_STANDARD_PRACTICES_STRUCTURES_GENERAL/README.md)
- **ATA 53 blend zone:** [../ATA_53-50-00_BLEND_ZONE_CENTREBODY_INTERFACE/README.md](../ATA_53-50-00_BLEND_ZONE_CENTREBODY_INTERFACE/README.md)
- **ATA 57 winglets:** [../ATA_57-30-00_WING_TIP_WINGLETS/README.md](../ATA_57-30-00_WING_TIP_WINGLETS/README.md)

---

## 5) Traceability

See [ATA_20-00-00_TRACEABILITY.yaml](ATA_20-00-00_TRACEABILITY.yaml) for chapter-level
requirement traceability to ATA 51/53/57 owning documents.

---

## 6) Change control

Changes to this governance layer require a Change Request logged at LC01.
See `ATA_20-00-00_TRACEABILITY.yaml` for current open items.
