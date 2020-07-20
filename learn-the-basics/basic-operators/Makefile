export PATH := ../../venv/bin:$(PATH)

.PHONY: simple-operator
simple-operator:
	./simple_operator.sh &> simple_operator.console

.PHONY: modulo-operator
modulo-operator:
	./modulo_operator.sh &> modulo_operator.console

.PHONY: power-operator
power-operator:
	./power_operator.sh &> power_operator.console

.PHONY: concatenate-strings
concatenate-strings:
	./concatenate_strings.sh &> concatenate_strings.console

.PHONY: multiply-strings
multiply-strings:
	./multiply_strings.sh &> multiply_strings.console

.PHONY: join-lists
join-lists:
	./join_lists.sh &> join_lists.console

.PHONY: repeat-list
repeat-list:
	./repeat_list.sh &> repeat_list.console

.PHONY: all
all: simple-operator modulo-operator power-operator concatenate-strings multiply-strings join-lists repeat-list
