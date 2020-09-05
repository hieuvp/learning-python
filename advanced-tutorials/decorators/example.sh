#!/usr/bin/env bash

set -eou pipefail

set -x
python example_with_decorator.py

set +x
echo

set -x
python example_without_decorator.py
