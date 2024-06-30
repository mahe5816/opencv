import requests,openpyxl
from bs4 import BeautifulSoup
import pandas as pd
excel = openpyxl.Workbook()
sheet=excel.active
sheet.title="top rated movie"
sheet.append(["Name","year"])
try:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    source = requests.get('https://www.imdb.com/chart/top/', headers=headers)
    source.raise_for_status()
    soup = BeautifulSoup(source.text, 'html.parser')
    pp=soup.find_all('li',class_="ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent")
    print(len(pp))
    
except Exception as e:
    print(e)
