A_STRING = "Hello world!"

# Starting at index "2"
# Ending at index "6" (not "7")
print("A_STRING[2:7]   = %s" % A_STRING[2:7])

# If you just have one number in the brackets,
# it will give you the single character at that index.
# If you leave out the first number but keep the colon,
# it will give you a slice from the start to the number you left in.
# If you leave out the second number,
# it will give you a slice from the first number to the end.
#
# You can even put negative numbers inside the brackets.
# They are an easy way of starting at the end of the string instead of the beginning.
# This way, -3 means "3rd character from the end".

print("A_STRING[2:7:2] = %s" % A_STRING[2:7:2])

# This prints the characters of string from 3 to 7 skipping one character.
# This is extended slice syntax. The general form is `[start:stop:step]`.

print("A_STRING[2:7]   = %s" % A_STRING[2:7])
print("A_STRING[2:7:1] = %s" % A_STRING[2:7:1])

# Note that both of them produce same output
#
# There is no function like strrev in C to reverse a string.
# But with the above mentioned type of slice syntax you can easily reverse a string like this

print("A_STRING[::-1]  = %s" % A_STRING[::-1])
