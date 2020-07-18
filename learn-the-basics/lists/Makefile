export PATH := ../../venv/bin:$(PATH)

.PHONY: list
list:
	./list.sh &> list.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: list exercise
