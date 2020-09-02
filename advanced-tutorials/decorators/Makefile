export PATH := ../../venv/bin:$(PATH)

.PHONY: example
example:
	./example.sh &> example.console

.PHONY: repeater
repeater:
	./repeater.sh &> repeater.console

.PHONY: decorating-functions
decorating-functions:
	./decorating_functions.sh &> decorating_functions.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: example repeater decorating-functions exercise

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
