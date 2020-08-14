#!/usr/bin/env bash

set -eou pipefail

# shellcheck disable=SC1090
source "${HELPER_SCRIPT_PATH}/init.sh"

FILES=$(ls_files::by_extension "py")

readarray -t FILES < <(printf "%s" "$FILES")
declare -ra FILES

declare -ra IGNORING_FILES=(
  "learn-the-basics/classes-and-objects/access_object_function.py"
  "learn-the-basics/classes-and-objects/access_object_variable.py"
  "learn-the-basics/classes-and-objects/create_class_and_object.py"
  "learn-the-basics/classes-and-objects/exercise.py"
  "learn-the-basics/conditions/boolean_operators.py"
  "learn-the-basics/conditions/in_operator.py"
  "learn-the-basics/conditions/not_operator.py"
  "learn-the-basics/functions/call_functions.py"
  "learn-the-basics/functions/exercise.py"
  "learn-the-basics/functions/write_functions.py"
  "learn-the-basics/loops/break_continue_statements.py"
  "learn-the-basics/loops/else_clause.py"
  "learn-the-basics/loops/for_range_loops.py"
  "learn-the-basics/loops/while_loop.py"
  "learn-the-basics/modules-and-packages/custom_import_name/draw.py"
  "learn-the-basics/modules-and-packages/import_all_module_objects/draw.py"
  "learn-the-basics/modules-and-packages/import_all_module_objects/game.py"
  "learn-the-basics/modules-and-packages/import_module_objects/draw.py"
  "learn-the-basics/modules-and-packages/module_initialization/draw.py"
  "learn-the-basics/modules-and-packages/my_game/draw.py"
  "learn-the-basics/modules-and-packages/my_game/game.py"
  "learn-the-basics/modules-and-packages/write_packages/__init__.py"
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
