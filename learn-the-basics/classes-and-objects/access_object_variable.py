class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


# To access the variable inside of the newly created object "myobjectx" you would do the following:
# So for instance the below would output the string "blah":
myobjectx = MyClass()
print(myobjectx.variable)

myobjecty = MyClass()
myobjecty.variable = "yackity"

# Then print out both values
print(myobjecty.variable)
