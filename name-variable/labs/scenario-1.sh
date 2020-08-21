#!/usr/bin/env bash

set -eou pipefail

set -x
tree -a scenario-1

set +x

echo
set -x
python scenario-1/stand_alone_script.py
