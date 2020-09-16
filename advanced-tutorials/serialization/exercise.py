import json


# Add the given "name"/"salary" pair to "salaries_json"
def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    json_str = json.dumps(salaries)

    return json_str


# Testing Code
def main():
    salaries_json = '{"Alfred" : 300, "Jane" : 400 }'

    # Add key-value pair {"Me" : 800}
    new_salaries_json = add_employee(salaries_json, "Me", 800)
    salaries = json.loads(new_salaries_json)

    # Print out the JSON string
    print('salaries["Alfred"] = %s' % salaries["Alfred"])
    print('salaries["Jane"]   = %s' % salaries["Jane"])
    print('salaries["Me"]     = %s' % salaries["Me"])


if __name__ == "__main__":
    main()
