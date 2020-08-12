export PATH := ../../venv/bin:$(PATH)

.PHONY: dictionary
dictionary:
	./dictionary.sh &> dictionary.console

.PHONY: iteration
iteration:
	./iteration.sh &> iteration.console

.PHONY: remove
remove:
	./remove.sh &> remove.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: dictionary iteration remove exercise
