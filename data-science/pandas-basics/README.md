# Pandas Basics

- **Pandas** is a high-level data manipulation tool.
- It is built on the **Numpy** package and its key data structure is called the **DataFrame**.
- **DataFrames** allow you to store and manipulate tabular data
  in rows of observations and columns of variables.

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [DataFrames](#dataframes)
- [Indexing DataFrames](#indexing-dataframes)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## DataFrames

> There are several ways to create a **DataFrame**.

One way is to use a dictionary:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=create_dataframe.py) -->
<!-- The below code snippet is automatically added from create_dataframe.py -->

```py
import pandas as pd

dictionary = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98],
}

# BRICS is the acronym coined for an association of five major emerging national economies:
# Brazil, Russia, India, China and South Africa
brics = pd.DataFrame(dictionary)

if __name__ == "__main__":
    print(brics)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=create_dataframe.console) -->
<!-- The below code snippet is automatically added from create_dataframe.console -->

```console
+ python create_dataframe.py
        country    capital    area  population
0        Brazil   Brasilia   8.516      200.40
1        Russia     Moscow  17.100      143.50
2         India  New Dehli   3.286     1252.00
3         China    Beijing   9.597     1357.00
4  South Africa   Pretoria   1.221       52.98
```

<!-- AUTO-GENERATED-CONTENT:END -->

As we can see with the new `brics` DataFrame,
Pandas has assigned a key for each country as the numerical values 0 through 4.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=set_index.py) -->
<!-- The below code snippet is automatically added from set_index.py -->

```py
from create_dataframe import brics

# If we would like to have different index values,
# say, the two letter country code

# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=set_index.console) -->
<!-- The below code snippet is automatically added from set_index.console -->

```console
+ python set_index.py
         country    capital    area  population
BR        Brazil   Brasilia   8.516      200.40
RU        Russia     Moscow  17.100      143.50
IN         India  New Dehli   3.286     1252.00
CH         China    Beijing   9.597     1357.00
SA  South Africa   Pretoria   1.221       52.98
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

Another way to create a DataFrame is by importing a csv file using Pandas.
Now, the csv `cars.csv` is stored and can be imported using `pd.read_csv`:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=read_csv.py) -->
<!-- The below code snippet is automatically added from read_csv.py -->

```py
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv("cars.csv")

# Print out cars
print(cars)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=read_csv.console) -->
<!-- The below code snippet is automatically added from read_csv.console -->

```console
+ python read_csv.py
  Unnamed: 0  cars_per_cap        country  drives_right
0         US           809  United States          True
1        AUS           731      Australia         False
2        JAP           588          Japan         False
3         IN            18          India         False
4         RU           200         Russia          True
5        MOR            70        Morocco          True
6         EG            45          Egypt          True
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Indexing DataFrames

> There are several ways to index a Pandas DataFrame.

One of the easiest ways to do this is by using square bracket notation.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=index_dataframe.py) -->
<!-- The below code snippet is automatically added from index_dataframe.py -->

```py
# Use square brackets to select one column of the cars DataFrame.
#
# We can either use a single bracket or a double bracket.
# The single bracket with output a Pandas Series,
# while a double bracket will output a Pandas DataFrame.

# Import pandas and cars.csv
import pandas as pd

cars = pd.read_csv("cars.csv", index_col=0)

# Print out country column as Pandas Series
print(cars["cars_per_cap"])

# Print out country column as Pandas DataFrame
print(cars[["cars_per_cap"]])

# Print out DataFrame with country and drives_right columns
print(cars[["cars_per_cap", "country"]])
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=index_dataframe.console) -->
<!-- The below code snippet is automatically added from index_dataframe.console -->

```console
+ python index_dataframe.py
US     809
AUS    731
JAP    588
IN      18
RU     200
MOR     70
EG      45
Name: cars_per_cap, dtype: int64
     cars_per_cap
US            809
AUS           731
JAP           588
IN             18
RU            200
MOR            70
EG             45
     cars_per_cap        country
US            809  United States
AUS           731      Australia
JAP           588          Japan
IN             18          India
RU            200         Russia
MOR            70        Morocco
EG             45          Egypt
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

Square brackets can also be used to access observations (rows) from a DataFrame.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=access_observations.py) -->
<!-- The below code snippet is automatically added from access_observations.py -->

```py
# Import cars data
import pandas as pd

cars = pd.read_csv("cars.csv", index_col=0)

# Print out first 4 observations
print(cars[0:4])

# Print out fifth and sixth observation
print(cars[4:6])
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=access_observations.console) -->
<!-- The below code snippet is automatically added from access_observations.console -->

```console
+ python access_observations.py
     cars_per_cap        country  drives_right
US            809  United States          True
AUS           731      Australia         False
JAP           588          Japan         False
IN             18          India         False
     cars_per_cap  country  drives_right
RU            200   Russia          True
MOR            70  Morocco          True
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

You can also use `loc` and `iloc` to perform just about any data selection operation.

- `loc` is label-based,
  which means that you have to specify rows and columns based on their row and column labels.
- `iloc` is integer index based,
  so you have to specify rows and columns by their integer index like you did in the previous exercise.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=select_data.py) -->
<!-- The below code snippet is automatically added from select_data.py -->

```py
# Import cars data
import pandas as pd

cars = pd.read_csv("cars.csv", index_col=0)

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[["AUS", "EG"]])
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=select_data.console) -->
<!-- The below code snippet is automatically added from select_data.console -->

```console
+ python select_data.py
cars_per_cap      588
country         Japan
drives_right    False
Name: JAP, dtype: object
     cars_per_cap    country  drives_right
AUS           731  Australia         False
EG             45      Egypt          True
```

<!-- AUTO-GENERATED-CONTENT:END -->
