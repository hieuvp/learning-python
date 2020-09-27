# Filter out "words" that are "palindromes" from a tuple
words = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda word: word == word[::-1], words))

print("type(dromes) = %s" % type(words))
print("list(dromes) = %s" % list(words))
print("palindromes  = %s" % palindromes)
