# TOP-LAP — Multi-Dimensional Logical State Process

## LC05 Formal Framework · AMPEL360 Family

<p align="center">
  <img src="https://img.shields.io/badge/Framework-TOP--LAP-0066cc" alt="TOP-LAP">
  <img src="https://img.shields.io/badge/Phase-LC05%20Analysis%20Models-blue" alt="LC05">
  <img src="https://img.shields.io/badge/Status-CONFIRMED-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/Family-AMPEL360-purple" alt="AMPEL360">
  <img src="https://img.shields.io/badge/Tokenomics-TT%20v3.14-gold" alt="TT">
  <img src="https://img.shields.io/badge/Programmes-WTW%20%C3%97%20BWB-teal" alt="Programmes">
</p>

<p align="center">
  <strong>Formal process specification for multi-dimensional state-space analysis,
  uncertainty reduction, and evidence generation across the AMPEL360 programme
  family lifecycle.</strong>
</p>

---

| Field | Value |
|---|---|
| **Document ID** | AMPEL360-FAM-TOPLAP-001 Rev A |
| **Classification** | Engineering Process — LC05 Analysis Framework |
| **Date** | 2026-02-23 |
| **Author** | Amedeo Pelliccia / AI-Assisted Engineering |
| **Scope** | AMPEL360 WTW × AMPEL360 BWB (family-level) |
| **Framework** | OPT-IN v1.1 / LC05 Analysis Models |
| **Dependency** | IBD-001 Rev B (inheritance boundary) |
| **Status** | CONFIRMED |

---

## 1. Purpose & Scope

**TOP-LAP** (Multi-Dimensional Logical State Process) is the formal analysis
framework governing all LC05 simulation, modelling, and evidence-generation
activities within the AMPEL360 programme family. It defines:

1. **State-space dimensions** — the physical and logical variables tracked
   across each analysis domain
2. **Transition operators** — the mathematical and procedural transformations
   that advance a system from one state to the next
3. **Validation gates** — acceptance criteria that must be satisfied before
   a state transition is certified
4. **Evidence chains** — the traceable path from raw analysis output to KNOT
   residual reduction and TT distribution

TOP-LAP applies to both AMPEL360 WTW (Wide Tube & Wing) and AMPEL360 BWB
(Quantum-Enhanced Blended Wing Body). Where analysis methods diverge between
programmes, the **inheritance boundary** (IBD-001 Rev B §7) governs which
models are SHARED and which are FORKED.

---

## 2. Foundations

### 2.1 State Vector Notation

Every analysable subsystem in AMPEL360 is represented by a state vector
**S** in a multi-dimensional logical space:

```
S_i = (D₁, D₂, ..., D_n)_i
```

where each **D_k** is a dimension relevant to the subsystem's physics. The
subscript **i** indexes the analysis iteration (time-step, design loop, or
uncertainty-reduction cycle).

### 2.2 C² CELL State Vector (ATA 28 Specialisation)

For cryogenic subsystems governed by the C² CELL paradigm (Chemical
Containment & Circulation), the state vector specialises to:

```
S_i = (M_i, P_i, T_i, G_i)
```

| Dimension | Symbol | Unit | Description |
|---|---|---|---|
| Mass | M_i | kg | Prime Material inventory (LH₂, NH₃, or N₂) |
| Pressure | P_i | bar | Vessel / line operating pressure |
| Thermal | T_i | K | Bulk temperature of the Prime Material |
| Phase/Grade | G_i | — | Phase state (liquid, gas, two-phase) or purity grade |

This 4-tuple propagates through every C² CELL analysis model and is the
primary input to KNOT residual calculations for ATA 28, ATA 47, and ATA 75.

### 2.3 Extended State Vectors

Beyond the C² CELL core, TOP-LAP defines extended dimensions for
structural, aerodynamic, and certification analyses:

| Domain | State Vector | Dimensions |
|---|---|---|
| **Structural (ATA 51–57)** | S_struct = (σ, ε, T, N_cyc) | Stress, strain, temperature, fatigue cycles |
| **Aerodynamic (ATA 27)** | S_aero = (CL, CD, α, Ma) | Lift coefficient, drag, angle of attack, Mach |
| **CG / Stability (ATA 55)** | S_cg = (x_cg, z_cg, m_tot, I_yy) | CG position, total mass, pitch inertia |
| **Thermal (ATA 21/75)** | S_therm = (Q_in, Q_out, T_wall, η_HX) | Heat flux in/out, wall temp, HX efficiency |
| **Safety (ATA 26/47)** | S_safe = (c_H2, c_NH3, c_O2, t_resp) | H₂/NH₃/O₂ concentrations, response time |

Each KNOT's analysis model must declare which state vector it operates on
and which dimensions it resolves.

---

## 3. Process Architecture

### 3.1 The TOP-LAP Cycle

TOP-LAP operates as a **four-phase iterative cycle** that transforms
uncertainty into evidence:

```
╔═══════════════════════════════════════════════════════════════╗
║                    TOP-LAP CYCLE                              ║
║                                                               ║
║   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌────────┐ ║
║   │  TOPO    │───▶│  OPER    │───▶│  PROJ    │───▶│  LATCH │ ║
║   │  Define  │    │  Execute │    │  Project │    │  Lock  │ ║
║   │  state   │    │  transit │    │  residual│    │  evid. │ ║
║   │  space   │    │  operator│    │  Δ       │    │  chain │ ║
║   └──────────┘    └──────────┘    └──────────┘    └────────┘ ║
║        │                                               │      ║
║        └───────────────── iterate ◀────────────────────┘      ║
╚═══════════════════════════════════════════════════════════════╝
```

| Phase | Name | Action | Output |
|---|---|---|---|
| **T** | **TOPO** (Topology) | Define the state-space dimensions and initial conditions for the KNOT | State vector S₀, dimension declaration |
| **O** | **OPER** (Operate) | Execute the transition operator (simulation, FEA, CFD, test correlation) | State trajectory S₀ → S₁ → ... → S_n |
| **P** | **PROJ** (Project) | Project the analysis results onto the KNOT residual axis; compute Δ_residual | `delta_residual_primary` value for TT formula |
| **L** | **LATCH** (Latch) | Lock the evidence into the KNOT/KNU chain; gate acceptance; distribute TT | KNU_EVIDENCE.md committed; KNOT residual updated |

### 3.2 Phase Details

#### T — TOPO (Topology Definition)

Before any analysis begins, the analyst must:

1. Identify the **KNOT** being addressed
2. Declare the **state vector** type (C² CELL, structural, aero, etc.)
3. Specify **initial conditions** S₀ with uncertainty bounds
4. Define the **target state** S_target and acceptance envelope
5. Register the analysis in `KNU_PLAN.csv` as an LC05 KNU

**Artifact:** `TOPO_DECLARATION.yaml` in the KNOT simulation folder

```yaml
knot_id: KNOT-ATA28-40-00-001
knu_id: KNU-ATA28-40-001
state_vector_type: "C2_CELL"
dimensions:
  - { name: "M_NH3", unit: "kg", initial: 350, uncertainty: "±10%" }
  - { name: "P_cracker", unit: "bar", initial: 8.0, uncertainty: "±0.5" }
  - { name: "T_catalyst", unit: "K", initial: 773, uncertainty: "±25" }
  - { name: "G_conversion", unit: "fraction", initial: 0.0, target: "≥0.95" }
acceptance_envelope:
  G_conversion: { min: 0.95, target: 0.98 }
  delta_residual_primary: { min: 60 }
```

#### O — OPER (Operate Transition)

The analyst executes the analysis model (OpenModelica, FEA, CFD, or
analytical calculation). The transition operator **Φ** maps:

```
S_{i+1} = Φ(S_i, u_i, p)
```

where:
- **S_i** is the current state vector
- **u_i** is the control/input vector (design parameters under study)
- **p** is the parameter vector (material properties, boundary conditions)
- **Φ** is the transition operator (the model itself)

The operator must be:
- **Deterministic** for a given (S_i, u_i, p) triple
- **Versioned** — model files committed to SSOT/LC05 under the KNOT folder
- **Reproducible** — CI can re-execute and obtain the same results

#### P — PROJ (Project Residual)

The raw analysis output is projected onto the **KNOT residual axis** to
compute the uncertainty reduction achieved:

```
Δ_R = R_before − R_after
```

where **R** is the KNOT residual (initially 100, target per KNOTS.csv).

The **delta_residual_primary** is the key metric that feeds into the TT
distribution formula:

```
I_i = Δ_R_k,i + λ · S_i
```

where λ = 0.50 (spillover multiplier from TOKENOMICS_TT.yaml).

The projection must be documented with:
- Quantitative mapping from analysis output to residual reduction
- Uncertainty propagation (how input uncertainties affect Δ_R)
- Comparison against the acceptance envelope defined in TOPO

#### L — LATCH (Lock Evidence)

Once the PROJ phase demonstrates that acceptance criteria are met:

1. `KNU_EVIDENCE.md` is completed with all fields populated
2. The KNOT's `Residual` value in `KNOTS.csv` is updated
3. The evidence is committed to `SSOT/LC05_ANALYSIS_MODELS/`
4. The TT distribution is triggered per `TOKENOMICS_TT.yaml`
5. If the KNOT residual falls to or below its target, the KNOT is closed

**Latch is irreversible** — once evidence is accepted and TT distributed,
the KNOT residual cannot increase. New evidence can only further reduce it.

---

## 4. Multi-Dimensional Coupling

### 4.1 Cross-Dimensional Interactions

Real aircraft systems exhibit coupling between state dimensions. TOP-LAP
formalises these as **coupling tensors** between KNOTs:

```
C_{jk} : S_j × S_k → Δ_interaction
```

For example, the NH₃ cracker (ATA 28-40) is coupled to:

| Source KNOT | Coupled KNOT | Coupling | Description |
|---|---|---|---|
| KNOT-ATA28-40 | KNOT-ATA75-20 | T_catalyst ↔ Q_waste_heat | Cracker temp depends on waste heat routing |
| KNOT-ATA28-40 | KNOT-ATA47-10 | G_conversion → c_N2_purity | Cracker efficiency determines N₂ purity |
| KNOT-ATA28-40 | KNOT-ATA28-20 | M_H2_supplemental → M_LH2_boiloff | Extra H₂ from cracking offsets boil-off losses |
| KNOT-ATA28-40 | KNOT-ATA28-10 | M_NH3 → tank_volume | NH₃ inventory affects total cryogenic volume |

### 4.2 Coupled Analysis Protocol

When two or more KNOTs are coupled, TOP-LAP requires a **coupled iteration**:

1. Each KNOT executes its OPER phase independently (first pass)
2. Coupling outputs are exchanged at defined interface points
3. Each KNOT re-executes with updated boundary conditions
4. Iteration continues until the coupled residual converges (Δ < ε)

The convergence criterion ε is defined per coupling pair and recorded in
the `COUPLING_REGISTER.yaml`:

```yaml
couplings:
  - source: "KNOT-ATA28-40-00-001"
    target: "KNOT-ATA75-20-00-001"
    interface: "waste_heat_flux_kW"
    epsilon: 5.0    # kW convergence tolerance
    max_iterations: 10
```

### 4.3 Cross-Programme Coupling (IBD Spillover)

Per IBD-001 Rev B §8.3, evidence produced by a KNOT in one programme may
reduce residual uncertainty in a sibling KNOT in the other programme. This
is captured through the **spillover adjacency coefficient** `a_k_to_j`:

```
Δ_R_sibling = a_k_to_j · Δ_R_source
```

The `a_k_to_j` values are defined in `TOKENOMICS_TT.yaml` under
`cross_programme_spillover.adjacency_coefficients`. TOP-LAP's PROJ phase
must compute spillover impacts when applicable.

---

## 5. Validation Gates

### 5.1 Gate Definitions

Each TOP-LAP phase has a **mandatory validation gate** before proceeding:

| Gate | Phase Exit | Check | Fail Action |
|---|---|---|---|
| **G-T** | After TOPO | State vector declared; KNOT registered; S₀ within physics bounds | Reject — return to TOPO |
| **G-O** | After OPER | Model executes without error; output within expected order-of-magnitude | Reject — debug model |
| **G-P** | After PROJ | Δ_R computed; uncertainty bounds documented; acceptance envelope checked | Conditional — may iterate |
| **G-L** | After LATCH | KNU_EVIDENCE.md complete; BREX-validated (if PUB); KNOTS.csv updated | Reject — complete evidence |

### 5.2 Automated Gate Checks (CI Integration)

The following CI checks enforce TOP-LAP gates:

| Check | Tool | Gate |
|---|---|---|
| TOPO_DECLARATION.yaml schema | `optin_structure_validator.py` | G-T |
| Model file presence + version | Git commit hook | G-O |
| `delta_residual_primary` field present | `knot_issues_sync.py` | G-P |
| KNU_EVIDENCE.md completeness | `brex_validator.py` (if PUB) | G-L |
| Ledger hash-chain integrity | `knu_distribution.py verify` | G-L |

---

## 6. Evidence Artefact Specification

### 6.1 KNU_EVIDENCE.md Template (TOP-LAP Enhanced)

```yaml
---
# TOP-LAP Evidence Record
knot_id: KNOT-ATAxx-xx-xx-xxx
knu_id: KNU-ATAxx-xx-xxx
toplap_phase: LATCH                     # Current phase
state_vector_type: "C2_CELL"            # or STRUCTURAL, AERO, CG, THERMAL, SAFETY
dimensions_resolved:
  - { name: "dimension_name", before: <value>, after: <value>, unit: "unit" }

# Residual projection
delta_residual_primary: <numeric_value>
residual_before: <value>
residual_after: <value>
acceptance_criteria: "<description>"
acceptance_met: true | false

# Coupling
coupled_knots: []                       # List of coupled KNOT IDs if applicable
spillover_generated:
  - { sibling_knot: "KNOT-BWB-xxx", a_k_to_j: 0.xx, delta_sibling: <value> }

# Provenance
model_version: "<git SHA>"
model_path: "SSOT/LC05_ANALYSIS_MODELS/thermodynamic-models/<knot-folder>/"
analyst: "<name>"
date: "YYYY-MM-DD"
status: PLANNED | IN_PROGRESS | COMPLETE | ACCEPTED
---
```

### 6.2 Directory Structure per KNOT

```
SSOT/LC05_ANALYSIS_MODELS/thermodynamic-models/
└── KNOT-ATA28-40-00-001/
    ├── TOPO_DECLARATION.yaml      ← Phase T artefact
    ├── models/
    │   └── cracker_1d.mo          ← OpenModelica model (Phase O)
    ├── results/
    │   └── run_001.csv            ← Simulation output
    ├── PROJECTION.md              ← Phase P analysis
    ├── KNU_EVIDENCE.md            ← Phase L locked evidence
    └── COUPLING_REGISTER.yaml     ← Cross-KNOT couplings
```

---

## 7. KNOT–TOP-LAP Mapping

The following table maps each LC05 KNOT to its TOP-LAP state vector type
and primary dimensions:

| KNOT | Title | State Vector | Primary Dimensions | Couplings |
|---|---|---|---|---|
| KNOT-ATA28-10-00-001 | LH₂ Tank Structural Sizing | STRUCTURAL + C²CELL | σ_wall, T_cryo, P_internal, M_LH2 | ATA 53 (fuselage Ø) |
| KNOT-ATA28-20-00-001 | NH₃ Cryo-Shield Boil-Off | C²CELL + THERMAL | M_boiloff, T_jacket, Q_parasitic, G_phase | ATA 28-40 (cracker) |
| KNOT-ATA28-40-00-001 | NH₃ Cracker Efficiency | C²CELL | M_NH3, P_cracker, T_catalyst, G_conversion | ATA 75-20, ATA 47-10 |
| KNOT-ATA47-10-00-001 | N₂ Purity / Contaminants | SAFETY | c_N2, c_NH3_residual, c_H2O, G_purity | ATA 28-40 (cracker) |
| KNOT-ATA47-20-00-001 | Tank Inerting O₂ Control | SAFETY | c_O2, P_ullage, V_tank, t_purge | ATA 47-10 (N₂ source) |
| KNOT-ATA47-30-00-001 | Leak Sniff Sensitivity | SAFETY | c_H2_detect, c_NH3_detect, t_response | ATA 47-40 (suppression) |
| KNOT-ATA47-40-00-001 | N₂ Suppression ≤ 3 s | SAFETY | c_H2_zone, V_flood, P_N2, t_resp | ATA 47-10, ATA 47-30 |
| KNOT-ATA28-70-00-001 | H₂ Embrittlement | STRUCTURAL | σ_fatigue, N_cycles, c_H2_absorbed, T_service | — (shared evidence) |
| KNOT-ATA75-20-00-001 | Waste Heat to Cracker | THERMAL | Q_exhaust, T_bleed, η_HX, Q_delivered | ATA 28-40 (cracker) |
| KNOT-ATA55-10-00-001 | CG Envelope Management | CG | x_cg, m_LH2(t), I_yy, SM | ATA 28-10 (tank) |
| KNOT-ATA53-10-00-001 | Fuselage Diameter Trade | STRUCTURAL + AERO | Ø_fuse, S_wet, C_D0, V_cabin | ATA 28-10 (tank volume) |
| KNOT-ATA32-10-00-001 | Landing Gear Yehudi | STRUCTURAL | F_gear, x_gear, m_penalty, clearance | ATA 55-10 (CG) |
| KNOT-ATA25-50-00-001 | NH₃ Containment Zone | SAFETY + STRUCTURAL | L_zone, P_burst, t_evac, c_NH3_cabin | ATA 28-40 (cracker bay) |

---

## 8. Lifecycle Integration

### 8.1 TOP-LAP in the OPT-IN Lifecycle

```
LC01 ──── LC04 ──── LC05 ──── LC06 ──── LC07 ──── LC08
KNOT       Trade     TOP-LAP    Test      Verify    Certify
Define     Study     Analyse    Validate  Close     Publish
  │          │         │          │         │         │
  │          │    ┌────┤          │         │         │
  │          │    │TOPO│          │         │         │
  │          │    │OPER│──────────┤         │         │
  │          │    │PROJ│          │         │         │
  │          │    │LATCH─────────────────────┤         │
  │          │    └────┘          │         │         │
  └──────────┴────────────────────┴─────────┴─────────┘
                    Evidence Chain
```

TOP-LAP's primary residence is **LC05** but its outputs feed forward:

| Phase | LC05 (TOP-LAP) | Downstream |
|---|---|---|
| TOPO | State-space definition | LC04 trade study inputs |
| OPER | Simulation execution | LC06 test planning (correlation targets) |
| PROJ | Residual projection | LC07 verification evidence |
| LATCH | Evidence lock | LC08 certification data package |

### 8.2 TT Integration

The `delta_residual_primary` from TOP-LAP's PROJ phase is the primary
driver of the **impact** component in the TT distribution formula:

```
w_i = α · Ê_i + (1 − α) · Î_i      T_i = P_k · w_i
```

Where `Î_i` incorporates the normalised `delta_residual_primary`:

```
I_i = Δ_R_k,i + λ · S_i
Î_i = I_i / Σ I_i
```

TOP-LAP ensures that every `delta_residual_primary` value is:
- Quantitatively derived (not subjective)
- Traceable to a specific simulation or analysis
- Reproducible from committed model files
- Validated against acceptance criteria before LATCH

---

## 9. Programme-Specific Considerations

### 9.1 AMPEL360 WTW (Wide Tube & Wing)

The WTW variant uses the **tri-species** C² CELL state vector natively.
All 14 current KNOTs apply. The cracker coupling chain
(ATA 28-40 → ATA 47-10 → ATA 47-20/30/40) is the most complex coupled
analysis in the family.

### 9.2 AMPEL360 BWB (Quantum-Enhanced)

The BWB variant uses **single-species** C² CELL (LH₂ only). ATA 47 uses
conventional OBIGGS rather than cracker-sourced N₂. Quantum-enhanced
topology optimisation adds additional state dimensions:

```
S_quantum = (S_struct, q_topology, q_aero)
```

where `q_topology` and `q_aero` represent quantum-optimised design
variables. These are BWB-FORKED and do not appear in WTW analysis.

### 9.3 Shared Analysis (per IBD-001 Rev B)

The following TOP-LAP analyses are **SHARED** across both programmes:

- H₂ embrittlement material models (KNOT-ATA28-70-00-001)
- Standard material characterisation (material-library)
- Safety methodology (H₂ concentration limits, LFL definitions)
- TT distribution mechanics (tokenomics formula, ledger)

---

## 10. Glossary

| Term | Definition |
|---|---|
| **TOP-LAP** | Multi-Dimensional Logical State Process — the LC05 formal analysis framework |
| **TOPO** | Topology phase — define state space and initial conditions |
| **OPER** | Operate phase — execute transition operator (simulation) |
| **PROJ** | Project phase — map analysis output to KNOT residual reduction |
| **LATCH** | Latch phase — lock evidence, gate acceptance, distribute TT |
| **State vector** | Multi-dimensional tuple describing a subsystem's analysable state |
| **C² CELL** | Chemical Containment & Circulation — the cryogenic paradigm |
| **Transition operator** | Mathematical function mapping one state to the next |
| **Coupling tensor** | Formal description of cross-KNOT dimensional interactions |
| **Validation gate** | Mandatory check at each phase boundary |
| **delta_residual_primary** | Quantitative KNOT residual reduction from a single KNU |

---

<p align="center">
  <strong>AMPEL360 WTW × AMPEL360 BWB</strong><br/>
  <em>TOP-LAP — From uncertainty to evidence, one state transition at a time.</em>
</p>
<p align="center">
  <em>By Amedeo Pelliccia · AI-Assisted Engineering · aircraftmodel.eu</em>
</p>
