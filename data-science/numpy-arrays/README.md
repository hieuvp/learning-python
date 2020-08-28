# Numpy Arrays

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Getting Started](#getting-started)
- [Element-wise Calculations](#element-wise-calculations)
- [Subsetting](#subsetting)
- [Exercise](#exercise)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Getting Started

> **Numpy Arrays** are great alternatives to **Python Lists**.
> <br />Some of the key advantages of Numpy Arrays are that they are fast, easy to work with,
> <br />and give users the opportunity to perform calculations across entire arrays.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=getting_started.py) -->
<!-- The below code snippet is automatically added from getting_started.py -->

```py
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
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=getting_started.console) -->
<!-- The below code snippet is automatically added from getting_started.console -->

```console
+ python getting_started.py
np_height       = [1.87 1.87 1.82 1.91 1.9  1.85]
np_weight       = [81.65 97.52 95.25 92.98 86.18 88.45]
type(np_height) = <class 'numpy.ndarray'>
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Element-wise Calculations

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=calculate_bmi.py) -->
<!-- The below code snippet is automatically added from calculate_bmi.py -->

```py
from getting_started import np_weight, np_height

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
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=calculate_bmi.console) -->
<!-- The below code snippet is automatically added from calculate_bmi.console -->

```console
+ python calculate_bmi.py
bmi = [23.34925219 27.88755755 28.75558507 25.48723993 23.87257618 25.84368152]
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Subsetting

> Another great feature of **Numpy Arrays** is the ability to **subset**.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=subset.py) -->
<!-- The below code snippet is automatically added from subset.py -->

```py
from calculate_bmi import bmi

# For instance,
# if you wanted to know which observations in our BMI array are above 23,
# we could quickly subset it to find out

# For a boolean response
print("(bmi > 23) = %s" % (bmi > 23))

# Print only those observations above 23
print("bmi[bmi > 23] = %s" % bmi[bmi > 23])
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=subset.console) -->
<!-- The below code snippet is automatically added from subset.console -->

```console
+ python subset.py
(bmi > 23) = [ True  True  True  True  True  True]
bmi[bmi > 23] = [23.34925219 27.88755755 28.75558507 25.48723993 23.87257618 25.84368152]
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# First, convert the list of weights from a list to a Numpy array.
# Then, convert all of the weights from kilograms to pounds.
# Use the scalar conversion of 2.2 lbs per kilogram to make your conversion.
# Lastly, print the resulting array of weights in pounds.

# import numpy as np

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]


# Create a numpy array np_weight_kg from weight_kg


# Create np_weight_lbs from np_weight_kg

# Print out np_weight_lbs
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
```

<!-- AUTO-GENERATED-CONTENT:END -->

## References

- [Day 7: Python - Calculate BMI](https://liyenz.wordpress.com/2019/01/04/day-7-python-calculate-bmi)
