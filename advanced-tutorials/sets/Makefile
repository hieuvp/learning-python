export PATH := ../../venv/bin:$(PATH)

.PHONY: words
words:
	./words.sh &> ./words.console

.PHONY: participants
participants:
	./participants.sh &> ./participants.console

.PHONY: intersection
intersection:
	./intersection.sh &> ./intersection.console

.PHONY: symmetric-difference
symmetric-difference:
	./symmetric_difference.sh &> ./symmetric_difference.console

.PHONY: difference
difference:
	./difference.sh &> ./difference.console

.PHONY: union
union:
	./union.sh &> ./union.console

.PHONY: all
all: words participants intersection symmetric-difference difference union

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
