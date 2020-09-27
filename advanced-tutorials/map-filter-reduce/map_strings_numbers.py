strings = ["a", "b", "c", "d", "e"]
numbers = [1, 2, 3, 4, 5]

print(list(map(lambda x, y: (x, y), strings, numbers)))
