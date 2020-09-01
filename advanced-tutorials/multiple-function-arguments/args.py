# "rest" variable is a list of variables,
# which receives all arguments which were given to the function after the first 3 arguments
def function(first, second, third, *rest):
    print("first  = %s" % first)
    print("second = %s" % second)
    print("third  = %s" % third)
    print("rest   = %s" % list(rest))


function(1, 2, 3, 4, 5)
