export PATH := ../../venv/bin:$(PATH)

.PHONY: create-class-and-object
create-class-and-object:
	./create_class_and_object.sh

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
all: create-class-and-object access-object-variable access-object-function exercise
