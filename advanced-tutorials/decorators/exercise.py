# A "decorator factory" which returns a "decorator"
# that checks if the input type is correct
def type_check(correct_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for argument in args:
                if not isinstance(argument, correct_type):
                    # In reality, it should raise an error
                    print('Bad type! "%s" is not of type "%s"' % (argument, correct_type))

                    return None

            print("Type checking of function arguments, Passed!")

            return func(*args, **kwargs)

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


def test_first_letter():
    print()
    word = "Hello World"
    print("word = %s" % word)
    print('first_letter(%s) = %s' % (word, first_letter(word)))

    print()
    word = ["Not", "A", "String"]
    print("word = %s" % word)
    print('first_letter(%s) = %s' % (word, first_letter(word)))


test_first_letter()


@type_check(int)
def times(multiplier, multiplicand):
    return multiplier * multiplicand


def test_times():
    print()
    multiplier = 2
    multiplicand = 3
    print("multiplier   = %s" % multiplier)
    print("multiplicand = %s" % multiplicand)
    print("times(%s, %s) = %s" % (multiplier, multiplicand, times(multiplier, multiplicand)))

    print()
    multiplier = 2
    multiplicand = "Not A Number"
    print("multiplier   = %s" % multiplier)
    print("multiplicand = %s" % multiplicand)
    print("times(%s, %s) = %s" % (multiplier, multiplicand, times(multiplier, multiplicand)))


test_times()
