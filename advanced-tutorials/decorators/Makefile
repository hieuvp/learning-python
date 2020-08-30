export PATH := ../../venv/bin:$(PATH)

.PHONY: repeater
repeater:
	./repeater.sh &> repeater.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: repeater exercise

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
