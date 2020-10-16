import pandas as pd

# Import "cars" data
cars = pd.read_csv("cars.csv", index_col=0)

print("+ cars\n%s\n" % cars)

# Print out first 4 observations
print("+ cars[0:4]\n%s\n" % cars[0:4])

# Print out fifth and sixth observations
print("+ cars[4:6]\n%s" % cars[4:6])
