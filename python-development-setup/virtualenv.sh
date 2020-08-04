#!/usr/bin/env bash

set -eou pipefail

<<<<<<< HEAD
=======
# Cleaning up
rm -rf venv

>>>>>>> master
set -x
type python
type pip || true

<<<<<<< HEAD
rm -rf venv
=======
>>>>>>> master
virtualenv venv

set +x
echo "+ source venv/bin/activate"
source venv/bin/activate

set -x
type python
type pip

<<<<<<< HEAD
pip list
pip install --requirement requirements.txt
=======
pip install --quiet --upgrade pip
pip list
pip freeze

pip install --quiet --requirement requirements.txt
pip list
>>>>>>> master
pip freeze

rm -rf venv
