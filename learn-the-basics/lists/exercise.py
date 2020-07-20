numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# Add numbers and strings to the lists using the "append" list method
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")

second_name = None

# Fill in the variable second_name with the second name in the "names" list
second_name = names[1]

# Write out the filled arrays and the second name in the names list (Eric)
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
