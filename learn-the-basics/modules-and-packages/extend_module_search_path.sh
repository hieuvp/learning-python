#!/usr/bin/env bash

set -eoux pipefail

python extend_module_search_path.py

set +x
echo
set -x

# Enable this script to load modules
# from ".." (means "./learning-python/learn-the-basics") directory
# as well as the local directory
PYTHONPATH=".." python extend_module_search_path.py
