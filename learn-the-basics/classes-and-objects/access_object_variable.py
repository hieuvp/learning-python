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
