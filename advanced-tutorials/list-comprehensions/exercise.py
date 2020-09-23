# Use a "List Comprehension"
# to create a list of "positive_integers" out of "numbers"
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_integers = [int(number) for number in numbers if number > 0]

print("numbers           = %s" % numbers)
print("positive_integers = %s" % positive_integers)
