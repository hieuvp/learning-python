from bmi import bmi

print("bmi           = %s" % bmi)

# Use subset to find out
# which observations in our BMI array are above "25"
print("bmi > 25      = %s" % (bmi > 25))

# Print only those observations above "25"
print("bmi[bmi > 25] = %s" % bmi[bmi > 25])
