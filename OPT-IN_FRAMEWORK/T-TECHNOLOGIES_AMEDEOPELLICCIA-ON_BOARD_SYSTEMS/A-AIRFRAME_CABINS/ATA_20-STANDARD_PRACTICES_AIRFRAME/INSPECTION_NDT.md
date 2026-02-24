# ATA 20 — Inspection Invocation Rules and NDT Method Selection Guidance

**Doc ID:** T-A-ATA20-NDT-001
**Lifecycle:** LC04 (planned increment)
**Parent:** [ATA 20 README](README.md)

---

## 1) Scope

Defines when and how inspection methods are invoked for airframe structural work on the **AMPEL360 Q100** platform (both WTW and BWB variants). Specific acceptance limits and detailed procedures remain in the SRM and applicable NDT manuals.

> **Note:** This file is a planned increment under LC04. Governing rules are summarised in `README.md` §7.

---

## 2) Inspection Invocation Matrix

| Task Type | Minimum Required Inspection | Notes |
|-----------|---------------------------|-------|
| Any structural repair (metallic) | Visual (GVI) + applicable NDT per §3 | Additional NDT if in fatigue zone |
| Any structural repair (composite) | Visual + tap test + UT (bond/laminate) | Tap test alone insufficient for primary structure |
| Fastener removal and replacement | Visual (hole quality) + eddy current if suspect | Mandatory eddy current at fatigue-critical holes |
| Corrosion removal (Class 2+) | Visual + dimensional + dye penetrant (metals) | Confirm depth/area within allowable before re-protect |
| Bonded repair (metallic/composite) | Process controls + UT (bond line) | Acceptance criteria in repair scheme / SRM |
| Routine access area closure | Visual (GVI) minimum | Verify drain/vent path open and sealant applied |

---

## 3) NDT Method Selection Guidance

### 3.1 Visual Inspection (VT)

| Type | Application | Equipment |
|------|-------------|-----------|
| General Visual Inspection (GVI) | Screen for obvious damage, missing fasteners, fluid leaks | Unaided eye at normal working distance |
| Detailed Visual Inspection (DVI) | Close examination of specific area | Torch, mirror, magnifying glass (×10 max) |
| Special Detailed Inspection (SDI) | Specific defect types at identified locations | Borescope, endoscope, CCTV as applicable |

**Invocation rule:** GVI is the default minimum; DVI required for areas identified by SRM, after any structural event (hard landing, lightning strike, ground damage), and after all structural repairs.

---

### 3.2 Dye Penetrant Inspection (PT)

| Application | Suitable for | Not suitable for |
|-------------|-------------|-----------------|
| Surface-open crack detection | Metallic (aluminium, steel, titanium) | Composites, porous materials |
| Corrosion-removal area check | Confirm no remaining cracks after blend | Subsurface defects |

**Rules (shall):**
- Clean surface to bare metal (no paint, sealant, conversion coat) before penetrant application.
- Observe minimum dwell times per process spec (temperature-dependent).
- Remove penetrant completely before developer application.
- Interpret under adequate lighting (minimum 500 lux, white light; UV for fluorescent PT).

---

### 3.3 Eddy Current Inspection (ET)

| Application | Suitable for | Notes |
|-------------|-------------|-------|
| Fatigue crack detection at fastener holes | Aluminium and titanium | Can inspect through limited paint thickness with calibration |
| Surface and near-surface cracks | Metallic (conductive) | Depth limited to ~6 mm depending on frequency |
| Conductivity measurement | Alloy identification, heat damage | Requires calibration standard for alloy |

**Rules (shall):**
- Calibrate probe and instrument with reference standard of same material/geometry before use.
- Use correct frequency for penetration depth required.
- Record lift-off, calibration, and scan results in inspection record.

---

### 3.4 Ultrasonic Inspection (UT)

| Method | Application | Notes |
|--------|-------------|-------|
| Pulse-echo (contact) | Laminate thickness, delamination (composites) | Requires couplant (gel/water); calibrate on reference block |
| Through-transmission (TTU) | Bond line integrity, large composite panels | Requires access from both sides |
| Phased array UT (PAUT) | Complex geometry, primary composite structure | Operator qualification required (Level II minimum) |

**Rules (shall):**
- Calibrate on approved reference standard (same material stack as component) before and after inspection.
- Gate settings and scan resolution shall be per approved procedure.
- Operator qualification: minimum UT Level II per EN4179 / NAS410 or equivalent.

---

### 3.5 Tap Test (TT)

| Application | Limitation |
|-------------|-----------|
| Disbond/delamination screening in composite sandwich | Unreliable for thick laminates (>3 mm) or deep core disbonds |
| Quick in-field screen prior to UT | Shall not substitute for UT on primary structure |

**Rules (shall):**
- Use calibrated tap hammer or coin; standardised coin tap acceptable for secondary structure screening.
- Any area flagged by tap test on primary structure **shall** be confirmed by UT before disposition.

---

## 4) Repair Bonding Integrity — Mandatory Verification

Any repair that relies on bonding integrity (adhesive, wet layup, prepreg) **shall** include:

| Step | Requirement |
|------|-------------|
| Process monitoring | Temperature, pressure, and vacuum log during cure |
| Post-cure visual | Inspect for voids, porosity, incomplete cure (colour, tack) |
| NDT (UT/TTU) | Verify bond line continuity to approved procedure |
| Acceptance criteria | Per repair scheme or SRM NDT acceptance standard |

---

## 5) Inspector Qualification Requirements (minimum)

| NDT Method | Minimum Qualification |
|-----------|----------------------|
| Visual (GVI/DVI) | Basic Structures authorisation per maintenance organisation |
| Dye Penetrant (PT) | Level I (supervised) / Level II (independent) per EN4179/NAS410 |
| Eddy Current (ET) | Level I (supervised) / Level II (independent) per EN4179/NAS410 |
| Ultrasonic (UT) | Level II per EN4179/NAS410 |
| Phased Array UT | Level II with PAUT endorsement |

---

## Related Documents

- [ATA 20 README](README.md)
- [REPAIR_ACCEPTABILITY.md](REPAIR_ACCEPTABILITY.md)
- [STANDARDS_MATERIALS.md](STANDARDS_MATERIALS.md)
- [ATA 51 — Structures General](../ATA_51-STRUCTURES_GENERAL/README.md)
