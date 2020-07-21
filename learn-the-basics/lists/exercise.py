numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# Add Numbers and Strings to the Lists using the "append" list method
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")

SECOND_NAME = None

# Fill in the variable SECOND_NAME with the second name in the "names" list
SECOND_NAME = names[1]

# Write out the filled arrays and the second name in the names list (Eric)
print(numbers)
print(strings)
print("The second name on the names list is %s" % SECOND_NAME)
