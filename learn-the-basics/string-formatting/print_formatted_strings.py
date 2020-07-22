# Let's say you have a variable called "name" with your user name in it,
# and you would then like to print(out a greeting to that user.)
# This prints out "Hello, John!"
NAME = "John"
print("Hello, %s!" % NAME)

# To use two or more argument specifiers, use a tuple (parentheses):
# This prints out "John is 23 years old."
NAME = "John"
AGE = 23
print("%s is %d years old." % (NAME, AGE))
