# ATA 20 — Standard Practices – Airframe

**Domain:** T-TECHNOLOGIES / A-AIRFRAME_CABINS
**Boundary:** SHARED
**Doc ID:** T-A-ATA20-001
**Lifecycle:** Standard (LC01–LC13)

---

## Scope

Defines standard airframe maintenance and repair practices for the **AMPEL360 Q100** platform, covering **material standards**, **fastener specifications**, **surface treatments**, and **repair acceptability criteria** applicable to both **WTW** and **BWB** variants.

This document is the **baseline practice layer** used by:

* Structural maintenance tasks (line/hangar), shop repairs, and rework
* Engineering dispositions (repair schemes, concessions)
* S1000D/CSDB procedural and descriptive content that references "standard practices"

---

## Architecture / Standards

### 1) Normative hierarchy

**Order of precedence (highest → lowest):**

1. **Type certification basis / Airworthiness** (e.g., CS-25/Part 25 + special conditions as applicable)
2. **AMPEL360 Q100 Structural Repair Manual (SRM)** and approved repair data
3. **This ATA 20 Standard Practices** (common methods, materials, workmanship criteria)
4. Component/part CMM / vendor process specs (when explicitly invoked)
5. Local MRO work instructions (shall not relax requirements above)

**Rule:** If a conflict exists, the higher-level document **shall govern**.

---

### 2) Applicability model (WTW vs BWB)

Standard practices are **common** unless a subsection explicitly declares one of:

* **WTW-only** (e.g., conventional fuselage skin/stringer access patterns)
* **BWB-only** (e.g., large-area composite skin repairs, distributed panels)
* **BOTH** (default)

**Rule:** Procedures **shall** tag applicability at section level to prevent ambiguity in CSDB outputs.

---

### 3) Material standards (minimum practice set)

#### 3.1 Metallic materials (typical airframe scope)

* **Aluminum alloys** (2xxx/7xxx families): handling, corrosion prevention, rework limits
* **Titanium alloys**: galling avoidance, cutting fluids, fastener pairing constraints
* **Steels** (incl. stainless): passivation and corrosion controls

**Workmanship rules (shall):**

* Prevent dissimilar-metal contact without approved isolation (primer/sealant/shim).
* Use only approved abrasives and cleaning agents compatible with the substrate.

#### 3.2 Composite materials (BWB emphasis, WTW selective use)

* CFRP/GFRP structures: scarf repairs, ply orientation control, cure control
* Core materials (honeycomb/foam): potting, core splice rules
* Lightning strike layers / conductive meshes (where applicable): continuity restoration requirements

**Workmanship rules (shall):**

* Control **surface preparation** (abrade → vacuum → solvent wipe) with contamination limits.
* Control **environment** for bonding/repairs (temperature/humidity per process spec).

---

### 4) Fasteners, holes, torque, and locking

#### 4.1 Fastener families

This practice set covers (when invoked by the SRM/task):

* Solid rivets, blind rivets
* Hi-Lok / lockbolt systems
* Bolts/screws/nuts/washers
* Inserts and captive fasteners
* Temporary fasteners (Clecos) for fit-up and drill match

**Selection rules (shall):**

* Use fasteners per drawing/SRM; substitutions require engineering approval.
* Maintain material compatibility (galvanic) and coating compatibility.

#### 4.2 Hole quality and rework

* Drill/ream practices shall meet hole quality limits for:

  * Diameter / roundness
  * Burr control
  * Surface finish
  * Edge distance and pitch (per SRM/design allowables)

**Rework rules (shall):**

* Hole upsizing shall follow an approved rework ladder.
* Cracks, elongation, or out-of-round beyond limits **shall** trigger engineering disposition.

#### 4.3 Torque and locking

* Torque application method shall be specified (dry / lubricated / wet-installed sealant).
* Locking methods (cotter pin, lockwire, self-locking nuts, thread-lock) shall be per spec.

**Rule:** Torque values are not universal; they **shall** be taken from the approved torque table for the exact fastener, lubrication state, and joint stack.

---

### 5) Surface treatments, corrosion prevention, sealing

#### 5.1 Surface treatment families

* Conversion coatings (chemical film)
* Anodizing (where applicable)
* Primers/topcoats
* Sealants for faying surfaces and wet-installation

**Rule:** Treatment selection shall be compatible with:

* Base material
* Bonding/adhesion requirements
* Operating environment (moisture, salts, fluids, temperature)

#### 5.2 Corrosion control (CPCP-aligned principles)

* Cleaning and neutralization after corrosion removal
* Re-protection of bare metal (conversion + primer + topcoat or approved equivalent)
* Seal restoration and drain/vent path preservation

---

### 6) Repairs and acceptability criteria

#### 6.1 Damage classification (minimum taxonomy)

* **Minor damage**: within SRM "no repair" limits (may allow blend-out / stop-drill per rule)
* **Repairable damage**: requires standard SRM repair scheme (doubler/patch/scarf)
* **Non-repairable**: replacement required or approved engineering repair needed

#### 6.2 Metallic repair practices (examples of covered methods)

* Stop drilling crack tips (where allowed), blend-out limits, surface finish control
* External/internal doublers, splice repairs, riveted/bolted repairs
* Cold working/oversize practices only when approved

#### 6.3 Composite repair practices (examples of covered methods)

* Scarf repairs with ply-by-ply restoration, orientation control
* Core repairs (plug, splice, potting) with edge close-out rules
* Cure management (time/temperature), vacuum integrity, debulk and inspection

**Rule:** Structural repairs shall restore:

* Load path
* Environmental sealing
* Lightning/EMC features (if present)
* Surface profile limits (aerodynamic/fit constraints)

---

### 7) Inspection and NDT (entry-level standard)

This standard defines *when* and *how* inspections are invoked; specific acceptance limits remain in SRM/NDT manuals.

Covered inspection families:

* Visual inspection (general/detailed)
* Dye penetrant (metals)
* Eddy current (crack detection around fastener holes)
* Ultrasonic (composites, bonds, laminates)
* Tap test (limited use, controlled conditions)

**Rule:** Any repair that relies on bonding integrity shall have a defined verification method (process controls + inspection).

---

### 8) Interfaces, ICDs, and digital models

#### 8.1 CSDB / S1000D linkage (recommended)

* Standard practices content should be authored as reusable modules (e.g., common process DMs) referenced by:

  * Maintenance procedures (PM)
  * Fault isolation / corrective tasks (if applicable)
  * SRM extracts (controlled reuse only)

**Rule:** A task DM shall reference the exact standard practice revision used at release time (configuration control).

#### 8.2 Evidence and traceability (configuration)

Minimum evidence objects expected per repair event:

* Material batch / shelf-life (sealants, adhesives, prepregs)
* Tool calibration status (torque tools, NDT equipment)
* Environmental conditions logs where required (bonding/cure)
* Inspection record + disposition reference

---

### 9) Change control (LC01–LC13 aligned)

* Changes to standard practices **shall** be versioned and reviewed as safety-relevant enabling content.
* Any change impacting acceptability/limits **shall** trigger:

  * impact analysis on SRM/procedures
  * downstream CSDB regeneration controls
  * release notes with migration guidance

---

## ATA Cross-References

| Related ATA | Relationship |
|-------------|-------------|
| ATA 51 | General structural standards and damage tolerance criteria |
| ATA 53 | Fuselage structure practices and repairs that invoke ATA 20 methods |
| ATA 55 | Stabilizers structure practices and repairs that invoke ATA 20 methods |
| ATA 56 | Windows/windshields structural interfaces and sealing practices |
| ATA 57 | Wings structure practices and repairs that invoke ATA 20 methods |

---

## File Structure

| File | Description |
|------|-------------|
| `README.md` | This file |
| `STANDARDS_MATERIALS.md` | Approved material families, handling, compatibility rules |
| `STANDARDS_FASTENERS_TORQUE.md` | Fastener practices, hole quality, torque/locking rules |
| `STANDARDS_SURFACE_TREATMENTS.md` | Conversion, primer/topcoat, sealing, corrosion prevention |
| `REPAIR_ACCEPTABILITY.md` | Damage taxonomy, acceptability flow, escalation triggers |
| `INSPECTION_NDT.md` | Inspection invocation rules and method selection guidance |

---

## Related Documents

- [T-TECHNOLOGIES README](../../README.md)
- [Lifecycle Phase Registry](../../../../lifecycle/LC_PHASE_REGISTRY.yaml)
