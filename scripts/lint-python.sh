#!/usr/bin/env bash

set -eou pipefail

# shellcheck disable=SC1090
source "${HELPER_SCRIPT_PATH}/init.sh"

FILES=$(ls_files::by_extension "py")

readarray -t FILES < <(printf "%s" "$FILES")
declare -ra FILES

declare -ra IGNORING_FILES=(
  "advanced-tutorials/exception-handling/example.py"
  "advanced-tutorials/exception-handling/exception.py"
  "advanced-tutorials/exception-handling/exercise.py"
  "advanced-tutorials/generators/exercise.py"
  "advanced-tutorials/generators/generator_function.py"
  "advanced-tutorials/generators/lottery.py"
  "advanced-tutorials/map-filter-reduce/map_pets.py"
  "advanced-tutorials/map-filter-reduce/sum.py"
  "advanced-tutorials/map-filter-reduce/sum_with_initial.py"
  "advanced-tutorials/multiple-function-arguments/exercise.py"
  "advanced-tutorials/multiple-function-arguments/kwargs.py"
  "advanced-tutorials/partial-functions/exercise.py"
  "advanced-tutorials/partial-functions/multiply.py"
  "advanced-tutorials/regular-expressions/example.py"
  "advanced-tutorials/regular-expressions/search.py"
  "advanced-tutorials/serialization/exercise.py"
  "advanced-tutorials/sets/words.py"
  "data-science/pandas-basics/index_dataframe.py"
  "lambda-functions/add.py"
  "lambda-functions/double.py"
  "lambda-functions/functions.py"
  "lambda-functions/multiply.py"
  "lambda-functions/sum.py"
  "learn-the-basics/conditions/boolean_operators.py"
  "learn-the-basics/conditions/in_operator.py"
  "learn-the-basics/conditions/not_operator.py"
  "learn-the-basics/functions/call_functions.py"
  "learn-the-basics/functions/write_functions.py"
  "learn-the-basics/loops/break_continue_statements.py"
  "learn-the-basics/loops/else_clause.py"
  "learn-the-basics/loops/for_range_loops.py"
  "learn-the-basics/loops/while_loop.py"
  "learn-the-basics/modules-and-packages/import_all_module_objects/game.py"
  "learn-the-basics/modules-and-packages/initialize_module/draw.py"
  "pass-statement/example.py"
  "pass-statement/if.py"
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
