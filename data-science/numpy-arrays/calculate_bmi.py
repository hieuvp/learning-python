from getting_started import np_weight, np_height

# Calculate bmi
bmi = np_weight / np_height ** 2

if __name__ == "__main__":
    # Print the result
    print("bmi = %s" % bmi)
