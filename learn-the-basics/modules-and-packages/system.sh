#!/usr/bin/env bash

set -eou pipefail

set -x
python system.py

set +x
echo

set -x
PYTHONPATH=".." python system.py
