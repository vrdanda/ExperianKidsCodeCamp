#
# Fetching a random recipe using the Spoonacular API. 
# You’ll need to sign up for a free RapidAPI account and get an API key from Spoonacular.
# Replace 'YOUR_API_KEY' with your actual API key in the code below:
#

import requests

def get_random_recipe():
    api_key = 'YOUR_API_KEY'
    url = f'https://api.spoonacular.com/recipes/random?apiKey={api_key}&number=1'

    try:
        # Fetch the page
        response = requests.get(url)
        # Parse the data
        data = response.json()
        recipe = data['recipes'][0]
        title = recipe['title']
        instructions = recipe['instructions']
        ingredients = [ingr['original'] for ingr in recipe['extendedIngredients']]

        print(f"Random Recipe: {title}")
        print("Ingredients:")
        for ingredient in ingredients:
            print(f"- {ingredient}")
        print("\nInstructions:")
        print(instructions)
    except Exception as e:
        print(f"Error fetching recipe: {e}")

# Call the function to get a random recipe
get_random_recipe()