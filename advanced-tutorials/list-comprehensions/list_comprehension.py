words = "the quick brown fox jumps over the lazy dog".split()
print("words = %s\n" % words)


# Create a list of integers which specify the length of each word in a certain sentence,
# but only if the word is not the word "the"
lengths = []
for word in words:
    if word != "the":
        lengths.append(len(word))
print("By traditional style,        lengths = %s" % lengths)

# When using a "list comprehension", we could simplify this process
lengths = [len(word) for word in words if word != "the"]
print("By using List Comprehension, lengths = %s" % lengths)
