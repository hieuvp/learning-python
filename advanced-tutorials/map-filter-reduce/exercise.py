from functools import reduce

# The square of each floating-point numbers rounded to two decimal places
original_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
square_floats = list(map(lambda number: round(number ** 2, 2), original_floats))
print("original_floats = %s" % original_floats)
print("square_floats   = %s" % square_floats)
print()

# The names that are less than or equal to seven letters
original_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
short_names = list(filter(lambda name: len(name) <= 7, original_names))
print("original_names = %s" % original_names)
print("short_names    = %s" % short_names)
print()

# The product of numbers
numbers = [4, 6, 9, 23, 5]
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print("numbers            = %s" % numbers)
print("product_of_numbers = %s" % product_of_numbers)
