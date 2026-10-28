#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHONPATH=src python -m gbt_bits_kit info
PYTHONPATH=src python -m gbt_bits_kit check --payload '{}'
PYTHONPATH=src python -m gbt_bits_kit run   --payload '{}'
