#!/usr/bin/env bash

set -eou pipefail

# shellcheck disable=SC1090
source "${HELPER_SCRIPT_PATH}/init.sh"

FILES=$(ls_files::by_extension "py")

readarray -t FILES < <(printf "%s" "$FILES")
declare -ra FILES

declare -ra IGNORING_FILES=(
  "learn-the-basics/conditions/boolean_operators.py"
  "learn-the-basics/conditions/in_operator.py"
  "learn-the-basics/conditions/not_operator.py"
)

main() {
  local -r file=$1

  flake8 \
    --config "${EXECUTION_PATH}/.flake8" \
    "$file"

  pylint \
    --rcfile "${EXECUTION_PATH}/.pylintrc" \
    --score no \
    "$file"
}

for file in "${FILES[@]}"; do
  if [[ " ${IGNORING_FILES[*]} " != *" ${file} "* ]] && is_processable "$file"; then
    main "$file"
  fi
done
