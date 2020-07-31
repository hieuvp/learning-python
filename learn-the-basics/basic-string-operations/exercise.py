TEXT = "Hey there! what should this string be?"

# Length should be 20
print("Length of TEXT = %d" % len(TEXT))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % TEXT.index("a"))

# Number of a's should be 2
print("a occurs %d times" % TEXT.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % TEXT[:5])  # Start to 5
print("The next five characters are '%s'" % TEXT[5:10])  # 5 to 10
print("The thirteenth character is '%s'" % TEXT[12])  # Just number 12
print("The characters with odd index are '%s'" % TEXT[1::2])  # (0-based indexing)
print("The last five characters are '%s'" % TEXT[-5:])  # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % TEXT.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % TEXT.lower())

# Check how a string starts
if TEXT.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if TEXT.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % TEXT.split(" "))
