import pandas as pd

# Use a Dictionary
dictionary = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98],
}

# BRICS is the acronym coined for an association of five major emerging national economies:
# Brazil, Russia, India, China and South Africa
brics = pd.DataFrame(dictionary)

if __name__ == "__main__":
    print(brics)
