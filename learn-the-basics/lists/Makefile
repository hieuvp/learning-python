export PATH := ../../venv/bin:$(PATH)

.PHONY: list
list:
	./list.sh &> list.console

.PHONY: list-exception
list-exception:
	./list_exception.sh &> list_exception.console || true

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: list list-exception exercise
