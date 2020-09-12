# Handle all the exception!
# Think back to the previous lessons to return the last name of the actor

# Setup
actor = {"name": "John Cleese", "rank": "awesome"}


# Function to modify!!!
def get_last_name():
    return actor["last_name"]


# Testing Code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())
