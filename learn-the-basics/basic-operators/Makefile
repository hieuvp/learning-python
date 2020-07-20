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

.PHONY: all
all: simple-operator modulo-operator power-operator
