#
# Using the Cat Fact API (Heroku):
# This API provides random cat facts.
# Install the requests library using pip install requests.
# Then, use the following Python code to get a random cat fact:
#
import requests

def get_random_cat_fact():
    url = 'https://cat-fact.herokuapp.com/facts'
    response = requests.get(url)
    data = response.json()
    random_fact = data[0]['text']
    return random_fact

print(get_random_cat_fact())