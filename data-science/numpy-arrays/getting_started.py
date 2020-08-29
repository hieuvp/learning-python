# Import the numpy package as np
import numpy as np

# Create 2 new Python lists
height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Create 2 numpy arrays out of the newly created lists
np_height = np.array(height)
np_weight = np.array(weight)


def main():
    print("np_height       = %s" % np_height)
    print("np_weight       = %s" % np_weight)

    # Print out the type of np_height
    print("type(np_height) = %s" % type(np_height))


if __name__ == "__main__":
    main()
