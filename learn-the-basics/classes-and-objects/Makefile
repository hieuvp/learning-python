export PATH := ../../venv/bin:$(PATH)

.PHONY: access-object-variable
access-object-variable:
	./access_object_variable.sh &> access_object_variable.console

.PHONY: access-object-function
access-object-function:
	./access_object_function.sh &> access_object_function.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: access-object-variable access-object-function exercise
