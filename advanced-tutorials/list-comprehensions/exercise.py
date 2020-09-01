numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
print("numbers  = %s" % numbers)


# Using a "List Comprehension" to create a "new_list" out of the list "numbers",
# which contains only the positive numbers from the list, as integers
new_list = [int(number) for number in numbers if number > 0]
print("new_list = %s" % new_list)
