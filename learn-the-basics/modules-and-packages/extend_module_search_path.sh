#!/usr/bin/env bash

set -eoux pipefail

python extend_module_search_path.py

set +x
echo
set -x

# Enabling the Python script to load modules
# from ".." (meaning: "/learning-python/learn-the-basics") directory
PYTHONPATH=".." python extend_module_search_path.py
