import requests
#
# 4> Custom Error Handling:
# Depending on your application, you might want to define custom error handling logic.
# For example, if you’re reading JSON from a file, handle FileNotFoundError:
try:
    with open("nonexistent.json", "r") as json_file:
        json_content = json.load(json_file)
except FileNotFoundError:
    print("JSON file not found.")

#
# 5> Graceful Degradation
# When working with external APIs, consider gracefully degrading functionality if the API response is unexpected
# requests is not part of standard python, to install in VS Code:
# python create terminal
#
#pip config set --user global.trusted-host files.pythonhosted.org​
#pip install requests

import requests  # Import the requests module​
try:
  api_response = requests.get("https://api.example.com/data")
  json_data = api_response.json()
except (requests.RequestException, ValueError):
  print("Error fetching or parsing API data. Using default values.")
  json_data = {}