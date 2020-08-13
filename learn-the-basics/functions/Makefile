export PATH := ../../venv/bin:$(PATH)

.PHONY: write-functions
write-functions:
	./write_functions.sh

.PHONY: call-functions
call-functions:
	./call_functions.sh &> call_functions.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: write-functions call-functions exercise
