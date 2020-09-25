# Say we have a list of circle areas, all in five decimal places
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

# We need to round each element in the list up to its position decimal places
# e.g.
# - Round up the first element in the list to one decimal place
# - The second element in the list to two decimal places
# - The third element in the list to three decimal places
round_circle_areas = list(map(round, circle_areas, range(1, 7)))

print("circle_areas       = %s" % circle_areas)
print("round_circle_areas = %s" % round_circle_areas)
