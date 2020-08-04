#!/usr/bin/env bash

set -eou pipefail

set -x
type python
type pip || true

rm -rf venv
virtualenv venv

set +x
echo "+ source venv/bin/activate"
source venv/bin/activate

set -x
type python
type pip

pip install --upgrade pip
pip list
pip install --requirement requirements.txt
pip freeze

rm -rf venv
