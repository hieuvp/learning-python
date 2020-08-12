export PATH := ../../venv/bin:$(PATH)

.PHONY: my-game
my-game:
	./my_game.sh &> my_game.console

.PHONY: import-module-objects
import-module-objects:
	./import_module_objects.sh &> import_module_objects.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: my-game import-module-objects exercise
