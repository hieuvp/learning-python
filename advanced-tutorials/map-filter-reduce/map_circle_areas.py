# Python 3
# Say I have a list of circle areas that I calculated somewhere,
# all in five decimal places.
# And I need to round each element in the list up to its position decimal places,
# meaning that I have to round up the first element in the list to one decimal place,
# the second element in the list to two decimal places,
# the third element in the list to three decimal places, etc.
# With map() this is a piece of cake. Let's see how.

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1, 7)))

print(result)
