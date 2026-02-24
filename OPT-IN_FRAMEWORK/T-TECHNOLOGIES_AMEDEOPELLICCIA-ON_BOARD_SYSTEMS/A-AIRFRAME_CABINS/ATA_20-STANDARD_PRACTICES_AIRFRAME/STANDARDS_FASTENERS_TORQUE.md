# ATA 20 — Fastener Practices, Hole Quality, Torque and Locking Rules

**Doc ID:** T-A-ATA20-FAST-001
**Lifecycle:** LC03 (planned increment)
**Parent:** [ATA 20 README](README.md)

---

## 1) Scope

Defines fastener selection, installation, hole quality requirements, torque application, and locking methods for airframe maintenance and repair on the **AMPEL360 Q100** platform (both WTW and BWB variants).

> **Note:** This file is a planned increment under LC03. Governing rules are summarised in `README.md` §4. Specific torque tables and fastener part numbers will be populated during detailed engineering.

---

## 2) Fastener Families and Selection

### 2.1 Solid and Blind Rivets

| Type | Drive | Application | Notes |
|------|-------|-------------|-------|
| 2117-T4 solid rivet | Bucked | Sheet metal joins | Most common; annealed for driving |
| NAS1097 solid rivet (countersunk) | Bucked | Flush aerodynamic skins | Verify countersink angle per drawing |
| Cherry / Huck blind rivet | Tool-set | Limited access areas | Match grip length to stack thickness |

**Rules (shall):**
- Select rivet material compatible with sheet material (no aluminium rivet into steel stack without engineering approval).
- Verify grip range before installation; oversized grip **shall not** be forced.

### 2.2 Hi-Lok and Lockbolt Systems

| Family | Collar Type | Application |
|--------|------------|-------------|
| Hi-Lok (HL) | Wrenching collar, torque-off | Primary structure, spar/rib joins |
| Huck BOM / CherryMAX lockbolt | Pull-type collar | High-shear joints, floor beams |

**Rules (shall):**
- Inspect pin for witness mark confirming collar separation (Hi-Lok).
- Do not reuse Hi-Lok pins after collar removal.

### 2.3 Bolts, Screws, Nuts, and Washers

| Standard | Application | Notes |
|----------|-------------|-------|
| NAS/AN hex bolts | General structural | Match grip length; washers under nut only per drawing |
| MS21250 / NAS1351 screws | Panel fasteners | Use with nut plate only where drawing specifies |
| AN960/NAS1149 washers | Load spreading | Do not omit; check drawing callout |

### 2.4 Inserts and Captive Fasteners

- Helical wire inserts (Heli-Coil / Kato): install per torque class; use approved installation tool.
- Nut plates (MS21047, K1000): riveted per drawing; verify torque drive fit before install.

---

## 3) Hole Quality Requirements

### 3.1 Drilled Hole Limits

| Parameter | Requirement | Inspection Method |
|-----------|-------------|------------------|
| Diameter tolerance | Per drawing (typically H8/H9) | Pin gauge or digital caliper |
| Roundness | ≤0.05 mm out-of-round (typical) | Pin gauge |
| Surface finish | 63 µin Ra (1.6 µm) or better | Visual + comparator |
| Burr height | ≤0.076 mm (0.003 in) | Visual + feeler |
| Countersink angle/depth | Per drawing ±0.5° / +0/−0.08 mm | Countersink gauge |

### 3.2 Edge Distance and Pitch

- Edge distance (e) and fastener pitch (p) **shall** meet SRM/drawing minimums.
- Encroachment of ≤5% on edge distance: engineering disposition required.
- Encroachment >5%: panel/part replacement or engineering repair required.

### 3.3 Hole Rework Ladder

| Condition | Allowed Action |
|-----------|---------------|
| Hole slightly undersize | Ream to nominal |
| Hole oversize ≤ one step | Upsize fastener (per SRM rework table) |
| Hole elongated / cracked | Engineering disposition mandatory |
| Multiple holes affected in pattern | Full engineering review required |

**Rule:** Upsize is a one-way path; record all upsizes in the repair record.

---

## 4) Torque Application

### 4.1 Torque States

| State | Definition | Torque Modifier |
|-------|------------|----------------|
| Dry | No lubricant | Use DRY torque table value |
| Lubricated | Approved thread lubricant applied | Use WET torque table value (typically reduced) |
| Wet-installed with sealant | PR sealant on thread | Use WET table; verify cure before final torque where required |

**Rule:** Torque values are **not interchangeable** between states. Always identify the torque state before applying.

### 4.2 Torque Tool Requirements

- Use calibrated torque wrenches or power tools with certified calibration (traceable to national standard).
- Calibration interval: per maintenance organisation quality procedure (typically 6–12 months or after drop/impact event).
- Record tool calibration ID in repair documentation.

### 4.3 Prevailing Torque Allowance

For self-locking nuts: measure prevailing torque before seating; add to specified torque to determine final applied torque.

---

## 5) Locking Methods

| Method | Application | Rule |
|--------|-------------|------|
| Cotter pin (AN380/MS24665) | Castle nuts, clevis pins | Pin legs bent 90° minimum in opposite directions |
| Lockwire (MS20995) | Bolt heads, drain plugs | Wire direction: tightening direction; 6–8 twists per inch |
| Self-locking nut (MIL-N-25027 / NAS) | General structure | Replace after removal if locking insert compressed |
| Thread-locking compound (Loctite) | Small fasteners, inserts | Approved grade per CMM; observe cure time before load |
| Safety cable | Access panels, quick-release | Pull test per approved procedure |

**Rule:** Do not mix locking methods unless explicitly approved by drawing/SRM.

---

## Related Documents

- [ATA 20 README](README.md)
- [STANDARDS_MATERIALS.md](STANDARDS_MATERIALS.md)
- [REPAIR_ACCEPTABILITY.md](REPAIR_ACCEPTABILITY.md)
