export PATH := ../../venv/bin:$(PATH)

.PHONY: search
search:
	./search.sh &> ./search.console

.PHONY: match
match:
	./match.sh &> ./match.console

.PHONY: all
all: search match

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
