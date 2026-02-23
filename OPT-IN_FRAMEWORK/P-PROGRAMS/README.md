<<<<<<< HEAD
# P — Programs

Programme plans, milestones, and scheduling artefacts.

<!-- KNU-ATA00-00-002 -->
=======
# P-PROGRAMS — ATA 06–12

<p>
  <img src="https://img.shields.io/badge/OPT--IN%20Axis-P--PROGRAMS-blue" alt="Axis">
  <img src="https://img.shields.io/badge/IBD--001%20Rev%20B-SHARED-brightgreen" alt="SHARED">
  <img src="https://img.shields.io/badge/ATA-06--12-1B3A5C" alt="ATA">
</p>

> **Classification: SHARED** — Dimensions, servicing, ground handling, and
> parking/mooring are programme-agnostic. Common content applies to both
> AMPEL360 WTW and AMPEL360 BWB.

---

## Boundary Metadata

```yaml
- ata_id:       "ATA_06-12"
  title:        "Dimensions / Levelling / Towing / Servicing / Parking-Mooring"
  opt_in_axis:  "P-PROGRAMS"
  class:        SHARED
  cut_node:     false
  common_path:  "P-PROGRAMS/"
  wtw_path:     null
  bwb_path:     null
  rationale:    >
    Dimensions, servicing, ground handling, and parking/mooring are
    programme-agnostic. Common content applies to both WTW and BWB.
```

---

## Scope

| ATA Chapter | Title | Description |
|---|---|---|
| ATA 06 | Dimensions & Areas | Aircraft dimensions, station numbering |
| ATA 07 | Levelling & Weighing | Jacking, levelling, weighing procedures |
| ATA 08 | Levelling & Weighing (alt) | Extended weighing procedures |
| ATA 09 | Towing & Taxiing | Ground movement procedures |
| ATA 10 | Parking, Mooring, Storage & Return to Service | Ground handling |
| ATA 11 | Placards & Markings | Required external/internal markings |
| ATA 12 | Servicing — Routine Maintenance | Replenishing, servicing equipment |

---

## Inheritance Rule

Per [IBD-001 Rev B](../../SSOT/LC04_TRADE_STUDIES/AMPEL360-FAM-IBD-001-RevB.md) §7:

- This content is maintained **once** in `AMPEL360-COMMON`
- Both `AMPEL360-WTW` and `AMPEL360-BWB` inherit it via submodule
- No programme-specific forks permitted without an approved IBCR
- Changes require a PR against `AMPEL360-COMMON` reviewed by both programme CEs
>>>>>>> origin/main
