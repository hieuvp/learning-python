SENTENCE = "the quick brown fox jumps over the lazy dog"
WORDS = SENTENCE.split()


# Create a list of integers
# which specify the length of each word in a certain sentence,
# but only if the word is not the word "the"
word_lengths = []
for word in WORDS:
    if word != "the":
        word_lengths.append(len(word))
print(WORDS)
print(word_lengths)

print()

# When using a "List Comprehension", we could simplify this process
word_lengths = [len(word) for word in WORDS if word != "the"]
print(WORDS)
print(word_lengths)
