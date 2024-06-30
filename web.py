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

    # Find the section containing the movie list
    movie_list = soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base")
    #movies = movie_list.find_all('tr')
    #df=pd.DataFrame(columns=['moviename',''])
    movv=[]
    print(len(movie_list))
    for movie in movie_list:
        movi=movie.find('div',class_="ipc-metadata-list-summary-item__c")
        mov=movi.find('div',class_="ipc-metadata-list-summary-item__tc")
        mo=mov.find('div',"sc-b189961a-0 hBZnfJ cli-children")
        na=mo.find('div',class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title").a.text
        print(na,end=" ")
        ye=mo.find('div',class_="sc-b189961a-7 feoqjK cli-title-metadata").span.text
        """for i in m:
            pp=i.find('span',class_="sc-b189961a-8 kLaxqf cli-title-metadata-item").text
            ppp=pp.text if pp else 'N/A'
            print(ppp,end=" ")"""
        print(ye)
        sheet.append([na,ye])

except Exception as e:
    print(e)
"""for movie in movie_list:
        title = movie.find('td', class_='titleColumn').a.text
        rank = movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
        rating = movie.find('td', class_='ratingColumn imdbRating').strong.text
        print(f'{rank}. {title} - Rating: {rating}')"""


