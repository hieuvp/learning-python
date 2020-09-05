pets = ["alfred", "tabitha", "william", "arla"]
upper_pets = []

for pet in pets:
    upper_pet = pet.upper()
    upper_pets.append(upper_pet)

print(upper_pets)

# Which would then output `['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']`

# With "map()" functions, it's not only easier, but it's also much more flexible
# I simply do this:

pets = ["alfred", "tabitha", "william", "arla"]

upper_pets = list(map(str.upper, pets))

print(upper_pets)
