#!/usr/bin/env bash

set -eoux pipefail

tree -a -I __pycache__ my_game

python my_game/game.py
