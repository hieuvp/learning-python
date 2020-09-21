export PATH := ../../venv/bin:$(PATH)

.PHONY: make-counter
make-counter:
	./make_counter.sh &> ./make_counter.console

.PHONY: transmit-to-space
transmit-to-space:
	./transmit_to_space.sh &> ./transmit_to_space.console

.PHONY: print-msg
print-msg:
	./print_msg.sh &> ./print_msg.console

.PHONY: exercise
exercise:
	./exercise.sh &> ./exercise.console

.PHONY: all
all: make-counter transmit-to-space print-msg exercise

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
