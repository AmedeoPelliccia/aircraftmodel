# ICD-WTW-50-002 — Cargo Access Door Geometry & Latch/Hinge

**Delta:** DELTA-WTW-50-002  
**Programme:** AMPEL360 WTW  
**ATA:** 50-10 / 52 Cargo Compartments / Doors  
**Status:** TBD — thresholds gate LC03  
**Interfaces with:** ATA 52 cargo door structure, ATA 53 door-surround frames

---

## 1. Purpose

Defines WTW-specific cargo door clear-opening dimensions, sill height above
ground line, hinge pin coordinates and latch mechanism interface.

---

## 2. Door Geometry

| Parameter | FWD Hold Door | AFT Hold Door | Notes |
|---|---|---|---|
| Clear opening width (mm) | TBD (LC03) | TBD (LC03) | Inner face of door frame |
| Clear opening height (mm) | TBD (LC03) | TBD (LC03) | Sill to header |
| Sill height above ground (mm) | TBD (LC03) | TBD (LC03) | MTOW, nominal loading |
| Door type | Upward-opening plug | Upward-opening plug | |
| Actuation | Electro-hydraulic | Electro-hydraulic | Power source ref ATA 29 |

---

## 3. Hinge/Latch Interface Points

| Feature | Qty | Location ref | Load limit |
|---|---|---|---|
| Hinge pins (upper) | TBD | Frame station TBD | TBD |
| Latch fittings (lower) | TBD | Frame station TBD | TBD |
| Ground locking pin | 1 per door | Sill fitting | TBD |

---

## 4. WTW Delta Statement

> **ΔICD vs. SHARED baseline §4:**  
> WTW belly door configuration is an upward-opening plug type mounted in the
> lower fuselage. Sill height is constrained by circular fuselage belly
> geometry. SHARED baseline does not define WTW-specific door sill coordinates.

---

## 5. Open Actions

| Action ID | Description | Owner | Due |
|---|---|---|---|
| ACT-WTW-50-DOOR-001 | Finalise door clear-opening dimensions | Structures/Doors | LC03 |
| ACT-WTW-50-DOOR-002 | Define hinge pin and latch load limits | Loads | LC04 |
