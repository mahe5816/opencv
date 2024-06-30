import requests
from bs4 import BeautifulSoup

# Set up the headers for the request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# URL of the Amazon search page
url = "https://www.amazon.in/s?k=iphone+15+pro+max&crid=426KW62JC7CE&sprefix=ipo%2Caps%2C206&ref=nb_sb_ss_ts-doa-p_2_3"

# Request the page
page = requests.get(url, headers=headers)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# Find all elements that match the product name class
name_elements = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')

# Extract and print the product names
product_names = [name.get_text() for name in name_elements if name.get_text() is not None]
for name in product_names:
    print(name)
a=2+3
print(a)