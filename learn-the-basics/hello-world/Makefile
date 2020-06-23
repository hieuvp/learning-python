export PATH := ../../venv/bin:$(PATH)

.PHONY: indentation
indentation:
	./indentation.sh &> indentation.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: indentation exercise
