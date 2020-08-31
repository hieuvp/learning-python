import pandas as pd

# Import cars data
cars = pd.read_csv("cars.csv", index_col=0)

print()

print("# Print out observation for Japan")
print("+ cars.iloc[2]")
print(cars.iloc[2])
print()

print("# Print out observations for Australia and Egypt")
print('+ cars.loc[["AUS", "EG"]]')
print(cars.loc[["AUS", "EG"]])
