# Say, we have an iterable list of our favourite pet names, all in lowercase
PETS = ["alfred", "tabitha", "william", "arla"]

# We need them in uppercase
upper_pets = []

# Traditionally, in normal Pythoning
for pet in PETS:
    upper_pet = pet.upper()
    upper_pets.append(upper_pet)

print(upper_pets)


# With "map()",
# it's not only easier, but it's also much more flexible
print(list(map(str.upper, PETS)))
