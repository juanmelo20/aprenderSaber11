#!/usr/bin/env bash
# Recarga los datos de demostración y corre el recorrido en el navegador.
set -euo pipefail
cd "$(dirname "$0")/.."
export FIRESTORE_EMULATOR_HOST=127.0.0.1:8080 FIREBASE_AUTH_EMULATOR_HOST=127.0.0.1:9099
PY=backend/.venv/bin/python; [ -x "$PY" ] || PY=python3
LINK=$(cd backend && "../$PY" -m scripts.dev_seed 2>/dev/null | tail -1 | tr -d ' ')
python3 e2e/recorrido.py "${1:-/tmp/shots}" "$LINK"
