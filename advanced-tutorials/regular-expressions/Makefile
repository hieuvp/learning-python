export PATH := ../../venv/bin:$(PATH)

.PHONY: example
example:
	./example.sh &> ./example.console

.PHONY: all
all: example

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
