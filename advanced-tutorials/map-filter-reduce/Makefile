export PATH := ../../venv/bin:$(PATH)

.PHONY: map-pets
map-pets:
	./map_pets.sh &> ./map_pets.console

.PHONY: map-circle-areas
map-circle-areas:
	./map_circle_areas.sh &> ./map_circle_areas.console

.PHONY: map-inequable-iterables
map-inequable-iterables:
	./map_inequable_iterables.sh &> ./map_inequable_iterables.console

.PHONY: zip-strings-numbers
zip-strings-numbers:
	./zip_strings_numbers.sh &> ./zip_strings_numbers.console

.PHONY: map-strings-numbers
map-strings-numbers:
	./map_strings_numbers.sh &> ./map_strings_numbers.console

.PHONY: filter-scores
filter-scores:
	./filter_scores.sh &> ./filter_scores.console

.PHONY: filter-palindromes
filter-palindromes:
	./filter_palindromes.sh &> ./filter_palindromes.console

.PHONY: sum
sum:
	./sum.sh &> ./sum.console

.PHONY: sum-with-initial
sum-with-initial:
	./sum_with_initial.sh &> ./sum_with_initial.console

.PHONY: exercise
exercise:
	./exercise.sh &> ./exercise.console

.PHONY: all
all: map-pets map-circle-areas map-inequable-iterables zip-strings-numbers map-strings-numbers filter-scores filter-palindromes sum sum-with-initial exercise

.PHONY: git-add
git-add: all
	@printf "\n"
	$(MAKEFILE_SCRIPT_PATH)/fmt-markdown.sh

	@printf "\n"
	git add --all .
