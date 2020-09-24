export PATH := ../../venv/bin:$(PATH)

.PHONY: lottery
lottery:
	# Notice: the output is likely to change
	# ./lottery.sh &> lottery.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: lottery exercise

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
