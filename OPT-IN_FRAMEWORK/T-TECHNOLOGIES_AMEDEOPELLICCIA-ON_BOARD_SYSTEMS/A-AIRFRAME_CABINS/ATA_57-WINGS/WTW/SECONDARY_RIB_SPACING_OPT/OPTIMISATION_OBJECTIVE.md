# Wing Rib Spacing — Optimisation Objective Function

**Module:** Wing Rib Spacing Optimisation
**Doc ID:** T-A-ATA57-WTW-RIBOPT-OBJ-001
**Lifecycle gate:** LC57-03
**Status:** DRAFT

## 1. Problem Statement
Find the rib spacing register vector **R** = [r₁, r₂, ..., r_N] (N = number of rib bays,
each rᵢ ∈ {0, 1, ..., 255}) that minimises structural mass while satisfying fatigue life
and aeroelastic divergence constraints.

## 2. Decision Variables
| Variable | Domain | Description |
|---------|--------|-------------|
| rᵢ | {0..255} | 8-bit register value for rib bay i |
| N | Integer, TBD | Number of optimisable rib bays (excludes fixed boundary ribs) |

## 3. Objective Function

### 3.1 Primary Objective: Minimum structural mass
```
minimise  f(R) = Σᵢ m_rib(rᵢ) + m_skin_panels(R)
```
Where:
- `m_rib(rᵢ)` = mass of rib i as a function of its spacing register value (bay area × rib web area density)
- `m_skin_panels(R)` = skin panel mass, which depends on rib spacing through required skin thickness (buckling-driven or fatigue-driven)

### 3.2 Secondary Objective (lexicographic priority):
In case of equal mass: maximise minimum fatigue life margin across all bays.

## 4. Constraints
See `CONSTRAINTS_FATIGUE_AND_DIVERGENCE.md` for full constraint definitions.

| Constraint ID | Type | Limit |
|--------------|------|-------|
| C-FATIGUE | Inequality | Fatigue life ≥ 80,000 cycles (CS-25 Appendix J) |
| C-DIVERGENCE | Inequality | Divergence speed margin ≥ 15% above VD/MD (CS-25.629) |
| C-BUCKLING | Inequality | Skin panel buckling load factor ≥ 1.0 at DLL |
| C-MIN-PITCH | Inequality | Spacing ≥ S_min for each bay |
| C-MAX-PITCH | Inequality | Spacing ≤ S_max for each bay |
| C-BOUNDARY | Equality | Fixed ribs at tank boundaries, root, tip, and access bays |

## 5. Solution Method
The optimisation is implemented as an integer optimisation problem solved by:
1. **Initial screening:** Exhaustive or quasi-random search over reduced design space
2. **Main optimisation:** Genetic algorithm (GA) with:
   - Population size: see `MODELS/optimisation_config.yaml`
   - Chromosome: N 8-bit integers (one per rib bay)
   - Fitness: f(R) with penalty method for constraint violations
   - Selection: Tournament selection (k=3)
   - Crossover: Uniform crossover (p=0.8)
   - Mutation: Bit-flip with p_mutation per bit = see config
3. **Verification:** Determinism check via `TEST_WTW_DETERMINISM_REPRODUCIBILITY.md`

## 6. Output
The optimisation produces a register pack (`rib_spacing_registers.example.yaml` format)
containing the optimal register value for each rib bay, together with:
- Decoded physical spacing [mm]
- Predicted structural mass [kg]
- Fatigue life margin [%] per bay
- Divergence speed margin [%] at wing level

## 7. Traceability to Requirements
| Requirement | Objective / Constraint Reference |
|------------|----------------------------------|
| REQ-WTW-57-RIBOPT-001 | Encoding standard (§2) |
| REQ-WTW-57-RIBOPT-002 | Determinism requirement |
| REQ-WTW-57-RIBOPT-003 | Fatigue constraint C-FATIGUE |
| REQ-WTW-57-RIBOPT-004 | Divergence constraint C-DIVERGENCE |
| REQ-WTW-57-RIBOPT-006 | Buckling constraint C-BUCKLING |
