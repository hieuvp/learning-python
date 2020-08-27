#!/usr/bin/env bash

set -eou pipefail

set -x
tree -a -I "*.pyc" scenario-1

set +x

echo
set -x
python scenario-1/standalone_script.py
