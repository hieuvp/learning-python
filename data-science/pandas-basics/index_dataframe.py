# Use square brackets to select one column of the cars DataFrame
#
# We can either use a single bracket or a double bracket:
# - Single bracket will output a Pandas Series
# - Double bracket will output a Pandas DataFrame

# Import "pandas"
import pandas as pd

# Import "cars.csv"
cars = pd.read_csv("cars.csv", index_col=0)

print("+ cars\n%s\n" % cars)

# Pandas Series with "cars_per_cap" column
print('+ cars["cars_per_cap"]\n%s\n' % cars["cars_per_cap"])

try:
    # Pandas Series with "cars_per_cap" and "country" columns
    print('+ cars["cars_per_cap", "country"]')
    print(cars["cars_per_cap", "country"])
except Exception as err:
    print("type(err) = %s" % type(err))
    print("err       = %s" % err)
print()

# Pandas DataFrame with "cars_per_cap" column
print('+ cars[["cars_per_cap"]]\n%s\n' % cars[["cars_per_cap"]])

# Pandas DataFrame with "cars_per_cap" and "country" columns
print('+ cars[["cars_per_cap", "country"]]\n%s' % cars[["cars_per_cap", "country"]])
