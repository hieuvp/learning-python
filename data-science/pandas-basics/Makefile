export PATH := ../../venv/bin:$(PATH)

.PHONY: create-dataframe
create-dataframe:
	./create_dataframe.sh &> create_dataframe.console

.PHONY: set-index
set-index:
	./set_index.sh &> set_index.console

.PHONY: read-csv
read-csv:
	./read_csv.sh &> read_csv.console

.PHONY: index-dataframe
index-dataframe:
	./index_dataframe.sh &> index_dataframe.console

.PHONY: all
all: create-dataframe set-index read-csv index-dataframe
