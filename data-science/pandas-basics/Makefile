export PATH := ../../venv/bin:$(PATH)

.PHONY: create-dataframe
create-dataframe:
	./create_dataframe.sh &> create_dataframe.console

.PHONY: read-csv
read-csv:
	./read_csv.sh &> read_csv.console

.PHONY: index-dataframe
index-dataframe:
	./index_dataframe.sh &> index_dataframe.console

.PHONY: all
all: create-dataframe read-csv index-dataframe
