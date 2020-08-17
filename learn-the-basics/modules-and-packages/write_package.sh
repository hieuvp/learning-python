#!/usr/bin/env bash

set -eou pipefail

set -x
tree -a -I __pycache__ write_package

set +x

echo
set -x
python write_package/ping_pong.py
