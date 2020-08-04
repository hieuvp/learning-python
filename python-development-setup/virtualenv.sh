#!/usr/bin/env bash

set -eou pipefail

# Cleaning up
rm -rf venv

set -x
type python
type pip || true

virtualenv venv

set +x
echo "+ source venv/bin/activate"
source venv/bin/activate

set -x
type python
type pip

pip install --quiet --upgrade pip
pip list

pip install --quiet --requirement requirements.txt
pip freeze

rm -rf venv
