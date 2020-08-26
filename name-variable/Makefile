export PATH := ../venv/bin:$(PATH)

.PHONY: introduction
introduction:
	cd labs && ./introduction.sh &> ./introduction.console

.PHONY: scenario-1
scenario-1:
	cd labs && ./scenario-1.sh &> ./scenario-1.console

.PHONY: scenario-2
scenario-2:
	cd labs \
	&& cp scenario-1/standalone_script.py scenario-2/ \
	&& ./scenario-2.sh &> ./scenario-2.console

.PHONY: all
all: introduction scenario-1 scenario-2
