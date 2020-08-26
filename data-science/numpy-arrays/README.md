# Numpy Arrays

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Getting Started](#getting-started)
- [Element-wise Calculations](#element-wise-calculations)
- [Subsetting](#subsetting)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Getting Started

Numpy arrays are great alternatives to Python Lists.
Some of the key advantages of Numpy arrays are that they are fast,
easy to work with, and give users the opportunity to perform calculations across entire arrays.

In the following example, you will first create two Python lists.
Then, you will import the numpy package and create numpy arrays out of the newly created lists.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=getting_started.py) -->
<!-- The below code snippet is automatically added from getting_started.py -->

```py
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
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=getting_started.console) -->
<!-- The below code snippet is automatically added from getting_started.console -->

```console
+ python getting_started.py
np_height = [1.87 1.87 1.82 1.91 1.9  1.85]
np_weight = [81.65 97.52 95.25 92.98 86.18 88.45]
<class 'numpy.ndarray'>
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Element-wise Calculations

Now we can perform element-wise calculations on height and weight.
For example, you could take all 6 of the height and weight observations above,
and calculate the BMI (Body Mass Index) for each observation with a single equation.
These operations are very fast and computationally efficient.
They are particularly helpful when you have 1000s of observations in your data.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=calculate_bmi.py) -->
<!-- The below code snippet is automatically added from calculate_bmi.py -->

```py
# Calculate bmi
# bmi = np_weight / np_height ** 2

# Print the result
# print(bmi)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=calculate_bmi.console) -->
<!-- The below code snippet is automatically added from calculate_bmi.console -->

```console
+ python calculate_bmi.py
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Subsetting

Another great feature of Numpy arrays is the ability to subset.
For instance, if you wanted to know which observations in our BMI array are above 23,
we could quickly subset it to find out.

```python
# For a boolean response
bmi > 23

# Print only those observations above 23
bmi[bmi > 23]
```

## Exercise

First, convert the list of weights from a list to a Numpy array.
Then, convert all of the weights from kilograms to pounds.
Use the scalar conversion of 2.2 lbs per kilogram to make your conversion.
Lastly, print the resulting array of weights in pounds.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
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
