#!/usr/bin/env python3
"""Teknia Token (TT) distribution and ledger management.

Implements the effort+impact allocation formula and SHA-256 hash-chain
verification for the TT ledger.

Usage:
    python tools/knu_distribution.py verify
    python tools/knu_distribution.py quote --amount 100 --op transfer
"""

import argparse
import hashlib
import json
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LEDGER_PATH = os.path.join(REPO_ROOT, "finance", "ledger.json")

# Default allocation parameters (overridden by TOKENOMICS_TT.yaml)
ALPHA = 0.30  # 30 % effort, 70 % impact
LAMBDA_SPILLOVER = 0.15

FEE_RATES = {
    "transfer": 0.005,
    "conversion": 0.010,
    "governance_vote": 0.000,
}


def compute_fee(amount, op_type):
    """Compute fee for a given operation."""
    rate = FEE_RATES.get(op_type, 0.0)
    return round(amount * rate, 4)


def quote(amount, op_type):
    """Quote fee and net amount for an operation."""
    fee = compute_fee(amount, op_type)
    return {"gross": amount, "fee": fee, "net": round(amount - fee, 4), "op": op_type}


def compute_hash(entry, prev_hash):
    """Compute SHA-256 hash for a ledger entry."""
    payload = json.dumps(entry, sort_keys=True) + prev_hash
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def load_ledger():
    """Load the TT ledger."""
    if not os.path.isfile(LEDGER_PATH):
        return {"version": "1.0", "entries": [], "hash_chain": []}
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_ledger(ledger):
    """Save the TT ledger."""
    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


def verify_ledger():
    """Verify the hash chain integrity of the ledger."""
    ledger = load_ledger()
    entries = ledger.get("entries", [])
    chain = ledger.get("hash_chain", [])

    if len(entries) != len(chain):
        print(f"FAIL — entry count ({len(entries)}) != chain count ({len(chain)})")
        return False

    if not entries:
        print("PASS — ledger is empty (no entries to verify)")
        return True

    prev_hash = ""
    for i, (entry, expected_hash) in enumerate(zip(entries, chain)):
        actual = compute_hash(entry, prev_hash)
        if actual != expected_hash:
            print(f"FAIL — hash mismatch at entry {i}")
            return False
        prev_hash = actual

    print(f"PASS — {len(entries)} entry/entries verified")
    return True


def main():
    parser = argparse.ArgumentParser(description="TT distribution & ledger tool")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("verify", help="Verify ledger hash-chain integrity")

    quote_parser = sub.add_parser("quote", help="Quote fee for an operation")
    quote_parser.add_argument("--amount", type=float, required=True)
    quote_parser.add_argument("--op", required=True, choices=list(FEE_RATES.keys()))

    args = parser.parse_args()

    if args.command == "verify":
        ok = verify_ledger()
        sys.exit(0 if ok else 1)
    elif args.command == "quote":
        result = quote(args.amount, args.op)
        print(json.dumps(result, indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
