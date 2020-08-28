# In the following example, you will first create two Python lists.
# Then, you will import the numpy package and create numpy arrays out of the newly created lists.

# Import the numpy package as np
import numpy as np

# Create 2 new lists height and weight
height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]


# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)


def main():
    print("np_height = %s" % np_height)
    print("np_weight = %s" % np_weight)

    # Print out the type of np_height
    print(type(np_height))


if __name__ == "__main__":
    main()
