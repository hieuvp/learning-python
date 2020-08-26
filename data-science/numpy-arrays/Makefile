export PATH := ../../venv/bin:$(PATH)

.PHONY: getting-started
getting-started:
	./getting_started.sh &> getting_started.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: getting-started exercise
