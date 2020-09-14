from functools import reduce

# Print the square of each numbers rounded to two decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
print("my_floats = %s" % my_floats)
print(list(map(lambda number: round(number ** 2, 2), my_floats)))
print()

# Print only the names that are less than or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
print("my_names = %s" % my_names)
print(list(filter(lambda name: len(name) <= 7, my_names)))
print()

# Print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]
print("my_numbers = %s" % my_numbers)
print(reduce(lambda x, y: x * y, my_numbers))
