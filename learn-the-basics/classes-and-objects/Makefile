export PATH := ../../venv/bin:$(PATH)

.PHONY: class-and-object
class-and-object:
	./class_and_object.sh &> class_and_object.console

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
all: class-and-object access-object-variable access-object-function exercise
