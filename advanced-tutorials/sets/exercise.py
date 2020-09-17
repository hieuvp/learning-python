a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

# Print out a "set" containing all the participants
# from the event A who did not attend the event B
print(set(a).difference(set(b)))
