#!/usr/bin/env bash

set -eou pipefail

readarray -t MAKEFILES < <(find . -name "Makefile")
declare -ra MAKEFILES

main() {
  local -r file=$1
  local -r dirname="$(dirname "$file")"

  echo

  (
    set -x
    cd "$dirname"
    make all
  )
}

for file in "${MAKEFILES[@]}"; do
  if [[ $file != "./Makefile" ]]; then
    main "$file"
  fi
done
