export PATH := ../../venv/bin:$(PATH)

.PHONY: my-game
my-game:
	./my_game.sh &> my_game.console

.PHONY: import-module-objects
import-module-objects:
	./import_module_objects.sh &> import_module_objects.console

.PHONY: import-all-module-objects
import-all-module-objects:
	./import_all_module_objects.sh &> import_all_module_objects.console

.PHONY: customize-import-name
customize-import-name:
	./customize_import_name.sh &> customize_import_name.console

.PHONY: initialize-module
initialize-module:
	./initialize_module.sh &> initialize_module.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: my-game import-module-objects import-all-module-objects customize-import-name initialize-module exercise
