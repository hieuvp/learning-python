export PATH := ../../venv/bin:$(PATH)

.PHONY: print
print:
	./print.sh &> print.console

.PHONY: string-index
string-index:
	./string_index.sh &> string_index.console

.PHONY: string-count
string-count:
	./string_count.sh &> string_count.console

.PHONY: string-slice
string-slice:
	./string_slice.sh &> string_slice.console

.PHONY: string-case
string-case:
	./string_case.sh &> string_case.console

.PHONY: string-check
string-check:
	./string_check.sh &> string_check.console

.PHONY: string-split
string-split:
	./string_split.sh &> string_split.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: print string-index string-count string-slice string-case string-check string-split exercise
