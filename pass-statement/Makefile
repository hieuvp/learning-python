export PATH := ../venv/bin:$(PATH)

.PHONY: example
example:
	./example.sh &> ./example.console

.PHONY: loop
loop:
	./loop.sh

.PHONY: function
function:
	./function.sh

.PHONY: class
class:
	./class.sh

.PHONY: if
if:
	./if.sh

.PHONY: all
all: example loop function class if

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
