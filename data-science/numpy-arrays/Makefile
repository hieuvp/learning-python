export PATH := ../../venv/bin:$(PATH)

.PHONY: getting-started
getting-started:
	./getting_started.sh &> getting_started.console

.PHONY: calculate-bmi
calculate-bmi:
	./calculate_bmi.sh &> calculate_bmi.console

.PHONY: exercise
exercise:
	./exercise.sh &> exercise.console

.PHONY: all
all: getting-started calculate-bmi exercise
