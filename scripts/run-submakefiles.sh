#!/usr/bin/env bash

args=("$@")
set -eou pipefail

readonly TARGET_NAME="${args[0]}"

readarray -t MAKEFILES < <(find . -name "Makefile")
declare -ra MAKEFILES

main() {
  local -r file=$1
  local -r dirname="$(dirname "$file")"

  echo

  (
    set -x
    cd "$dirname"
    make "$TARGET_NAME"
  )
}

for file in "${MAKEFILES[@]}"; do
  if [[ $file != "./Makefile" ]]; then
    main "$file"
  fi
done
