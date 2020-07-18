export PATH := ../../venv/bin:$(PATH)

.PHONY: pyenv
pyenv:
	./pyenv.sh &> pyenv.console

.PHONY: virtualenv
virtualenv:
	./virtualenv.sh &> virtualenv.console

.PHONY: all
all: pyenv virtualenv
