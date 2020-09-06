export PATH := ../../venv/bin:$(PATH)

.PHONY: multiply
multiply:
	./multiply.sh &> ./multiply.console

.PHONY: exercise
exercise:
	./exercise.sh &> ./exercise.console

.PHONY: all
all: multiply exercise

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
