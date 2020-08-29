# The "therest" variable is a list of variables,
# which receives all arguments which were given to the "foo" function after the first 3 arguments.
def function(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % (list(therest)))


# So calling foo(1,2,3,4,5) will print out:
function(1, 2, 3, 4, 5)
