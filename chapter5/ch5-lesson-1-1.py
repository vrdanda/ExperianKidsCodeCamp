# Loading JSON from Strings​
import json
json_string = '{"name": "John", "age": 30}'
python_dict = json.loads(json_string)
print(python_dict)

# Loading JSON from Files​
import json
with open('data.json') as f:
  data = json.load(f)
print(data)