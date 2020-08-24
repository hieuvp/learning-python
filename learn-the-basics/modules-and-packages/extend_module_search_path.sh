#!/usr/bin/env bash

set -eou pipefail

set -x
python extend_module_search_path.py

set +x
echo

set -x
PYTHONPATH=".." python extend_module_search_path.py
