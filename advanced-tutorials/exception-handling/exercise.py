actor = {"name": "John Cleese", "rank": "Awesome"}


# Get last name of the actor
def get_last_name():
    full_name = actor["name"].split()
    last_name = full_name[-1]

    return last_name


# Exception handling
try:
    print('The actor\'s last name is "%s"' % get_last_name())
except KeyError:
    print("All exceptions caught! Good job!")
