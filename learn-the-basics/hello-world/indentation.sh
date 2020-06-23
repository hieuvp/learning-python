#!/usr/bin/env bash

set -eou pipefail

export PATH="../../venv/bin:${PATH}"

set -x

type python

python indentation.py
