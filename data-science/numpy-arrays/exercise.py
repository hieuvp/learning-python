import numpy as np

weight_kgs = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Convert from a "List" to a "NumPy Array"
np_weight_kgs = np.array(weight_kgs)
print("np_weight_kgs = %s" % np_weight_kgs)

# Convert all of the weights from kilograms to pounds ("pound" abbreviated as "lb")
# Use the scalar conversion of 2.2 lbs per kilogram to make your conversion
np_weight_lbs = np_weight_kgs * 2.2

# Print the resulting array of weights in pounds
print("np_weight_lbs = %s" % np_weight_lbs)
