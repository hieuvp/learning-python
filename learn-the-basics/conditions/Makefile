export PATH := ../../venv/bin:$(PATH)

.PHONY: boolean-operators
boolean-operators:
	./boolean_operators.sh &> boolean_operators.console

.PHONY: in-operator
in-operator:
	./in_operator.sh &> in_operator.console

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
all: boolean-operators in-operator is-operator not-operator exercise
