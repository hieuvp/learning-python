# Python 3

my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [1, 2, 3, 4, 5]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)
