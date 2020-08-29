# "the_rest" variable is a list of variables,
# which receives all arguments which were given to the function after the first 3 arguments
def function(first, second, third, *the_rest):
    print("first    = %s" % first)
    print("second   = %s" % second)
    print("third    = %s" % third)
    print("the_rest = %s" % list(the_rest))


function(1, 2, 3, 4, 5)
