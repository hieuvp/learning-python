#!/usr/bin/env bash

set -eou pipefail

set -x
tree -a -I __pycache__ my_game

set +x

echo
set -x
python my_game/game.py
