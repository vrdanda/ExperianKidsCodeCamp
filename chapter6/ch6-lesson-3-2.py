import requests
from bs4 import BeautifulSoup

page = requests.get('https://ww.msn.com')
soup = BeautifulSoup(page.content, 'html.parser')
links = soup.find_all('a')
for link in links:
    print(link.get('href'))


# Find all header tags from the html page content
links = soup.find_all('h1')

# Find all elements with the class name “highlight”:
highlights = soup.find_all(class_='highlight')

# Find an element with the ID “main-content”:
main_content = soup.find(id='main-content')

# Get the text content of an element
paragraph_text = soup.p.text

# Get the parent of an element:
parent = soup.p.parent

# Get the value of an attribute (e.g., href from an anchor tag):
link_href = links[0]['href']

# Navigate
next_sibling = soup.p.next_sibling

# Find the first <h1> tag:
first_h1 = soup.find('h1')

# find() with Custom Functions:
def has_custom_class(tag):
    return tag.has_attr('data-custom')

custom_element = soup.find(has_custom_class)