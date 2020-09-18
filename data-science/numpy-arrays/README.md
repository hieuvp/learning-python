# Numpy Arrays

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Getting Started](#getting-started)
- [Elementwise Operations](#elementwise-operations)
- [Subsetting](#subsetting)
- [Exercise](#exercise)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Getting Started

> **Numpy Arrays** are great alternatives to **Python Lists**.
> <br />Some of the key advantages of **Numpy Arrays** are that they are fast, easy to work with,
> <br />and give users the opportunity to perform calculations across entire arrays.

<br />

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
    print()
    print("height          = %s" % height)
    print("np_height       = %s" % np_height)

    print()
    print("weight          = %s" % weight)
    print("np_weight       = %s" % np_weight)

    print()
    print("type(height)    = %s" % type(height))
    print("type(np_height) = %s" % type(np_height))


if __name__ == "__main__":
    main()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=getting_started.console) -->
<!-- The below code snippet is automatically added from getting_started.console -->

```console
+ python getting_started.py

height          = [1.87, 1.87, 1.82, 1.91, 1.9, 1.85]
np_height       = [1.87 1.87 1.82 1.91 1.9  1.85]

weight          = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
np_weight       = [81.65 97.52 95.25 92.98 86.18 88.45]

type(height)    = <class 'list'>
type(np_height) = <class 'numpy.ndarray'>
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Elementwise Operations

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=bmi.py) -->
<!-- The below code snippet is automatically added from bmi.py -->

```py
from getting_started import np_height, np_weight

# Body Mass Index (BMI) is a measure of body fat
# based on height and weight that applies to adult men and women
#
# Formula: BMI = kg/m^2
# - kg  : a person's weight in kilograms
# - m^2 : their height in metres squared
#
# A BMI of "25.0" or more is overweight, while the healthy range is "18.5" to "24.9"
# BMI applies to most adults 18-65 years


# Performing element-wise calculations on height and weight:
#
# Take all 6 of the "np_height" and "np_weight" observations,
# and calculate the BMI for each observation with a single equation
bmi = np_weight / np_height ** 2

# These operations are very fast and computationally efficient
# They are particularly helpful when you have 1000s (thousands) of observations in our data

if __name__ == "__main__":
    print("bmi = %s" % bmi)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=bmi.console) -->
<!-- The below code snippet is automatically added from bmi.console -->

```console
+ python bmi.py
bmi = [23.34925219 27.88755755 28.75558507 25.48723993 23.87257618 25.84368152]
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Subsetting

> Another great feature of **Numpy Arrays** is the ability to **subset**.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=subset.py) -->
<!-- The below code snippet is automatically added from subset.py -->

```py
from bmi import bmi

print("bmi           = %s" % bmi)

# For instance,
# if you wanted to know which observations in our BMI array are above 25,
# we could quickly subset it to find out

# Boolean response
print("(bmi > 25)    = %s" % (bmi > 25))

# Print only those observations above 25
print("bmi[bmi > 25] = %s" % bmi[bmi > 25])
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=subset.console) -->
<!-- The below code snippet is automatically added from subset.console -->

```console
+ python subset.py
bmi           = [23.34925219 27.88755755 28.75558507 25.48723993 23.87257618 25.84368152]
(bmi > 25)    = [False  True  True  True False  True]
bmi[bmi > 25] = [27.88755755 28.75558507 25.48723993 25.84368152]
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
import numpy as np

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# First, convert the list of weights from a list to a Numpy array
# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)
print("np_weight_kg  = %s" % np_weight_kg)

# Then, convert all of the weights from kilograms to pounds.
# Use the scalar conversion of 2.2 lbs per kilogram to make your conversion.
# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2046226218488

# Lastly, print the resulting array of weights in pounds.
# Print out np_weight_lbs
print("np_weight_lbs = %s" % np_weight_lbs)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
np_weight_kg  = [81.65 97.52 95.25 92.98 86.18 88.45]
np_weight_lbs = [180.00743707 214.99479808 209.99030473 204.98581138 189.99437755
 194.9988709 ]
```

<!-- AUTO-GENERATED-CONTENT:END -->

## References

- [Python - Calculate BMI](https://liyenz.wordpress.com/2019/01/04/day-7-python-calculate-bmi)
