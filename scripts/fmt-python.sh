#!/usr/bin/env bash

set -eou pipefail

# shellcheck disable=SC1090
source "${HELPER_SCRIPT_PATH}/init.sh"

FILES=$(ls_files::by_extension "py")

readarray -t FILES < <(printf "%s" "$FILES")
declare -ra FILES

main() {
  local -r file=$1

  options=(
    # Do not emit non-error messages to stderr, errors are still emitted
    --quiet

    # How many characters per line to allow
    --line-length 96
  )

  black "${options[@]}" "$file"
}

for file in "${FILES[@]}"; do
  if is_processable "$file"; then
    main "$file"
  fi
done
