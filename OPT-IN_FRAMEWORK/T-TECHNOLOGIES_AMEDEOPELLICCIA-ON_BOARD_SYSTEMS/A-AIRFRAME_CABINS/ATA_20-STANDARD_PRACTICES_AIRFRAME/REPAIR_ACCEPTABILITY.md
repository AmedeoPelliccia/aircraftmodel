# ATA 20 — Damage Taxonomy, Repair Acceptability Flow, and Escalation Triggers

**Doc ID:** T-A-ATA20-REP-001
**Lifecycle:** LC04 (planned increment)
**Parent:** [ATA 20 README](README.md)

---

## 1) Scope

Defines the damage classification taxonomy, repair acceptability decision flow, and escalation triggers for airframe damage on the **AMPEL360 Q100** platform (both WTW and BWB variants).

> **Note:** This file is a planned increment under LC04. Governing rules are summarised in `README.md` §6. Specific SRM chapter references and allowable tables will be added during detailed engineering.

---

## 2) Damage Classification Taxonomy

### 2.1 Metallic Structure

| Class | Definition | Default Disposition |
|-------|------------|---------------------|
| **Negligible damage** | Dents, scratches within SRM "no repair" limits | Clean, protect, close |
| **Minor damage** | Dent depth/area within SRM "blend-out only" limits | Blend, verify, protect |
| **Repairable damage** | Exceeds minor limits but within SRM repair scheme | Standard SRM repair (doubler / stop-drill per SRM) |
| **Non-standard / major damage** | Exceeds SRM repair limits or involves primary load path | Engineering disposition required before repair |
| **Beyond repair** | Structural integrity cannot be restored by SRM methods | Part replacement required |

### 2.2 Composite Structure

| Class | Definition | Default Disposition |
|-------|------------|---------------------|
| **Surface scratch / paint damage** | Paint only; no fibre damage | Repaint per surface treatment standard |
| **Barely visible impact damage (BVID)** | Within design allowable; no delamination growth expected | Monitor per inspection schedule (SRM controlled) |
| **Visible impact damage (VID)** | Visible surface damage; delamination possible | Tap test/UT inspection; scarf repair if confirmed |
| **Penetrating damage** | Full or partial puncture through laminate | Core/ply repair per SRM |
| **Major structural damage** | Damage to primary load-bearing composite element | Engineering repair scheme required |

---

## 3) Repair Acceptability Decision Flow

```
[DAMAGE FOUND]
     │
     ▼
[Identify material type: Metallic / Composite / Mixed]
     │
     ▼
[Classify damage per §2 above]
     │
     ├─► Negligible / BVID → Protect/Monitor → CLOSE
     │
     ├─► Minor / VID → Blend-out or inspection → [Within SRM limits?]
     │                                              │
     │                                              ├─ YES → Protect/repair per SRM → CLOSE
     │                                              └─ NO  → Escalate to Repairable
     │
     ├─► Repairable → Apply SRM repair scheme → [Verify load path, seal, EMC]
     │                → [NDT verification] → [Accept?]
     │                    │
     │                    ├─ YES → Record repair → CLOSE
     │                    └─ NO  → Escalate to Engineering
     │
     └─► Major / Non-repairable → [Engineering Disposition]
                                   → [Approved repair scheme or replacement]
                                   → CLOSE per engineering authority
```

---

## 4) Escalation Triggers (shall escalate to engineering)

The following conditions **shall** trigger mandatory engineering notification before proceeding:

| Trigger | Condition |
|---------|-----------|
| Load path involvement | Damage to primary load-carrying member (spar cap, frame, keel beam) |
| Fatigue-sensitive zone | Damage at or within 25 mm (1 in) of known fatigue-critical location |
| Repeated damage | Same location has been repaired more than once |
| Limits exceeded | SRM blend/repair allowables exceeded |
| Crack detected | Any crack in metallic primary structure |
| Delamination growth | Composite delamination growth confirmed at re-inspection |
| Repair failure | Previously applied repair has disbonded, cracked, or otherwise failed |
| Corrosion Class 3 | Material loss beyond SRM allowable depth/area |
| Uncertainty | Inspector uncertainty about classification or applicable SRM chapter |

---

## 5) Structural Repair Restoration Requirements

All structural repairs **shall** restore:

| Requirement | Verification Method |
|-------------|---------------------|
| **Load path** | Engineering analysis or conservative SRM compliance |
| **Environmental sealing** | Visual + sealant continuity check |
| **Lightning/EMC features** | Continuity check per approved procedure |
| **Surface profile limits** | Step measurement (≤0.076 mm for aerodynamic critical zones) |
| **Drain/vent paths** | Physical verification (probe/light) |

---

## 6) Documentation Requirements

Every repair event **shall** be documented with:

1. **Damage record**: photograph(s), location sketch, measurement data.
2. **Material traceability**: batch/shelf-life of sealants, adhesives, prepregs used.
3. **Tool record**: calibrated torque wrench ID, NDT equipment ID.
4. **Environmental log**: temperature/humidity at bonding/cure (composites).
5. **Inspection record**: NDT method, acceptance criteria reference, result, inspector ID.
6. **Disposition reference**: SRM chapter/repair number or engineering repair scheme number.

---

## Related Documents

- [ATA 20 README](README.md)
- [INSPECTION_NDT.md](INSPECTION_NDT.md)
- [STANDARDS_MATERIALS.md](STANDARDS_MATERIALS.md)
- [STANDARDS_FASTENERS_TORQUE.md](STANDARDS_FASTENERS_TORQUE.md)
- [ATA 51 — Structures General](../ATA_51-STRUCTURES_GENERAL/README.md)
