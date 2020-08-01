TEXT = "String, what should it become!"

print("Length of TEXT = %d" % len(TEXT))
print("The first occurrence of the letter a = %d" % TEXT.index("a"))
print("Letter a occurs %d times" % TEXT.count("a"))
print()

# Slice the TEXT into bits
print("The first five characters are     => '%s'" % TEXT[:5])
print("The next five characters are      => '%s'" % TEXT[5:10])
print("The fourteenth character is       => '%s'" % TEXT[13])
print("The characters with odd index are => '%s'" % TEXT[1::2])
print("The last five characters are      => '%s'" % TEXT[-5:])
print()

print("TEXT in uppercase: %s" % TEXT.upper())  # Convert everything to uppercase
print("TEXT in lowercase: %s" % TEXT.lower())  # Convert everything to lowercase
print()

if TEXT.startswith("Str"):  # Check how a string starts
    print("String starts with 'Str'. Good!")
if TEXT.endswith("ome!"):  # Check how a string ends
    print("String ends with 'ome!'. Good!")
print()

# Split the TEXT into separate substrings, each containing only a word
print("Split the words of the string: %s" % TEXT.split(" "))
