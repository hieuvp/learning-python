export PATH := ../../venv/bin:$(PATH)

.PHONY: my-game
my-game:
	./my_game.sh &> my_game.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: my-game exercise
