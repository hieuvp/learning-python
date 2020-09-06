export PATH := ../venv/bin:$(PATH)

.PHONY: add
add:
	./add.sh &> add.console

.PHONY: multiply
multiply:
	./multiply.sh &> multiply.console

.PHONY: sum
sum:
	./sum.sh &> sum.console

.PHONY: all
all: add multiply sum

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
