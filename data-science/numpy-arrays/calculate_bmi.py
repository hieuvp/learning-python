from getting_started import np_height, np_weight

# Body mass index (BMI) is a measure of body fat
# based on height and weight that applies to adult men and women
#
# Formula: BMI = kg/m^2
# - kg  : a person's weight in kilograms
# - m^2 : their height in metres squared
#
# A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9.
# BMI applies to most adults 18-65 years.

# Now we can perform element-wise calculations on height and weight.
#
# For example,
# you could take all 6 of the height and weight observations above,
# and calculate the BMI (Body Mass Index) for each observation with a single equation.


bmi = np_weight / np_height ** 2

# These operations are very fast and computationally efficient.
# They are particularly helpful when you have 1000s of observations in your data.

if __name__ == "__main__":
    # Print the result
    print("bmi = %s" % bmi)
