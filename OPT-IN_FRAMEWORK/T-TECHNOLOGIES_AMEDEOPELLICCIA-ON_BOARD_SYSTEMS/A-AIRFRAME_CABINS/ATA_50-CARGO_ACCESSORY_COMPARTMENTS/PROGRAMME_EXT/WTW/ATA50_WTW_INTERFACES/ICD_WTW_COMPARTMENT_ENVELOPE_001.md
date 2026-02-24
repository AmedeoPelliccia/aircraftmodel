# ICD-WTW-50-001 — Cargo Compartment Envelope (Circular Fuselage)

**Delta:** DELTA-WTW-50-001  
**Programme:** AMPEL360 WTW  
**ATA:** 50-10 Cargo Compartments  
**Status:** TBD — thresholds gate LC03  
**Interfaces with:** ATA 53 fuselage frames, ATA 25 cargo floor assembly

---

## 1. Purpose

Defines the WTW-specific available envelope for the forward (FWD) and aft (AFT)
belly-hold cargo compartments, arising from the circular fuselage cross-section.
The BWB planform baseline uses a flat-floor wide-body bay; this ICD captures the
WTW departure.

---

## 2. Envelope Parameters

| Parameter | FWD Hold | AFT Hold | Notes |
|---|---|---|---|
| Usable width at floor (mm) | TBD (LC03) | TBD (LC03) | At nominal floor level |
| Usable height (mm) | TBD (LC03) | TBD (LC03) | Floor to crown arc |
| Usable length (mm) | TBD (LC03) | TBD (LC03) | Structural bay limit |
| Floor-to-keel offset (mm) | TBD (LC03) | TBD (LC03) | Drain/keel clearance |
| Contour radius (mm) | TBD (LC03) | — | Fuselage inner radius |

---

## 3. Structural Boundary Interfaces

| Interface | ATA ref | Note |
|---|---|---|
| Fwd pressure bulkhead | ATA 53 | FWD hold forward limit |
| Aft pressure bulkhead | ATA 53 | AFT hold aft limit |
| Wing carry-through | ATA 57/53 | Discontinuity frame at centre section |
| Keel beam | ATA 53 | Floor attachment reference |

---

## 4. WTW Delta Statement

> **ΔICD vs. SHARED baseline §3:**  
> Circular fuselage imposes a width-at-floor limit narrower than BWB flat-floor
> baseline. Width is governed by the inner mould line at floor beam level.
> Curved contour requires curved liner panels — flat panels from SHARED spec
> inapplicable. See `ATA50_WTW_INTERFACES/ICD_WTW_LINER_ATTACHMENTS_001.md`.

---

## 5. Open Actions

| Action ID | Description | Owner | Due |
|---|---|---|---|
| ACT-WTW-50-ENV-001 | Define FWD/AFT usable envelope (mm) at LC03 | Structures | LC03 |
| ACT-WTW-50-ENV-002 | Confirm keel-to-floor offset for drain routing | Systems | LC03 |
