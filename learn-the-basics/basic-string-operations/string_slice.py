A_STRING = "Hello world!"

# Starting at index 2, and ending at index 6 (not 7)
print("A_STRING[2:7]   = %s" % A_STRING[2:7])

# If you just have one number in the brackets,
# it will give you the single character at that index
print("A_STRING[2]     = %s" % A_STRING[2])

# If you leave out the first number but keep the colon,
# it will give you a slice from the start to the number you left in
print("A_STRING[:7]    = %s" % A_STRING[:7])

# If you leave out the second number,
# it will give you a slice from the first number to the end
print("A_STRING[2:]    = %s" % A_STRING[2:])

# You can even put negative numbers inside the brackets.
# They are an easy way of starting at the end of the string instead of the beginning.
# This way, -3 means "3rd character from the end".

print("A_STRING[2:7:2] = %s" % A_STRING[2:7:2])

# Print the characters of string from 2 to 7, skipping one character
# Both of these produce same output
print("A_STRING[2:7]   = %s" % A_STRING[2:7])
print("A_STRING[2:7:1] = %s" % A_STRING[2:7:1])

# Easily reverse a string using slice
print("A_STRING[::-1]  = %s" % A_STRING[::-1])
