export PATH := ../../venv/bin:$(PATH)

.PHONY: transmit-to-space
transmit-to-space:
	./transmit_to_space.sh &> ./transmit_to_space.console

.PHONY: print-msg
print-msg:
	./print_msg.sh &> ./print_msg.console

.PHONY: transmit-to-space-v2
transmit-to-space-v2:
	./transmit_to_space_v2.sh &> ./transmit_to_space_v2.console

.PHONY: exercise
exercise:
	./exercise.sh &> ./exercise.console

.PHONY: all
all: transmit-to-space print-msg transmit-to-space-v2 exercise

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
