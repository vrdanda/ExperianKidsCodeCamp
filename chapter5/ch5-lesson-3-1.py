# 1> Invalid JSON Format. try-except
json_data = '{"name": "Alice", "age": 25, "city": "Los Angeles"'
try:
    python_dict = json.loads(json_data)
except ValueError as e:
    print(f"Error parsing JSON: {e}")

# 2> Key Errors:
# JSON data without the 'city' key​
invalid_json = '{ "name": "Jason", "age": 22 }'
try:
    data = json.loads(invalid_json)
    city = data["city"]  # Accessing a non-existent key​
    print(city)
except KeyError:
    print("Missing 'city' key in JSON data")

# 3> Type Errors (Here we are passing a dictionary instead of json):
invalid_json = {42: "value"}
try:
    data = json.loads(invalid_json)
    print(data)
except TypeError as e:
    print("Type Error:", e)