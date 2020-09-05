export PATH := ../../venv/bin:$(PATH)

.PHONY: exercise
exercise:
	./exercise.sh &> ./exercise.console

.PHONY: all
all: exercise

.PHONY: all
all:

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
