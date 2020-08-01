A_STRING = "Hello world!"

# Starting at index 2, and ending at index 6 (not 7)
print("A_STRING[2:7]   = %s" % A_STRING[2:7])

# Single character at an index
print("A_STRING[2]     = %s" % A_STRING[2])

# Slicing from the start to a number
print("A_STRING[:7]    = %s" % A_STRING[:7])

# Slicing from a first number to the end
print("A_STRING[2:]    = %s" % A_STRING[2:])

# Starting at the end of the string instead of the beginning by using a "negative number"
# This way, "-2" means "2nd character from the end"
print("A_STRING[-2:]   = %s" % A_STRING[-2:])

# Printing the characters of string from "2" to "7", skipping "2" characters
print("A_STRING[2:7:2] = %s" % A_STRING[2:7:2])

# Printing the characters of string from "2" to "7", skipping "1" character
# Both of these produce a same output
print("A_STRING[2:7]   = %s" % A_STRING[2:7])
print("A_STRING[2:7:1] = %s" % A_STRING[2:7:1])

# Reverse a string using slice
print("A_STRING[::-1]  = %s" % A_STRING[::-1])
