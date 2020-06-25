#!/usr/bin/env bash

set -eoux pipefail

black learn-the-basics/variables-and-types/exercise.py

# Options:
#   -c, --code TEXT                 Format the code passed in as a string.
#   -l, --line-length INTEGER       How many characters per line to allow.
#                                  [default: 88]
#
#   -t, --target-version [py27|py33|py34|py35|py36|py37|py38]
#                                  Python versions that should be supported by
#                                  Black's output. [default: per-file auto-
#                                  detection]
#
#   --py36                          Allow using Python 3.6-only syntax on all
#                                  input files.  This will put trailing commas
#                                  in function signatures and calls also after
#                                  *args and **kwargs. Deprecated; use
#                                  --target-version instead. [default: per-file
#                                  auto-detection]
#
#   --pyi                           Format all input files like typing stubs
#                                  regardless of file extension (useful when
#                                  piping source on standard input).
#
#   -S, --skip-string-normalization
#                                  Don't normalize string quotes or prefixes.
#   --check                         Don't write the files back, just return the
#                                  status.  Return code 0 means nothing would
#                                  change.  Return code 1 means some files
#                                  would be reformatted.  Return code 123 means
#                                  there was an internal error.
#
#   --diff                          Don't write the files back, just output a
#                                  diff for each file on stdout.
#
#   --config FILE                   Read configuration from PATH.
