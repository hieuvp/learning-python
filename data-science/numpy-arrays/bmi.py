from getting_started import np_height, np_weight

# Body Mass Index (BMI) is a measure of body fat
# based on "height" and "weight" that applies to adult men and women
#
# Formula: BMI = kg/m^2
# - kg  : a person's weight in kilograms
# - m^2 : their height in metres squared
#
# A BMI of "25.0" or more is overweight,
# while the healthy range is "18.5" to "24.9"


# Perform "Element-wise Calculations" on "weight" and "height":
#
# Take all "np_height" and "np_weight" observations,
# and calculate the BMI for each observation with a single equation
bmi = np_weight / np_height ** 2

# These operations are very fast and computationally efficient
# They are particularly helpful when we have 1000s (thousands) of observations in our data

if __name__ == "__main__":
    print("np_weight      = %s" % np_weight)
    print("np_height      = %s" % np_height)
    print("np_height ** 2 = %s" % np_height ** 2)
    print("bmi            = %s" % bmi)
