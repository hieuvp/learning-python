export PATH := ../venv/bin:$(PATH)

.PHONY: double
double:
	./double.sh &> double.console

.PHONY: multiply
multiply:
	./multiply.sh &> multiply.console

.PHONY: sum
sum:
	./sum.sh &> sum.console

.PHONY: functions
functions:
	./functions.sh &> functions.console

.PHONY: all
all: double multiply sum functions

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
