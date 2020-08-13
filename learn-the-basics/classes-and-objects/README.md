# Classes and Objects

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Fundamentals](#fundamentals)
- [Accessing Object Variables](#accessing-object-variables)
- [Accessing Object Functions](#accessing-object-functions)
- [Exercise](#exercise)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Fundamentals

- **Objects** are an encapsulation of variables and functions into a single entity.
- **Objects** get their variables and functions from classes.
- **Classes** are essentially a template to create your objects.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=class_and_object.py) -->
<!-- The below code snippet is automatically added from class_and_object.py -->

```py
# One very basic class
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


# Assign the above class (template) to an object
my_object_x = MyClass()
```

<!-- AUTO-GENERATED-CONTENT:END -->

- The `self` parameter is a reference to the current instance of the class,
  and is used to access variables that belongs to the class.

- It does not have to be named `self`,
  you can call it whatever you like,
  but it has to be the first parameter of any function in the class.

Now the variable `my_object_x` holds an object of the class `MyClass`
that contains the variable, and the function defined within the class called `MyClass`.

## Accessing Object Variables

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=access_object_variable.py) -->
<!-- The below code snippet is automatically added from access_object_variable.py -->

```py
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


my_object_x = MyClass()
# Access the variable inside of the newly created object
print("my_object_x.variable = %s" % my_object_x.variable)

my_object_y = MyClass()
my_object_y.variable = "yackity"
print("my_object_y.variable = %s" % my_object_y.variable)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=access_object_variable.console) -->
<!-- The below code snippet is automatically added from access_object_variable.console -->

```console
+ python access_object_variable.py
my_object_x.variable = blah
my_object_y.variable = yackity
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Accessing Object Functions

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=access_object_function.py) -->
<!-- The below code snippet is automatically added from access_object_function.py -->

```py
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


my_object_x = MyClass()
# To access a function inside of an object,
# you use notation similar to accessing a variable
my_object_x.function()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=access_object_function.console) -->
<!-- The below code snippet is automatically added from access_object_function.console -->

```console
+ python access_object_function.py
This is a message inside the class.
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# Define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


# Create two new vehicles called car1 and car2
car1 = Vehicle()
car2 = Vehicle()

# Set car1 to be a red convertible worth $60,000.00 with a name of Fer
car1.name = "Fer"
car1.color = "red"
car1.value = 60000.00

print(car1.description())

# Set car2 to be a blue van named Jump worth $10,000.00
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.00

print(car2.description())
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
Fer is a red car worth $60000.00.
Jump is a blue van worth $10000.00.
```

<!-- AUTO-GENERATED-CONTENT:END -->

## References

- [Python Self](https://www.w3schools.com/python/gloss_python_self.asp)
