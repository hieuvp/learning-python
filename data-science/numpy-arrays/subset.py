from bmi import bmi

# For instance,
# if you wanted to know which observations in our BMI array are above 23,
# we could quickly subset it to find out

# Boolean response
print("(bmi > 23) = %s" % (bmi > 23))

# Print only those observations above 23
print("bmi[bmi > 23] = %s" % bmi[bmi > 23])
