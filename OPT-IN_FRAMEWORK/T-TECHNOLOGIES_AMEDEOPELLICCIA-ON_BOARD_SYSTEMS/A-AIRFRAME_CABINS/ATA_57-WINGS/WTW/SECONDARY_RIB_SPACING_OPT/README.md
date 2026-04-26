# Wing Rib Spacing Optimisation — Secondary Module

**Domain:** T-TECHNOLOGIES / A-AIRFRAME_CABINS / ATA 57 Wings / WTW
**Module ID:** T-A-ATA57-WTW-RIBOPT-001
**Lifecycle gate:** LC57-03 (Detailed Design)
**Status:** DRAFT

## Purpose
This secondary module defines the Wing Rib Spacing Optimisation method for the AMPEL360 WTW.
Rib spacing is the primary structural parameter governing the trade between:
- **Mass efficiency** (fewer ribs = lighter structure)
- **Skin panel buckling resistance** (tighter ribs = higher buckling allowable)
- **Fatigue life** (rib pitch affects in-plane load redistribution and stress concentration at rib-to-spar joints)
- **Aeroelastic divergence speed** (rib spacing affects torsional rigidity and divergence margin)

## Encoding Convention
Rib spacing is discretised to **8-bit registers** per rib bay (see `STD_RIB_SPACING_ENCODING.md`).
This deterministic encoding enables:
1. Reproducible optimisation runs (bit-for-bit identical output from identical config)
2. Integer optimisation solvers (genetic algorithm, branch-and-bound)
3. Traceability from requirement to register value to physical dimension

## Contents

| File | Purpose |
|------|---------|
| `STD_RIB_SPACING_ENCODING.md` | 8-bit register standard: range, resolution, bias, boundary conditions |
| `OPTIMISATION_OBJECTIVE.md` | Multi-objective function definition (mass, buckling, fatigue, divergence) |
| `CONSTRAINTS_FATIGUE_AND_DIVERGENCE.md` | Binding constraint definitions with traceability to CS-25 |
| `REQ_WTW_57_RIB_SPACING_OPT.yaml` | Structured requirements for the optimisation module |
| `MODELS/rib_bay_definition.yaml` | Rib bay geometry definitions (spanwise station, chord fraction) |
| `MODELS/rib_spacing_registers.example.yaml` | Example register pack for a nominal WTW inner wing |
| `MODELS/optimisation_config.yaml` | Optimisation algorithm configuration (population, generations, constraints) |
| `VERIFICATION_EVIDENCE/` | Evidence stubs: fatigue life check, divergence margin check, determinism test |

## Constraints Summary

| Constraint | Limit | Reference |
|-----------|-------|-----------|
| Minimum fatigue life | 80,000 flight cycles | CS-25 Appendix J / LC57-09 |
| Aeroelastic divergence margin | ≥ 15% above VD/MD | CS-25.629 |
| Minimum rib spacing | TBD mm (driven by access) | Manufacturing WI |
| Maximum rib spacing | TBD mm (driven by skin buckling) | Structural analysis |
