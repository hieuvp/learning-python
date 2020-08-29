# Use square brackets to select one column of the cars DataFrame.
#
# We can either use a single bracket or a double bracket.
# The single bracket with output a Pandas Series,
# while a double bracket will output a Pandas DataFrame.

# Import pandas and cars.csv
import pandas as pd

cars = pd.read_csv("cars.csv", index_col=0)

print()

print("# Print out country column as Pandas Series")
print(cars["cars_per_cap"])
print()

print("# Print out country column as Pandas DataFrame")
print(cars[["cars_per_cap"]])
print()

print("# Print out DataFrame with country and drives_right columns")
print(cars[["cars_per_cap", "country"]])
