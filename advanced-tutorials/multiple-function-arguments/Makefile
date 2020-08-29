export PATH := ../../venv/bin:$(PATH)

.PHONY: args
args:
	./args.sh &> args.console

.PHONY: kwargs
kwargs:
	./kwargs.sh &> kwargs.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: args kwargs exercise

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
