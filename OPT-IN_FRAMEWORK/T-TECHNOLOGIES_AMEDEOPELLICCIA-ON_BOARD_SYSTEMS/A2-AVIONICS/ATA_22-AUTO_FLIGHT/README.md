# ATA 22 — Auto Flight

**Domain:** T-TECHNOLOGIES / A2-AVIONICS
**Boundary:** MIXED — core shared here; programme extensions in forks
**Doc ID:** T-A2-ATA22-001

---

## Scope

Core autopilot, autothrottle, and flight director architecture. Programme extensions hold control law tuning for WTW (conventional aerodynamics) and BWB (non-linear pitch-heave coupling). Certification basis: CS-25.1329 and SC-FCS-001 where applicable.

---

## Programme Extensions

| Programme | Extension Path |
|-----------|---------------|
| **WTW** | `PROGRAMME_EXT/WTW/` (pointer stub) |
| **BWB** | `PROGRAMME_EXT/BWB/` (pointer stub) |

---

## ATA Cross-References

| Related ATA | Relationship |
|-------------|-------------|
| ATA 27 | Flight control surfaces |
| ATA 34 | Navigation FMS integration |
| ATA 42 | IMA hosted auto-flight functions |

---

## File Structure

| File | Description |
|------|-------------|
| `README.md` | This file |
| `PROGRAMME_EXT/` | Programme-specific extension stubs |

---

## Related Documents

- [T-TECHNOLOGIES README](../../README.md)
- [Lifecycle Phase Registry](../../../../lifecycle/LC_PHASE_REGISTRY.yaml)
