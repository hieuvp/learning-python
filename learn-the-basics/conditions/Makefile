export PATH := ../../venv/bin:$(PATH)

.PHONY: boolean-expression
boolean-expression:
	./boolean_expression.sh &> boolean_expression.console

.PHONY: boolean-operators
boolean-operators:
	./boolean_operators.sh &> boolean_operators.console

.PHONY: in-operator
in-operator:
	./in_operator.sh &> in_operator.console

.PHONY: if-statement
if-statement:
	./if_statement.sh &> if_statement.console

.PHONY: is-operator
is-operator:
	./is_operator.sh &> is_operator.console

.PHONY: not-operator
not-operator:
	./not_operator.sh &> not_operator.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: boolean-expression boolean-operators in-operator if-statement is-operator not-operator exercise
