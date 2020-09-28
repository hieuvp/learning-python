export PATH := ../../venv/bin:$(PATH)

.PHONY: words
words:
	./words.sh &> ./words.console

.PHONY: intersection
intersection:
	./intersection.sh &> ./intersection.console

.PHONY: symmetric-difference
symmetric-difference:
	# Notice: the output is likely to change
	# ./symmetric_difference.sh &> ./symmetric_difference.console

.PHONY: difference
difference:
	# Notice: the output is likely to change
	# ./difference.sh &> ./difference.console

.PHONY: union
union:
	# Notice: the output is likely to change
	# ./union.sh &> ./union.console

.PHONY: exercise
exercise:
	# Notice: the output is likely to change
	# ./exercise.sh &> exercise.console

.PHONY: all
all: words intersection symmetric-difference difference union exercise

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
