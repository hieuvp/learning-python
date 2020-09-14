from functools import reduce

# Print the square of each numbers rounded to two decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
print("my_floats = %s" % my_floats)
print(list(map(lambda number: round(number ** 2, 2), my_floats)))


# Print only the names that are less than or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
print("my_names = %s" % my_names)
print(list(filter(lambda name: len(name) <= 7, my_names)))


# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]
print("my_numbers = %s" % my_numbers)

# Fix all three respectively.
# map_result = list(map(lambda x: x, my_floats))
# filter_result = list(filter(lambda name: name, my_names, my_names))
# reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers, 0)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)
