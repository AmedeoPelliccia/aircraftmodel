# `.asit/` — Agent & Operator Enforcement Registry

## Purpose

This directory defines the agent registration and operator enforcement
layer for the GEN-MODEL governance system.

| Directory              | Function                                    |
|------------------------|---------------------------------------------|
| `.asit/agents/`        | Agent registrations with mode bindings      |
| `.asit/operator/`      | Cross-mode enforcement rules and procedures |

## Relationship to `.askm/`

`.askm/` defines **what** each mode can do (observer / delineant configs).
`.asit/` defines **who** executes in each mode and **how** enforcement
is applied.

```
.askm/  ←  Mode definitions (capabilities, invariants, gates)
  │
  └──→  .asit/agents/  ←  Agent-to-mode bindings
         .asit/operator/  ←  Cross-mode enforcement rules
```

## Formal Specification

See: `SSOT/LC05_ANALYSIS_MODELS/LC05-GEN-MODEL-ROLE-SPEC.md`
(KNU-ATA96-70-001)

## Traceability

- KNOT: `KNOT-ATA96-70-00-001`
- KNU: `KNU-ATA96-70-001`
- Programme: ID-A360-Q100 · AMPEL360
