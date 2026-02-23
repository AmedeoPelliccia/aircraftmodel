#!/usr/bin/env python3
<<<<<<< HEAD
"""Teknia Token (TT) distribution and ledger management.

Implements the effort+impact allocation formula and SHA-256 hash-chain
verification for the TT ledger.

Usage:
    python tools/knu_distribution.py verify
    python tools/knu_distribution.py quote --amount 100 --op transfer
=======
"""Teknia Token (TT) distribution calculator and ledger manager.

Implements the effort + impact weighted distribution formula:
    w_i = alpha * E_hat_i + (1 - alpha) * I_hat_i
    T_i = P_k * w_i

Usage:
    python tools/knu_distribution.py quote --op reward --tt 200
    python tools/knu_distribution.py verify
>>>>>>> origin/main
"""

import argparse
import hashlib
import json
import os
import sys
<<<<<<< HEAD

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LEDGER_PATH = os.path.join(REPO_ROOT, "finance", "ledger.json")

# Default allocation parameters (overridden by TOKENOMICS_TT.yaml)
ALPHA = 0.30  # 30 % effort, 70 % impact
LAMBDA_SPILLOVER = 0.15

FEE_RATES = {
    "transfer": 0.005,
    "conversion": 0.010,
    "governance_vote": 0.000,
=======
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER_PATH = os.path.join(REPO_ROOT, "finance", "ledger.json")

# Default parameters from TOKENOMICS_TT.yaml
ALPHA = 0.30
LAMBDA_SPILLOVER = 0.50
FEE_RATES = {
    "reward": 0.005,
    "transfer_pi": 0.00314,
    "transfer_standard": 0.0099,
    "transfer_large": 0.0314,
>>>>>>> origin/main
}


def compute_fee(amount, op_type):
<<<<<<< HEAD
    """Compute fee for a given operation."""
    rate = FEE_RATES.get(op_type, 0.0)
    return round(amount * rate, 4)


def quote(amount, op_type):
    """Quote fee and net amount for an operation."""
    fee = compute_fee(amount, op_type)
    return {"gross": amount, "fee": fee, "net": round(amount - fee, 4), "op": op_type}
=======
    """Compute fee for a given operation type."""
    rate = FEE_RATES.get(op_type, FEE_RATES["transfer_standard"])
    return round(amount * rate, 6)


def quote(amount, op_type):
    """Quote the fee and net amount for an operation."""
    fee = compute_fee(amount, op_type)
    net = round(amount - fee, 6)
    return {"gross": amount, "fee": fee, "net": net, "rate": FEE_RATES.get(op_type, 0)}
>>>>>>> origin/main


def compute_hash(entry, prev_hash):
    """Compute SHA-256 hash for a ledger entry."""
    payload = json.dumps(entry, sort_keys=True) + prev_hash
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def load_ledger():
<<<<<<< HEAD
    """Load the TT ledger."""
    if not os.path.isfile(LEDGER_PATH):
        return {"version": "1.0", "entries": [], "hash_chain": []}
=======
    """Load the ledger from disk."""
    if not os.path.isfile(LEDGER_PATH):
        return {"entries": [], "last_hash": "0" * 64}
>>>>>>> origin/main
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_ledger(ledger):
<<<<<<< HEAD
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
=======
    """Save the ledger to disk."""
    os.makedirs(os.path.dirname(LEDGER_PATH), exist_ok=True)
    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")


def verify_ledger():
    """Verify the integrity of the hash chain."""
    ledger = load_ledger()
    entries = ledger.get("entries", [])
    if not entries:
        print("✅ Ledger is empty — nothing to verify")
        return True

    prev_hash = "0" * 64
    for i, entry in enumerate(entries):
        stored_hash = entry.get("hash", "")
        entry_data = {k: v for k, v in entry.items() if k != "hash"}
        expected = compute_hash(entry_data, prev_hash)
        if stored_hash != expected:
            print(f"❌ Hash mismatch at entry {i}: expected {expected[:16]}..., got {stored_hash[:16]}...")
            return False
        prev_hash = stored_hash

    if prev_hash != ledger.get("last_hash", ""):
        print("❌ last_hash does not match final entry hash")
        return False

    print(f"✅ Ledger verified — {len(entries)} entries, chain intact")
>>>>>>> origin/main
    return True


def main():
<<<<<<< HEAD
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
=======
    parser = argparse.ArgumentParser(description="TT distribution calculator")
    subparsers = parser.add_subparsers(dest="command")

    quote_parser = subparsers.add_parser("quote", help="Quote fee for an operation")
    quote_parser.add_argument("--op", required=True, choices=list(FEE_RATES.keys()))
    quote_parser.add_argument("--tt", required=True, type=float, help="TT amount")

    subparsers.add_parser("verify", help="Verify ledger hash chain")

    args = parser.parse_args()

    if args.command == "quote":
        result = quote(args.tt, args.op)
        print(f"Operation: {args.op}")
        print(f"  Gross:  {result['gross']:.6f} TT")
        print(f"  Fee:    {result['fee']:.6f} TT ({result['rate']*100:.3f}%)")
        print(f"  Net:    {result['net']:.6f} TT")
    elif args.command == "verify":
        ok = verify_ledger()
        sys.exit(0 if ok else 1)
    else:
        parser.print_help()
        sys.exit(1)
>>>>>>> origin/main


if __name__ == "__main__":
    main()
