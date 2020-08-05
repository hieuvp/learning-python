export PATH := ../../venv/bin:$(PATH)

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
all: iteration remove exercise
