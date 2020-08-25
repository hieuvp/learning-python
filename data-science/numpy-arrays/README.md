# Numpy Arrays

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Getting started](#getting-started)
- [Print out the type of `np_height`](#print-out-the-type-of-np_height)
- [Element-wise calculations](#element-wise-calculations)
- [Subsetting](#subsetting)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Getting started

Numpy arrays are great alternatives to Python Lists.
Some of the key advantages of Numpy arrays are that they are fast,
easy to work with, and give users the opportunity to perform calculations across entire arrays.

In the following example, you will first create two Python lists.
Then, you will import the numpy package and create numpy arrays out of the newly created lists.

```python
# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)
```

## Print out the type of `np_height`

```python
print(type(np_height))
```

## Element-wise calculations

Now we can perform element-wise calculations on height and weight.
For example, you could take all 6 of the height and weight observations above,
and calculate the BMI for each observation with a single equation.
These operations are very fast and computationally efficient.
They are particularly helpful when you have 1000s of observations in your data.

```python
# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)
```

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

```python
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# Create a numpy array np_weight_kg from weight_kg


# Create np_weight_lbs from np_weight_kg

# Print out np_weight_lbs
```