WORDS = "the quick brown fox jumps over the lazy dog".split()


# Create a list of integers which specify the length of each word in a certain sentence,
# but only if the word is not the word "the"
lengths = []
for word in WORDS:
    if word != "the":
        lengths.append(len(word))
print(WORDS)
print(lengths)

print()

# When using a "List Comprehension", we could simplify this process
lengths = [len(word) for word in WORDS if word != "the"]
print(WORDS)
print(lengths)
