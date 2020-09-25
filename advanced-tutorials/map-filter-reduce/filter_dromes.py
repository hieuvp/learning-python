# Filter out words that are palindromes
# from a tuple (iterable) of suspected palindromes
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda word: word == word[::-1], dromes))

print("type(dromes) = %s" % type(dromes))
print("list(dromes) = %s" % list(dromes))
print("palindromes  = %s" % palindromes)
