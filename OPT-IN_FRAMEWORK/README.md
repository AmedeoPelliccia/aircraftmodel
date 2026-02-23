<<<<<<< HEAD
# OPT-IN Framework — AMPEL360-COMMON Shared Spine

The OPT-IN topology organises programme content along five axes:

| Axis | Directory | Scope |
|---|---|---|
| **O** | `O-ORGANIZATIONS/` | Stakeholder roles, RACI, org structure |
| **P** | `P-PROGRAMS/` | Programme plans, milestones, scheduling |
| **T** | `T-TECHNOLOGIES/` | ATA-chapter technical content |
| **I** | `I-INFRASTRUCTURES/` | Ground systems, tooling, facilities |
| **N** | `N-NEURAL_NETWORKS/` | AI/ML models, governance, ATA 96 policies |

## Shared Spine

Content under `OPT-IN_FRAMEWORK/` is the **AMPEL360-COMMON** shared spine,
consumed by both **AMPEL360 BWB** and **AMPEL360 WTW** repositories via Git
submodule.

Changes to shared content require PRs against AMPEL360-COMMON governed by
the IBCR (Inheritance Boundary Change Request) process — see
`N-NEURAL_NETWORKS/ATA_96/96-70-governance-policies-and-rules/`.
=======
# AMPEL360-COMMON

<p>
  <img src="https://img.shields.io/badge/Doc-IBD--001%20Rev%20B-1B3A5C" alt="Doc ID">
  <img src="https://img.shields.io/badge/Status-CONFIRMED-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/Framework-OPT--IN%20v1.1-purple" alt="Framework">
  <img src="https://img.shields.io/badge/Programmes-WTW%20%C3%97%20BWB-blue" alt="Programmes">
  <img src="https://img.shields.io/badge/Tokenomics-TT%20v3.14-gold" alt="TT">
  <img src="https://img.shields.io/badge/Governance-IBCR%20via%20ATA%2096--70-gray" alt="Governance">
</p>

<p>
  <strong>Shared engineering spine for the AMPEL360 programme family.</strong><br>
  All content in this repository is inherited by both
  <code>AMPEL360-WTW</code> (Wide Tube & Wing, EIS 2035–40) and
  <code>AMPEL360-BWB</code> (Quantum-Enhanced Blended Wing Body, EIS 2042–48).
</p>

---

## What This Repository Is

`AMPEL360-COMMON` is the **single authoritative source** for all OPT-IN content
classified as **SHARED** under `IBD-001 Rev B`. It is consumed by both programme
branches as a Git submodule (or monorepo path). No content in this repository
may be modified by a programme branch directly — all changes flow through Pull
Requests against `AMPEL360-COMMON` and are governed by the IBCR process.

```
AMPEL360-COMMON/           ← This repository (you are here)
├── O-ORGANIZATIONS/       ATA 00–05
├── P-PROGRAMS/            ATA 06–12
├── T-TECHNOLOGIES/
│   ├── A-AIRFRAME/        ATA 20, 51 (std practices + material library)
│   ├── M-MECHANICS/       ATA 29 (hydraulics — shared EHA architecture)
│   ├── E1-ENVIRONMENT/    ATA 21, 30, 36 (ECS, anti-ice, pneumatic)
│   ├── D-DATA/            ATA 31, 45 (indicating, CMS)
│   ├── A2-AVIONICS/       ATA 22, 34, 42 (comms, nav, IMA — shared core)
│   └── C1-COMMS/          ATA 23
├── I-INFRASTRUCTURES/
│   └── H2-COMMON/         IN-10–50 (green H₂ supply chain — shared)
└── N-NEURAL_NETWORKS/     ATA 96, 98 (traceability, DPP, tokenomics)
```

---

## What Is NOT Here

All **FORKED** and **MIXED** content lives in the programme-specific repos:

| Programme | Repo | Key Forks |
|---|---|---|
| **AMPEL360 WTW** | `AMPEL360-WTW` | ATA 28 (LH₂ + NH₃ tri-species), ATA 47 (N₂ inerting from cracker), ATA 52–57 (fuselage stretch), ATA 60–80 (turbine + open fan) |
| **AMPEL360 BWB** | `AMPEL360-BWB` | ATA 28 (LH₂ conformal tanks), ATA 47 (conventional OBIGGS), ATA 52–57 (BWB centerbody), ATA 60–80 (distributed electric), quantum design optimisation |

---

## Inheritance Boundary Reference

The boundary between SHARED and FORKED content is defined in:

> [`AMPEL360-FAM-IBD-001 Rev B`](../SSOT/LC04_TRADE_STUDIES/AMPEL360-FAM-IBD-001-RevB.md)

### Summary (23 entries)

| Designation | Count | Examples |
|---|---|---|
| **SHARED** | 12 | ATA 00–12, ATA 20/51, ATA 21/29/30, ATA 23/31/45, ATA 95–98 |
| **FORKED** | 8 | ATA 24/26/27/28/32/47/49, ATA 52–57, ATA 60–80 |
| **MIXED** | 3 | ATA 25/44/50 (cabin shared, layout forked), ATA 22/34/42 (core shared, FBW forked), Infrastructure (H₂ shared, NH₃ forked) |

---

## Change Control

Any reclassification of a boundary entry (SHARED ↔ FORKED) requires an
**Inheritance Boundary Change Request (IBCR)**:

1. Requestor submits IBCR to `N-NEURAL_NETWORKS/ATA_96/96-70-governance-policies-and-rules/`
2. Both programme CEs review
3. AMPEL360 Family PM approves
4. Boundary table in IBD-001 is updated

See [IBCR Register](N-NEURAL_NETWORKS/ATA_96/96-70-governance-policies-and-rules/README.md).

---

## Integration Pattern

```
programme-repo/
├── AMPEL360-COMMON/       ← Git submodule pointing here
│   ├── O-ORGANIZATIONS/
│   ├── P-PROGRAMS/
│   ├── T-TECHNOLOGIES/    (shared axes only)
│   ├── I-INFRASTRUCTURES/ (H₂ common)
│   └── N-NEURAL_NETWORKS/
├── T-TECHNOLOGIES/        ← Programme-specific FORKED content
│   ├── C2-CIRCULAR_CRYOGENIC_CELLS/  (WTW: ATA 28 tri-species)
│   ├── E1-ENVIRONMENT/               (WTW: ATA 47 cracker N₂)
│   └── P-PROPULSION/                 (WTW: ATA 75 open fan)
├── SSOT/
├── PUB/
└── ...
```

---

<p align="center">
  <strong>AMPEL360 WTW × AMPEL360 BWB</strong><br>
  <em>Two paths. One family. Reshaping the sky.</em>
</p>
<p align="center">
  <em>By Amedeo Pelliccia · AI-Assisted Engineering · aircraftmodel.eu</em>
</p>
>>>>>>> origin/main
