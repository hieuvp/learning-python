export PATH := ../../venv/bin:$(PATH)

.PHONY: ping-pong-game
ping-pong-game:
	./ping_pong.sh &> ping_pong.console

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

.PHONY: extend-module-search-path
extend-module-search-path:
	./extend_module_search_path.sh &> extend_module_search_path.console

.PHONY: explore-built-in-urllib
explore-built-in-urllib:
	./explore_built_in_urllib.sh &> explore_built_in_urllib.console

.PHONY: write-package
write-package:
	./write_package.sh &> write_package.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: ping-pong-game import-module-objects import-all-module-objects customize-import-name initialize-module extend-module-search-path explore-built-in-urllib write-package exercise
