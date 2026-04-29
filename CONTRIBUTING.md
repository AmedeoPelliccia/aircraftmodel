# Contributing to ID-A360-Q100

## Contributor Loop

```
1. CLAIM  → Assign a KNU ID from SSOT/LC01_PROBLEM_STATEMENT/KNU_PLAN.csv
2. DRAFT  → Develop engineering artifact in SSOT/LCxx/ — include KNU ID in header
3. PUB    → Author S1000D DM in PUB/CSDB/DM/ if KNU_TYPE = PUB (BREX-validated)
4. TRACE  → Pre-commit hook enforces KNU ID presence in LC02–LC14 artifacts
5. PR     → Include KNU ID in PR title/body → CI auto-awards TT on merge
```

## Placement Rules

| Artifact is... | Place in... |
|---|---|
| Authoritative engineering evidence | `SSOT/` |
| Publishable or deliverable | `PUB/` |
| Formatted output (PDF, HTML, DOCX) | `PUB/EXPORT/` — **never** `SSOT/` |
| GEN-MODEL mode configs (observer/delineant) | `.askm/` — YAML configs |
| Agent registrations & enforcement rules | `.asit/` — agent bindings, operator rules |

## Format Rules

| Rule | Guidance |
|---|---|
| Narrative docs | `.md` only — never `.pdf` or `.docx` |
| Matrices / logs | `.csv` only — never `.xlsx` |
| Material data | Reference `material-library/` — no local definitions |
| Safety-critical DMs | `safetyClass="SC1"` + DO-178C/254 compliance tag |
| LH₂ DMs | `<cautionRef>` to H₂ caution (BREX-IDA360-001) |
| NH₃ DMs | `<warningRef>` to NH₃ warning (BREX-IDA360-002) |
| KNOT / KNU | Define uncertainty in LC01 **before** producing any artifact |

## Setup

```bash
pip install -r requirements.txt
bash .github/hooks/setup-hooks.sh
```

## Pre-Commit Hook

The hook rejects at commit time:

- `.pdf`, `.html`, `.docx` anywhere in `SSOT/`
- Raw `.csv` inside `PUB/CSDB/DM/`
- LC02–LC14 artifacts (> 5 lines) with no KNU ID reference

## Validation Commands

```bash
# Structure validation
python tools/ci/optin_structure_validator.py --check

# BREX validation
python tools/ci/brex_validator.py --dm-dir PUB/CSDB/DM

# TT tooling
python tools/knu_distribution.py quote --op reward --tt 200
python tools/knu_distribution.py verify
```

## License

Creative Commons Zero v1.0 Universal — see [LICENSE](./LICENSE).
