from create_dataframe import brics

# If we would like to have different index values,
# say, the two letter country code

# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)
