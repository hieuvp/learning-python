#!/usr/bin/env bash

set -eou pipefail

# shellcheck disable=SC1090
source "${HELPER_SCRIPT_PATH}/init.sh"

FILES=$(ls_files::by_extension "py")

readarray -t FILES < <(printf "%s" "$FILES")
declare -ra FILES

declare -ra IGNORING_FILES=(
  "learn-the-basics/variables-and-types/string.py"
)

main() {
  local -r file=$1

  local -ra options=(
    --quiet          # Do not emit non-error messages to stderr, errors are still emitted
    --line-length 96 # How many characters per line to allow
  )

  black "${options[@]}" "$file"
}

for file in "${FILES[@]}"; do
  if [[ " ${IGNORING_FILES[*]} " != *" ${file} "* ]] && is_processable "$file"; then
    main "$file"
  fi
done
