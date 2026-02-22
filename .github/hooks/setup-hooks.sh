#!/usr/bin/env bash
# Setup Git hooks for ID-A360-Q100
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
HOOKS_DIR="$REPO_ROOT/.github/hooks"

echo "Setting up Git hooks for ID-A360-Q100..."

# Configure Git to use our hooks directory
git config core.hooksPath "$HOOKS_DIR"

# Ensure hooks are executable
chmod +x "$HOOKS_DIR/pre-commit"

echo "✅ Git hooks configured — using $HOOKS_DIR"
