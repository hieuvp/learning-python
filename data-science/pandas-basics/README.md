# Pandas Basics

- **Pandas** is a high-level data manipulation tool.
- It is built on the **Numpy** package and its key data structure is called the **DataFrame**.
- **DataFrames** allow you to store and manipulate tabular data
  in rows of observations and columns of variables.

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concepts](#concepts)
  - [English Vietnamese Dictionary](#english-vietnamese-dictionary)
    - [**collectively** `/kəˈlektɪvli/`](#collectively-k%C9%99%CB%88lekt%C9%AAvli)
    - [**heterogeneous** `/ˌhetərəˈdʒiːniəs/`](#heterogeneous-%CB%8Chet%C9%99r%C9%99%CB%88d%CA%92i%CB%90ni%C9%99s)
    - [**tabular** `/ˈtæbjələ(r)/`](#tabular-%CB%88t%C3%A6bj%C9%99l%C9%99r)
    - [**axes** `/ˈæk.siːz/`](#axes-%CB%88%C3%A6ksi%CB%90z)
    - [**cater** `/ˈkeɪtə(r)/`](#cater-%CB%88ke%C9%AAt%C9%99r)
    - [**analogous** `/əˈnæləɡəs/`](#analogous-%C9%99%CB%88n%C3%A6l%C9%99%C9%A1%C9%99s)
    - [**matrices** `/ˈmeɪtrɪsiːz/`](#matrices-%CB%88me%C9%AAtr%C9%AAsi%CB%90z)
  - [Pandas Series](#pandas-series)
  - [Pandas DataFrame](#pandas-dataframe)
  - [Conclusion](#conclusion)
- [Creating Pandas DataFrames](#creating-pandas-dataframes)
  - [From Python Dictionaries](#from-python-dictionaries)
  - [From `.csv` Files](#from-csv-files)
- [Indexing Pandas DataFrames](#indexing-pandas-dataframes)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

### English Vietnamese Dictionary

#### **collectively** `/kəˈlektɪvli/`

- (adverb) chung, tập thể

#### **heterogeneous** `/ˌhetərəˈdʒiːniəs/`

- (adjective)
  - consisting of many different kinds of people or things
  - hỗn tạp, đa dạng

#### **tabular** `/ˈtæbjələ(r)/`

- (adjective)
  - presented or arranged in a table (= in rows and columns)
  - bảng, dạng bảng

#### **axes** `/ˈæk.siːz/`

- plural of **axis** `/ˈæksɪs/`

#### **cater** `/ˈkeɪtə(r)/`

- (verb)
  - to provide food and drinks for a social event
  - cung cấp đồ ăn thức uống
  - e.g. who will be catering the wedding?

<br />

- (phrasal verb) cater to somebody/something
  - to provide the things that a particular type of person wants,
    especially things that you do not approve of
  - phục vụ đến
  - e.g. they only publish novels which cater to the mass market

<br />

- (phrasal verb) cater for somebody/something
  - to provide the things that a particular person or situation needs or wants
  - phục vụ cho
  - e.g. this programme caters for the masses
    (chương trình này phục vụ cho quần chúng)
  - e.g. the class caters for all ability ranges

#### **analogous** `/əˈnæləɡəs/`

- (adjective) analogous (to/with something)
  - similar in some way to another thing or situation
    and therefore able to be compared with it
  - tương tự
  - e.g. the national debt is analogous with private debt
  - e.g. the two situations are roughly analogous

#### **matrices** `/ˈmeɪtrɪsiːz/`

- plural of **matrix** `/ˈmeɪtrɪks/`

### Pandas Series

> **Pandas Series** is a **one-dimensional** labeled array
> capable of holding data of any type (Integer, String, Float, Python Objects, etc.).

<div align="center">
  <img src="assets/pandas-series.png" width="640">
  <div><b>Pandas Series</b> is nothing but a column in an excel sheet</div>
</div>

<br />

1. The **axis labels** are collectively called **index**.
1. **Labels** need not be unique but must be a hashable type.
1. The object supports both **integer** and **label-based** **indexing**
   <br />and provides a host of methods for performing operations involving the **index**.

### Pandas DataFrame

> **Pandas DataFrame** is **two-dimensional** size-mutable,
> potentially heterogeneous tabular data structure with labeled axes (rows and columns).

<div align="center">
  <img src="assets/pandas-dataframe.png" width="680">
  <div>
    Think of it like a <b>spreadsheet</b>,
    or <b>SQL table</b>,
    or a <b>dictionary of Series objects</b>
  </div>
</div>

<br />

1. **Pandas DataFrame** consists of three principal components:
   **Data**, **Rows**, and **Columns**.
1. **Data** is aligned in a tabular fashion in **Rows** and **Columns**.

### Conclusion

- The **Pandas Series** is the data structure for a single column of a **Pandas DataFrame**,
  not only conceptually, but literally.
  <br />e.g. the data in a **Pandas DataFrame**
  is actually stored in memory as a collection of **Pandas Series**.

- They both have extremely similar APIs,
  but you will find that **Pandas DataFrame** methods always cater to the possibility
  that you have more than one column.
  And, of course,
  you can always add another **Pandas Series** (or equivalent object) to a **Pandas DataFrame**,
  while adding a **Pandas Series** to another **Pandas Series** involves creating a **Pandas DataFrame**.

## Creating Pandas DataFrames

### From Python Dictionaries

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=dataframe.py) -->
<!-- The below code snippet is automatically added from dataframe.py -->

```py
import pandas as pd

# Use a Dictionary
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
+ python dataframe.py
        country    capital    area  population
0        Brazil   Brasilia   8.516      200.40
1        Russia     Moscow  17.100      143.50
2         India  New Dehli   3.286     1252.00
3         China    Beijing   9.597     1357.00
4  South Africa   Pretoria   1.221       52.98
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

- As we can see with the new `brics` DataFrame,
  Pandas has assigned a **key** for each country as the numerical values `0` through `4`.
- If we would like to have different **index** values,
  say, the two letter country code:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=set_index.py) -->
<!-- The below code snippet is automatically added from set_index.py -->

```py
from dataframe import brics

# Set the "index"
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out "brics" with new "index" values
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

### From `.csv` Files

> Another way to create a **DataFrame** is
> by importing a **csv** file using **Pandas**.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=read_csv.py) -->
<!-- The below code snippet is automatically added from read_csv.py -->

```py
import pandas as pd

# Import "cars.csv" data
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

## Indexing Pandas DataFrames

> There are several ways to index a Pandas DataFrame.

<br />

One of the easiest ways to do this is by using square bracket notation.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=index_dataframe.py) -->
<!-- The below code snippet is automatically added from index_dataframe.py -->

```py
# Use square brackets to select one column of the cars DataFrame
#
# We can either use a single bracket or a double bracket:
# - Single bracket will output a Pandas Series
# - Double bracket will output a Pandas DataFrame

# Import "pandas"
import pandas as pd

# Import "cars.csv"
cars = pd.read_csv("cars.csv", index_col=0)

print("+ cars\n%s\n" % cars)

# Pandas Series with "cars_per_cap" column
print('+ cars["cars_per_cap"]\n%s\n' % cars["cars_per_cap"])

try:
    # Pandas Series with "cars_per_cap" and "country" columns
    print('+ cars["cars_per_cap", "country"]')
    print(cars["cars_per_cap", "country"])
except Exception as err:
    print("type(err) = %s" % type(err))
    print("err       = %s" % err)
print()

# Pandas DataFrame with "cars_per_cap" column
print('+ cars[["cars_per_cap"]]\n%s\n' % cars[["cars_per_cap"]])

# Pandas DataFrame with "cars_per_cap" and "country" columns
print('+ cars[["cars_per_cap", "country"]]\n%s' % cars[["cars_per_cap", "country"]])
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=index_dataframe.console) -->
<!-- The below code snippet is automatically added from index_dataframe.console -->

```console
+ python index_dataframe.py
+ cars
     cars_per_cap        country  drives_right
US            809  United States          True
AUS           731      Australia         False
JAP           588          Japan         False
IN             18          India         False
RU            200         Russia          True
MOR            70        Morocco          True
EG             45          Egypt          True

+ cars["cars_per_cap"]
US     809
AUS    731
JAP    588
IN      18
RU     200
MOR     70
EG      45
Name: cars_per_cap, dtype: int64

+ cars["cars_per_cap", "country"]
type(err) = <class 'KeyError'>
err       = ('cars_per_cap', 'country')

+ cars[["cars_per_cap"]]
     cars_per_cap
US            809
AUS           731
JAP           588
IN             18
RU            200
MOR            70
EG             45

+ cars[["cars_per_cap", "country"]]
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
import pandas as pd

# Import "cars" data
cars = pd.read_csv("cars.csv", index_col=0)

print("+ cars\n%s\n" % cars)

# Print out first 4 observations
print("+ cars[0:4]\n%s\n" % cars[0:4])

# Print out fifth and sixth observations
print("+ cars[4:6]\n%s" % cars[4:6])
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=access_observations.console) -->
<!-- The below code snippet is automatically added from access_observations.console -->

```console
+ python access_observations.py
+ cars
     cars_per_cap        country  drives_right
US            809  United States          True
AUS           731      Australia         False
JAP           588          Japan         False
IN             18          India         False
RU            200         Russia          True
MOR            70        Morocco          True
EG             45          Egypt          True

+ cars[0:4]
     cars_per_cap        country  drives_right
US            809  United States          True
AUS           731      Australia         False
JAP           588          Japan         False
IN             18          India         False

+ cars[4:6]
     cars_per_cap  country  drives_right
RU            200   Russia          True
MOR            70  Morocco          True
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

You can also use `loc` and `iloc` to perform just about any data selection operation.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=select_data.py) -->
<!-- The below code snippet is automatically added from select_data.py -->

```py
import pandas as pd

# Import "cars" data
cars = pd.read_csv("cars.csv", index_col=0)

print("+ cars\n%s\n" % cars)

# "iloc" is integer index based,
# so you have to specify rows and columns by their integer index
# like you did in the previous exercise

# Print out observation for Japan
print("+ cars.iloc[2]\n%s\n" % cars.iloc[2])


# "loc" is label-based,
# which means that you have to specify rows and columns
# based on their row and column labels

# Print out observations for Australia and Egypt
print('+ cars.loc[["AUS", "EG"]]\n%s' % cars.loc[["AUS", "EG"]])
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=select_data.console) -->
<!-- The below code snippet is automatically added from select_data.console -->

```console
+ python select_data.py
+ cars
     cars_per_cap        country  drives_right
US            809  United States          True
AUS           731      Australia         False
JAP           588          Japan         False
IN             18          India         False
RU            200         Russia          True
MOR            70        Morocco          True
EG             45          Egypt          True

+ cars.iloc[2]
cars_per_cap      588
country         Japan
drives_right    False
Name: JAP, dtype: object

+ cars.loc[["AUS", "EG"]]
     cars_per_cap    country  drives_right
AUS           731  Australia         False
EG             45      Egypt          True
```

<!-- AUTO-GENERATED-CONTENT:END -->

## References

- [Python | Pandas Series](https://www.geeksforgeeks.org/python-pandas-series)
- [Python | Pandas DataFrame](https://www.geeksforgeeks.org/python-pandas-dataframe)
