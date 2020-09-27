# Import cars data
import pandas as pd

cars = pd.read_csv("cars.csv", index_col=0)

print(cars)
print()

print("# Print out first 4 observations")
print("+ cars[0:4]")
print(cars[0:4])
print()

print("# Print out fifth and sixth observation")
print("+ cars[4:6]")
print(cars[4:6])
