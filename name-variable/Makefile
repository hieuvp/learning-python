export PATH := ../venv/bin:$(PATH)

.PHONY: introduction
introduction:
	cd labs && ./introduction.sh &> ./introduction/output.console

.PHONY: scenario-1
scenario-1:
	cd labs && ./scenario-1.sh &> ./scenario-1/output.console

.PHONY: scenario-2
scenario-2:
	cd labs && ./scenario-2.sh &> ./scenario-2/output.console

.PHONY: all
all: introduction scenario-1 scenario-2
