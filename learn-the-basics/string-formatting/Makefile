export PATH := ../../venv/bin:$(PATH)

.PHONY: print-formatted-strings
print-formatted-strings:
	./print_formatted_strings.sh &> print_formatted_strings.console

.PHONY: print-formatted-object
print-formatted-object:
	./print_formatted_object.sh &> print_formatted_object.console

.PHONY: all
all: print-formatted-strings print-formatted-object
