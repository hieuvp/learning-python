#!/usr/bin/env bash

set -eoux pipefail

rm -rf venv
virtualenv venv

set +x
echo "+ source venv/bin/activate"
source venv/bin/activate

set -x
type python
type pip

pip install --upgrade pip
pip install --requirement requirements.txt

pip list
pip freeze
