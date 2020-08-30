export PATH := ../../venv/bin:$(PATH)

.PHONY: list-comprehension
list-comprehension:
	./list_comprehension.sh &> list_comprehension.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: list-comprehension exercise

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
