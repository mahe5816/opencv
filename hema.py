import requests
from bs4 import BeautifulSoup
try:
# Set up the headers for the request
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# URL of the Amazon product page
    url = "https://www.amazon.in/Apple-iPhone-Pro-Max-256/dp/B0CHWV2WYK/ref=sr_1_1_sspa?crid=426KW62JC7CE&dib=eyJ2IjoiMSJ9.OYvib3u__hXFvKmx0hKSh7OzOxlFIZ5-uLa6lye50CBST5LVVbP2IMAQw2HmjO8h9bB51a78mTFKSvPaH3jkbFSv4Mo4c0tq3M_0AHPMaJVqTrb3mnFJlsOahrkcKeuSD_RanZkC92OVkPkEeK8DHX2Mz-DNPhUbTNPWXgqaCcAcCoF0YizucAiv-RiE8OrY-Co5s8oTVMBD1UJJ0Shl5JsEHKYLF2K5vnvijSCVjAw.g2uGLwSpzf7NenWFaN40mVnwkts6DOBKB3v5o-VFpiY&dib_tag=se&keywords=iphone%2B15%2Bpro%2Bmax&qid=1716978014&sprefix=ipo%2Caps%2C206&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

# Request the page
    page = requests.get(url, headers=headers)

# Parse the page content with BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')

# Find the element that contains the product name
    product_name = soup.find_all('span', id= 'productTitle')
    #print(product_name)
# Extract and print the product name
    if product_name:
        print(product_name.get_text(strip=True))
    else:
        print("Product name not found")
except Exception as e:
    print(e)
