# Classes and Objects

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Accessing Object Variables](#accessing-object-variables)
- [Accessing Object Functions](#accessing-object-functions)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

Objects are an encapsulation of variables and functions into a single entity.
Objects get their variables and functions from classes.
Classes are essentially a template to create your objects.

A very basic class would look something like this:

```python
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")
```

We'll explain why you have to include that "self" as a parameter a little bit later.
First, to assign the above class(template) to an object you would do the following:

```python
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
```

Now the variable "myobjectx" holds an object of the class "MyClass"
that contains the variable and the function defined within the class called "MyClass".

## Accessing Object Variables

To access the variable inside of the newly created object "myobjectx" you would do the following:

```python
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.variable
```

So for instance the below would output the string "blah":

```python
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

print(myobjectx.variable)
```

You can create multiple different objects that are of the same class
(have the same variables and functions defined).
However, each object contains independent copies of the variables defined in the class.
For instance, if we were to define another object with the "MyClass" class
and then change the string in the variable above:

```python
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)
```

## Accessing Object Functions

To access a function inside of an object you use notation similar to accessing a variable:

```python
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.function()
```

The above would print out the message, "This is a message inside the class."

## Exercise

We have a class defined for vehicles.
Create two new vehicles called car1 and car2.
Set car1 to be a red convertible worth $60,000.00 with a name of Fer,
and car2 to be a blue van named Jump worth $10,000.00.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


# your code goes here

# Test Code
# print(car1.description())
# print(car2.description())
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
```

<!-- AUTO-GENERATED-CONTENT:END -->
