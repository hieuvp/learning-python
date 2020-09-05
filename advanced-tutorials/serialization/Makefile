export PATH := ../../venv/bin:$(PATH)

.PHONY: json-dumps
json-dumps:
	./json_dumps.sh &> ./json_dumps.console

.PHONY: pickle-dumps
pickle-dumps:
	./pickle_dumps.sh &> ./pickle_dumps.console

.PHONY: all
all: json-dumps pickle-dumps

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
