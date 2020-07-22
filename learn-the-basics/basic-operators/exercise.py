x = object()
y = object()

# Create two lists called x_list and y_list,
# which contain 10 instances of the variables x and y, respectively.

x_list = [x]
y_list = [y]

# You are also required to create a list called big_list,
# which contains the variables x and y, 10 times each,
# by concatenating the two lists you have created.
big_list = []

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# Testing Code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
