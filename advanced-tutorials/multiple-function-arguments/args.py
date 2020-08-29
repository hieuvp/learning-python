def function(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % (list(therest)))


function(1, 2, 3, 4, 5)
