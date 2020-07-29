export PATH := ../../venv/bin:$(PATH)

.PHONY: for-loop
for-loop:
	./for_loop.sh &> for_loop.console

.PHONY: for-range-loops
for-range-loops:
	./for_range_loops.sh &> for_range_loops.console

.PHONY: while-loop
while-loop:
	./while_loop.sh &> while_loop.console

.PHONY: break-continue-statements
break-continue-statements:
	./break_continue_statements.sh &> break_continue_statements.console

.PHONY: else-clause
else-clause:
	./else_clause.sh &> else_clause.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: for-loop for-range-loops while-loop break-continue-statements else-clause exercise
