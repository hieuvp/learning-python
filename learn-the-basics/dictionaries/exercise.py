phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}

# Remove "Jill" from the "phonebook"
phonebook.pop("Jill")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

# Add "Jake" to the "phonebook" with the phone number "938273443"
phonebook["Jake"] = 938273443
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

print("phonebook = %s" % phonebook)
