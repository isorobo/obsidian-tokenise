#!/usr/bin/env bash
# wiki-vault graph launcher (macOS / Linux).
# Forwards to serve.py - the cross-platform launcher.
set -euo pipefail
cd "$(dirname "$0")"
exec python3 serve.py "$@"
