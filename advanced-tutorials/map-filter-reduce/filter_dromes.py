dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

# Filter out words that are palindromes
# from a tuple (iterable) of suspected palindromes
palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)
