# Import the "numpy" package as "np"
import numpy as np

# Create 2 new Python Lists
height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Create 2 NumPy Arrays out of the newly created Lists
np_height = np.array(height)
np_weight = np.array(weight)


if __name__ == "__main__":
    print("height    = %s" % height)
    print("np_height = %s" % np_height)

    print()

    print("type(height)    = %s" % type(height))
    print("type(np_height) = %s" % type(np_height))
