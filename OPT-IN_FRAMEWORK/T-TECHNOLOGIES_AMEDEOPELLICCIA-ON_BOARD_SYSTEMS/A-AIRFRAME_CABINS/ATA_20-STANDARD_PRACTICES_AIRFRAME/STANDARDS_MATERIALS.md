# ATA 20 — Approved Material Families, Handling, and Compatibility Rules

**Doc ID:** T-A-ATA20-MAT-001
**Lifecycle:** LC03 (planned increment)
**Parent:** [ATA 20 README](README.md)

---

## 1) Scope

This document defines the approved material families, handling requirements, and galvanic/chemical compatibility rules for airframe maintenance and repair on the **AMPEL360 Q100** platform (both WTW and BWB variants).

> **Note:** This file is a planned increment under LC03. The governing rules are summarised in `README.md` §3. Full material tables will be populated during detailed engineering.

---

## 2) Metallic Material Families

### 2.1 Aluminium Alloys (2xxx / 7xxx)

| Alloy Family | Typical Application | Corrosion Class | Notes |
|-------------|---------------------|----------------|-------|
| 2024-T3 | Skin, lower wing | High susceptibility | Clad preferred; isolate from steel |
| 7075-T6 | Upper wing, spar caps | High susceptibility | Avoid contact with carbon fibre without barrier |
| 7050-T7451 | Thick plate machined parts | Moderate | Stress-corrosion resistant temper |
| 6061-T6 | Secondary structure, brackets | Low | General purpose |

**Handling rules (shall):**
- Store in dry, low-humidity environment (<60% RH).
- Protect bare surfaces with approved temporary protective coating during fabrication.
- Prevent contact with mercury compounds, paints containing mercury, or wet concrete.

### 2.2 Titanium Alloys

| Alloy | Application | Constraint |
|-------|-------------|-----------|
| Ti-6Al-4V | Fasteners, fittings, brackets | Avoid cadmium-plated steel contact |
| Ti-3Al-2.5V | Hydraulic tubing | Use approved cutting fluids only |

**Handling rules (shall):**
- Prevent galling on mating titanium surfaces — use anti-seize compound per approved spec.
- Do not use chlorinated cutting fluids; use approved titanium-compatible coolants.

### 2.3 Steels (including Stainless)

| Grade | Application | Treatment Required |
|-------|-------------|-------------------|
| 4130/4340 | High-stress fittings | Cadmium plate or equivalent |
| 300-series SS | Fasteners, brackets in wet zones | Passivate per ASTM A967 or equivalent |
| 17-4 PH | Hi-strength attachments | H900/H1025 condition only |

**Handling rules (shall):**
- Passivate stainless parts after machining before assembly.
- Isolate carbon steel from aluminium with approved primer or insulating shim.

---

## 3) Composite Material Families

### 3.1 Carbon Fibre Reinforced Polymer (CFRP)

| Form | Application | Repair Note |
|------|-------------|-------------|
| Woven fabric prepreg | Secondary structure, fairings | Scarf repair preferred |
| Unidirectional tape | Primary structure (BWB skins, WTW ribs) | Ply-by-ply restoration, strict orientation |
| Wet layup | Field repairs only (non-structural) | Environment control mandatory |

**Workmanship (shall):**
- Abrade → vacuum → solvent wipe (approved solvent) sequence before bonding.
- Contamination limit: no visible oil/water on bond surface.
- Cure per approved cycle (time/temperature/pressure/vacuum).

### 3.2 Glass Fibre Reinforced Polymer (GFRP)

Used for radomes, antenna fairings, and non-structural panels.

- Lightning strike protection mesh continuity **shall** be verified after any repair.

### 3.3 Core Materials

| Type | Application | Splice/Repair Rule |
|------|-------------|-------------------|
| Aluminium honeycomb | Sandwich floors, panels | Potting required at edges/inserts |
| Nomex honeycomb | Composite sandwich panels | Core density match required |
| Rohacell / PMI foam | Monolithic core repairs | Density and cell match per SRM |

---

## 4) Galvanic Compatibility Table (minimum)

| Material A | Material B | Isolation Required? | Method |
|-----------|-----------|---------------------|--------|
| Carbon fibre composite | Aluminium alloy | **YES** | Approved primer + sealant barrier |
| Carbon fibre composite | Steel | **YES** | Approved primer + sealant barrier |
| Aluminium | Steel | **YES** | Primer/sealant or insulating shim |
| Titanium | Aluminium | No (compatible) | N/A |
| Titanium | CFRP | Verify per SRM | Check current SRM table |
| Aluminium | Aluminium (same alloy) | No | N/A |

---

## 5) Chemical Compatibility

- Approved cleaning agents: see current approved materials list in CMM/SRM.
- Do not use MEK (methyl ethyl ketone) on polycarbonate windows or acrylic transparencies.
- Hydraulic fluids (Skydrol/equivalent): incompatible with most paint systems unless topcoat is Skydrol-resistant.

---

## Related Documents

- [ATA 20 README](README.md)
- [STANDARDS_SURFACE_TREATMENTS.md](STANDARDS_SURFACE_TREATMENTS.md)
- [ATA 51 — Structures General](../ATA_51-STRUCTURES_GENERAL/README.md)
