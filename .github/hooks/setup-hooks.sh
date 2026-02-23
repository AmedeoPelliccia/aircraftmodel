#!/usr/bin/env bash
# Configure Git to use project hooks directory.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

git config core.hooksPath "$SCRIPT_DIR"
chmod +x "$SCRIPT_DIR/pre-commit"

echo "Git hooks configured: core.hooksPath → $SCRIPT_DIR"
