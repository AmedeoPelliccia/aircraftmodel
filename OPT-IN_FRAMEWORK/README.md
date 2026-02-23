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
