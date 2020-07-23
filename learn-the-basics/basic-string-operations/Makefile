export PATH := ../../venv/bin:$(PATH)

.PHONY: print-sentence
print-sentence:
	./print_sentence.sh &> print_sentence.console

.PHONY: string-index
string-index:
	./string_index.sh &> string_index.console

.PHONY: string-count
string_count:
	./string_count.sh &> string_count.console

.PHONY: all
all: print-sentence string-index string_count
