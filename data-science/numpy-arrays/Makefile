export PATH := ../../venv/bin:$(PATH)

.PHONY: getting-started
getting-started:
	./getting_started.sh &> getting_started.console

.PHONY: bmi
bmi:
	./bmi.sh &> bmi.console

.PHONY: subset
subset:
	./subset.sh &> subset.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: getting-started bmi subset exercise

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
