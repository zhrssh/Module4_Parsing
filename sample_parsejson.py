import json

# Example of json
x = '{"name": "Zherish Galvin Mayordo","age": "21","city": "Quezon City"}'

# Parse JSON
y = json.loads(x)
print("The output of json file is", y)
print("Age: ", y["age"])
print("Name: ", y["name"])
print("City: ", y["city"])
