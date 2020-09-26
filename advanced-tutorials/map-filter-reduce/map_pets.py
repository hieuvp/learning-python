# Say, we have an iterable list of our favourite pet names, all in lowercase
pets = ["alfred", "tabitha", "william", "arla"]
print("pets = %s" % pets)
print()


# We need them in uppercase
upper_pets = []
for pet in pets:
    upper_pet = pet.upper()
    upper_pets.append(upper_pet)

print("By following traditional style, upper_pets = %s" % upper_pets)
print()


# With "map()",
# it's not only easier, but it's also much more flexible
upper_pets = map(str.upper, pets)
print("By using a Map, list(upper_pets) = %s" % list(upper_pets))
print("- type(upper_pets)       = %s" % type(upper_pets))
print("- type(list(upper_pets)) = %s" % type(list(upper_pets)))
