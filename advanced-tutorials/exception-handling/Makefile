export PATH := ../../venv/bin:$(PATH)

.PHONY: exception
exception:
	./exception.sh &> ./exception.console

.PHONY: example
example:
	./example.sh &> ./example.console

.PHONY: exercise
exercise:
	./exercise.sh &> ./exercise.console

.PHONY: all
all: exception example exercise

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
