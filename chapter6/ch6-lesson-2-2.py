import requests

def get_random_cat_fact_ninja():
    url = 'https://catfact.ninja/fact'
    response = requests.get(url)
    data = response.json()
    random_fact = data['fact']
    return random_fact

print(get_random_cat_fact_ninja())