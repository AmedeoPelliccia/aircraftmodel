# Fatigue and Aeroelastic Divergence Constraints — BWB Blend Zone TDF

**Doc ID:** T-A-ATA57-BWB-BLEND-CNST-001  
**Status:** DRAFT  
**Regulatory basis:** CS-25.571 (fatigue/damage tolerance), CS-25.629 (flutter/divergence)

---

## 1. Fatigue Life Constraint (C-FATIGUE)

### 1.1 Statement
Every TDF patch in the blend zone SHALL sustain a minimum of **80,000 flight cycles** at the
AMPEL360 BWB design load spectrum without fatigue crack initiation or delamination exceeding
the damage tolerance threshold defined in the Damage Tolerance Plan.

### 1.2 Methodology
- **Fatigue law:** Miner's cumulative damage rule (Σ n_i / N_i ≤ 1.0)
- **Material property:** CFRP B-basis fatigue allowables with scatter factor γ = 2.0
- **Load spectrum:** AMPEL360 BWB baseline spectrum (TBD at LC57-04 stress analysis)
- **Patch-level evaluation:** Each patch is evaluated independently; adjacent patches may be
  evaluated as a group if structurally continuous

### 1.3 Constraint expression (for GA optimiser)
```
C_FATIGUE(r) = D_Miner(r) ≤ 1.0 / γ = 0.5
```
where `D_Miner(r)` is the Miner damage sum computed at register value `r`.

### 1.4 Physical mechanism
Thinner patches (lower register values) experience higher cyclic strain amplitude → shorter
fatigue life. The optimiser is therefore constrained to maintain registers above a
thickness-dependent lower bound `r_min_fatigue(location)`.

---

## 2. Aeroelastic Divergence Constraint (C-DIVERGENCE)

### 2.1 Statement
The blend zone stiffness matrix, as a function of the TDF register map, SHALL produce an
aeroelastic divergence speed V_div ≥ **1.15 × VD** per CS-25.629(d).

### 2.2 Methodology
- **Analysis method:** Doublet Lattice Method (DLM) eigenvalue analysis of the blend zone
  aeroelastic stiffness matrix
- **Stiffness parameterisation:** Blend zone stiffness K(r) is computed from the TDF register
  map via finite element homogenisation
- **Divergence eigenvalue:** smallest positive eigenvalue λ_div; V_div = √(2K_eff / q_ref)
- **Margin:** M_div = V_div / VD − 1.0 ≥ 0.15

### 2.3 Constraint expression (for GA optimiser)
```
C_DIVERGENCE(r) = V_div(r) / VD ≥ 1.15
```

### 2.4 Physical mechanism
Reducing patch stiffness (lower register values) in the blend zone reduces the torsional
stiffness of the blended planform, which reduces the divergence speed. The optimiser must
maintain sufficient aggregate stiffness in the critical inboard blend patches.

---

## 3. Interaction of Constraints

The fatigue and divergence constraints act in opposing directions on the register values:
- **C-FATIGUE** sets a lower bound on register values (minimum thickness per location)
- **C-DIVERGENCE** sets a lower bound on aggregate stiffness (minimum register sum in torsion-critical patches)

The multi-objective optimiser minimises structural mass subject to both constraints simultaneously
(constraints are embedded in `REQ_BWB_57_BLEND_TDF_OPT.yaml`).
