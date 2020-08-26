export PATH := ../../venv/bin:$(PATH)

.PHONY: create-dataframe
create-dataframe:
	./create_dataframe.sh &> create_dataframe.console

.PHONY: index-dataframe
index-dataframe:
	./index_dataframe.sh &> index_dataframe.console

.PHONY: all
all: create-dataframe index-dataframe
