from getting_started import np_height, np_weight

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
