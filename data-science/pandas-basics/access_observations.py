import pandas as pd

# Import cars data
cars = pd.read_csv("cars.csv", index_col=0)

print("+ cars")
print(cars)
print()

# Print out first 4 observations
print("+ cars[0:4]")
print(cars[0:4])
print()

# Print out fifth and sixth observations
print("+ cars[4:6]")
print(cars[4:6])
