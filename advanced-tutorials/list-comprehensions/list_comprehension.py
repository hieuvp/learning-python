words = "the quick brown fox jumps over the lazy dog".split()
print("words = %s\n" % words)


# Create a list of integers
# which specifies the length of each word in the sentence,
# but only if the "word" is not the word "the"

lengths = []
for word in words:
    if word != "the":
        lengths.append(len(word))
print("By following traditional style, lengths = %s" % lengths)

# When using a "List Comprehension", we could simplify this process
lengths = [len(word) for word in words if word != "the"]
print("By using a List Comprehension,  lengths = %s" % lengths)
