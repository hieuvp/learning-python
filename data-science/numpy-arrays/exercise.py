import numpy as np

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Convert the list of weights from a "List" to a "Numpy Array"
np_weight_kg = np.array(weight_kg)
print("np_weight_kg  = %s" % np_weight_kg)

# Convert all of the weights from kilograms to pounds ("pound" abbreviated as "lb")
# Use the scalar conversion of 2.2 lbs per kilogram to make your conversion
np_weight_lbs = np_weight_kg * 2.2

# Lastly, print the resulting array of weights in pounds
print("np_weight_lbs = %s" % np_weight_lbs)
