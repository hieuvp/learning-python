export PATH := ../../venv/bin:$(PATH)

.PHONY: generator-function
generator-function:
	./generator_function.sh &> generator_function.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: generator-function exercise

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
