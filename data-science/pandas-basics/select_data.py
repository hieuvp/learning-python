import pandas as pd

# Import "cars" data
cars = pd.read_csv("cars.csv", index_col=0)
print("+ cars\n%s\n" % cars)

# "iloc" is integer index based
# Print out observation for Japan
print("+ cars.iloc[2]\n%s\n" % cars.iloc[2])

# "loc" is label based
# Print out observations for Australia and Egypt
print('+ cars.loc[["AUS", "EG"]]\n%s' % cars.loc[["AUS", "EG"]])
