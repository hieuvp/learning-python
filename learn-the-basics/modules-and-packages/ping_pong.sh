#!/usr/bin/env bash

set -eou pipefail

set -x
tree -a ping_pong

set +x

echo
set -x
python ping_pong/game.py
