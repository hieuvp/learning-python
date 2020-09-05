export PATH := ../../venv/bin:$(PATH)

.PHONY: map-pets
map-pets:
	./map_pets.sh &> ./map_pets.console

.PHONY: map-circle-areas
map-circle-areas:
	./map_circle_areas.sh &> ./map_circle_areas.console

.PHONY: filter-scores
filter-scores:
	./filter_scores.sh &> ./filter_scores.console

.PHONY: filter-dromes
filter-dromes:
	./filter_dromes.sh &> ./filter_dromes.console

.PHONY: reduce-numbers
reduce-numbers:
	./reduce_numbers.sh &> ./reduce_numbers.console

.PHONY: exercise
exercise:
	./exercise.sh &> ./exercise.console

.PHONY: all
all: map-pets map-circle-areas filter-scores filter-dromes reduce-numbers exercise

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
