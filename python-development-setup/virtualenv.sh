#!/usr/bin/env bash

set -eoux pipefail

type python
type pip || true

rm -rf venv
virtualenv venv
source venv/bin/activate

type python
type pip

pip install --requirement requirements.txt
pip list
