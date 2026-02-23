<<<<<<< HEAD
# Contributing to AMPEL360 WTW

## KNU-Based Contributor Loop

1. Pick a **KNU** (Knowledge Need Unit) from `SSOT/LC01_PROBLEM_STATEMENT/KNU_PLAN.csv`
2. Create a branch: `knu/<KNU-ID>`
3. Produce evidence (analysis, test, model) — place in `SSOT/`
4. Produce deliverables (S1000D DM, export) — place in `PUB/`
5. Reference the **KNU ID** in every artifact longer than 5 lines (enforced by pre-commit hook)
6. Open a PR; CI validates structure, BREX, and KNU traceability

## Placement Rules

| Content Type | Directory | Format |
|---|---|---|
| Authoritative engineering evidence | `SSOT/` | Markdown, YAML, CSV, XML — **no binaries** |
| S1000D data modules | `PUB/CSDB/DM/` | XML |
| BREX rules | `PUB/CSDB/BREX/` | XML |
| Formatted deliverables | `PUB/EXPORT/` | PDF, HTML, DOCX |

## Pre-Commit Hook

Run `.github/hooks/setup-hooks.sh` once after cloning:

```bash
bash .github/hooks/setup-hooks.sh
```

The hook enforces:
- No binaries (.pdf, .html, .docx, .xlsx) in `SSOT/`
- KNU ID reference in LC02–LC14 artifacts longer than 5 lines
=======
# Contributing to ID-A360-Q100

## Contributor Loop

```
1. CLAIM  → Assign a KNU ID from SSOT/LC01_PROBLEM_STATEMENT/KNU_PLAN.csv
2. DRAFT  → Develop engineering artifact in SSOT/LCxx/ — include KNU ID in header
3. PUB    → Author S1000D DM in PUB/CSDB/DM/ if KNU_Type = PUB (BREX-validated)
4. TRACE  → Pre-commit hook enforces KNU ID presence in LC02–LC14 artifacts
5. PR     → Include KNU ID in PR title/body → CI auto-awards TT on merge
```

## Placement Rules

| Artifact is... | Place in... |
|---|---|
| Authoritative engineering evidence | `SSOT/` |
| Publishable or deliverable | `PUB/` |
| Formatted output (PDF, HTML, DOCX) | `PUB/EXPORT/` — **never** `SSOT/` |

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
>>>>>>> origin/main

## Validation Commands

```bash
<<<<<<< HEAD
python tools/ci/optin_structure_validator.py --check
python tools/ci/brex_validator.py --dm-dir PUB/CSDB/DM
python tools/knu_distribution.py verify
```
=======
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
>>>>>>> origin/main
