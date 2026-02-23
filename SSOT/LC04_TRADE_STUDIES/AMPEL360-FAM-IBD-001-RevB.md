# AMPEL360 Family — Inheritance Boundary Declaration

| Field | Value |
|---|---|
| **Doc ID** | AMPEL360-FAM-IBD-001 |
| **Rev** | B |
| **Status** | CONFIRMED |
| **Date** | 2026-02-22 |

## Purpose

This document declares which ATA-chapter content is **SHARED** (common spine)
versus **FORKED** (variant-specific) between the two AMPEL360 sibling
programmes:

- **AMPEL360 BWB** — Blended Wing Body, LH₂-only, fuel-cell propulsion
- **AMPEL360 WTW** — Wide Tube & Wing, tri-species LH₂/NH₃/LN₂

## Boundary Table

| ATA | Chapter | Boundary | Notes |
|---|---|---|---|
| 20 | Standard Practices | SHARED | Material library common |
| 21 | ECS | SHARED | Thermal architecture shared |
| 24 | Electrical | SHARED | Power bus topology common |
| 25 | Equipment / Furnishings | FORKED | NH₃ containment (WTW only) |
| 26 | Fire Protection | SHARED | H₂ leak detection common |
| 28 | **C² CELL (Fuel)** | **FORKED** | **Critical-path fork** — reservoir geometry, PM species, recirculation differ |
| 32 | Landing Gear | FORKED | Weight envelope differs |
| 47 | Inert Gas / Fuel Cell | SHARED | Stack architecture common |
| 51 | Structures | SHARED | Cryo-structural interface common |
| 53 | Fuselage | FORKED | Centre-body (BWB) vs tube (WTW) |
| 55 | Stabilisers | FORKED | CG management differs |
| 96 | Governance | SHARED | IBCR process common |

## Open Items (LC04)

| KNOT ID | Topic | Status |
|---|---|---|
| KNOT-ATA28-10-00-001 | LH₂ reservoir conformal vs cylindrical | OPEN |
| KNOT-ATA28-20-00-001 | NH₃ distribution double-containment | OPEN |
