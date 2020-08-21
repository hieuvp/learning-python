#!/usr/bin/env bash

set -eou pipefail

set -x
tree -a scenario-2

set +x

echo
set -x
python scenario-2/importing_script.py
