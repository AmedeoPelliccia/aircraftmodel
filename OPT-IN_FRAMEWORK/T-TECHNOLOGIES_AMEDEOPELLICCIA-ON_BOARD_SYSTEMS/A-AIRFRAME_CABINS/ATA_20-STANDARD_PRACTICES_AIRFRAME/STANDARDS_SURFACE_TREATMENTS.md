# ATA 20 — Surface Treatments, Corrosion Prevention, and Sealing

**Doc ID:** T-A-ATA20-SURF-001
**Lifecycle:** LC03 (planned increment)
**Parent:** [ATA 20 README](README.md)

---

## 1) Scope

Defines surface treatment selection, corrosion prevention practices, and sealant application rules for airframe maintenance and repair on the **AMPEL360 Q100** platform (both WTW and BWB variants).

> **Note:** This file is a planned increment under LC03. Governing rules are summarised in `README.md` §5. Specific approved products and process specs will be populated during detailed engineering.

---

## 2) Surface Treatment Families

### 2.1 Conversion Coatings (Chemical Film)

| Specification | Application | Notes |
|--------------|-------------|-------|
| Alodine / Iridite (MIL-DTL-5541) | Aluminium alloys | Electrical continuity maintained; primer required over for structural |
| Anodize (MIL-A-8625 Type II / III) | Aluminium, wear surfaces | Hard anodize (Type III) for wear; do not prime over hard anodize unless drawing specified |

**Rules (shall):**
- Apply chemical film within 4 hours of surface preparation (abrading/cleaning).
- Inspect for complete coverage — no bare aluminium spots.
- Seal with approved sealant in faying surface zones even after conversion coating.

### 2.2 Primers

| Type | Specification | Application |
|------|--------------|-------------|
| Epoxy primer (chromated) | MIL-PRF-23377 / equivalent | Metallic substrates; corrosion-inhibiting |
| Epoxy primer (chrome-free) | MIL-PRF-85582 | Where chromate-free required (environmental) |
| Composite primer | Per material process spec | CFRP/GFRP; verify compatibility with resin system |

**Rules (shall):**
- Apply over clean, dry, freshly converted surface.
- Allow primer to cure to tack-free before topcoat (time/temperature per product data sheet).
- Repair primer thin-spots before topcoat — minimum dry film thickness per drawing.

### 2.3 Topcoats

| Type | Application | Finish |
|------|-------------|--------|
| Polyurethane topcoat (gloss) | Exterior aerodynamic surfaces | Smooth/gloss per profile tolerance |
| Polyurethane topcoat (semi-gloss) | Interior structure (visible zones) | Semi-gloss per drawing |
| Skydrol-resistant topcoat | Hydraulic bays, wheel wells | Required in fluid-exposed zones |

**Rules (shall):**
- Topcoat within recoat window of primer (see product data sheet).
- Sand/feather edges of old paint before spot repair; maximum step height ≤0.13 mm (0.005 in) after blend.

### 2.4 Sealants

| Class | Use | Cure Type |
|-------|-----|-----------|
| Faying surface sealant (Class A) | Applied wet before assembly (wet installation) | Anaerobic/polysulfide; apply within pot life |
| Fillet/faying seal (Class B) | Applied over assembled joint as fillet | Polysulfide/polythioether |
| Injection sealant | Inaccessible faying zones (post-assembly injection) | Low-viscosity polysulfide |
| Quick-repair compound | Temporary environmental seal only | See approved products list |

**Rules (shall):**
- Use sealant within its pot life; discard and replace if shelf-life expired.
- Verify surface cleanliness before sealant application; sealant over oil/contamination is **not acceptable**.
- Maintain sealant bead profile per drawing (fillet radius, coverage width).

---

## 3) Corrosion Control (CPCP-Aligned)

### 3.1 Corrosion Classification

| Class | Description | Action |
|-------|-------------|--------|
| Light surface corrosion (Class 1) | Oxide/staining only; no measurable material loss | Clean, treat, re-protect |
| Moderate corrosion (Class 2) | Pitting or material loss within SRM allowable | Remove, treat, re-protect; document depth |
| Severe corrosion (Class 3) | Material loss beyond allowable | Engineering disposition required |

### 3.2 Corrosion Removal Sequence

1. **Clean**: Remove paint, sealant, and contamination in affected area.
2. **Remove corrosion**: Abrade/blend to bright metal using approved abrasive.
   - Do not exceed SRM blend limits (depth/area).
3. **Neutralise**: Apply approved corrosion neutraliser if required by SRM.
4. **Measure**: Record depth and area; compare to SRM allowable.
5. **Re-protect**: Conversion coat → primer → topcoat per §2 above.
6. **Re-seal**: Restore faying surface seals and fillets removed during access.

### 3.3 Drain and Vent Paths

- **Shall** be confirmed open after any repair in lower lobe/bilge zones.
- Do not allow sealant to block drain holes (verify with probe/light after application).

---

## 4) Applicability (WTW vs BWB)

| Section | WTW | BWB |
|---------|-----|-----|
| Metallic surface treatments | Full applicability | Full applicability |
| Composite-compatible primers | Selective (wing/nacelle areas) | Primary applicability (large composite skins) |
| Corrosion control (CPCP) | Standard CPCP zones | Modified zones due to large composite primary structure |

---

## Related Documents

- [ATA 20 README](README.md)
- [STANDARDS_MATERIALS.md](STANDARDS_MATERIALS.md)
- [REPAIR_ACCEPTABILITY.md](REPAIR_ACCEPTABILITY.md)
- [ATA 51 — Structures General](../ATA_51-STRUCTURES_GENERAL/README.md)
