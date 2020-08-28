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

.PHONY: access-observations
access-observations:
	./access_observations.sh &> access_observations.console

.PHONY: select-data
select-data:
	./select_data.sh &> select_data.console

.PHONY: all
all: create-dataframe set-index read-csv index-dataframe access-observations select-data

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
