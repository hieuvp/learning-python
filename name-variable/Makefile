export PATH := ../venv/bin:$(PATH)

.PHONY: introduction
introduction:
	cd labs/introduction && ./example.sh &> ./example.console

.PHONY: scenario-1
scenario-1:
	cd labs/scenario-1

.PHONY: scenario-2
scenario-2:
	cd labs/scenario-2 \
	&& cp ../scenario-1/name_script.py .

.PHONY: all
all: introduction scenario-1 scenario-2
