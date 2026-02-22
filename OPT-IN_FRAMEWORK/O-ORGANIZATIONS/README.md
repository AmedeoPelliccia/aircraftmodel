# O-ORGANIZATIONS — ATA 00–05

<p>
  <img src="https://img.shields.io/badge/OPT--IN%20Axis-O--ORGANIZATIONS-blue" alt="Axis">
  <img src="https://img.shields.io/badge/IBD--001%20Rev%20B-SHARED-brightgreen" alt="SHARED">
  <img src="https://img.shields.io/badge/ATA-00--05-1B3A5C" alt="ATA">
</p>

> **Classification: SHARED** — Governance, maintenance policy, airworthiness
> limitations, and time limits are programme-agnostic. Identical content applies
> to both AMPEL360 WTW and AMPEL360 BWB.

---

## Boundary Metadata

```yaml
- ata_id:       "ATA_00-05"
  title:        "General / Maintenance Policy / Airworthiness Limitations / Time Limits"
  opt_in_axis:  "O-ORGANIZATIONS"
  class:        SHARED
  cut_node:     false
  common_path:  "O-ORGANIZATIONS/"
  wtw_path:     null
  bwb_path:     null
  rationale:    >
    Governance, maintenance policy, airworthiness limitations, and time limits
    are programme-agnostic. Identical content applies to both WTW and BWB.
```

---

## Scope

| ATA Chapter | Title | Description |
|---|---|---|
| ATA 00 | General | Introduction, glossary, abbreviations |
| ATA 01 | Maintenance Policy | Maintenance programme requirements |
| ATA 02 | Weight & Balance | Mass properties (shared reference frame) |
| ATA 03 | Minimum Equipment | MEL / CDL definitions |
| ATA 04 | Airworthiness Limitations | ALIs, CMRs, safe-life items |
| ATA 05 | Time Limits / Maintenance Checks | Scheduled maintenance intervals |

---

## Inheritance Rule

Per [IBD-001 Rev B](../../SSOT/LC04_TRADE_STUDIES/AMPEL360-FAM-IBD-001-RevB.md) §7:

- This content is maintained **once** in `AMPEL360-COMMON`
- Both `AMPEL360-WTW` and `AMPEL360-BWB` inherit it via submodule
- No programme-specific forks permitted without an approved IBCR
- Changes require a PR against `AMPEL360-COMMON` reviewed by both programme CEs

---

## Related KNOTs

| KNOT ID | Title | Relevance |
|---|---|---|
| KNOT-ATA04-00-00-001 | ALIs for Cryo Systems | ATA 04 airworthiness limitations for LH₂/NH₃ cryo components |
