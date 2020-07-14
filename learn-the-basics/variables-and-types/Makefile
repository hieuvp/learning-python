export PATH := ../../venv/bin:$(PATH)

.PHONY: integer
integer:
	./integer.sh &> integer.console

.PHONY: float
float:
	./float.sh &> float.console

.PHONY: string
string:
	./string.sh &> string.console

.PHONY: simple-operators
simple-operators:
	./simple_operators.sh &> simple_operators.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: integer float string simple-operators exercise
