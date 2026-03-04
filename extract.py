import requests
from bs4 import BeautifulSoup
url = 'https://open.spotify.com/playlist/37i9dQZEVXcXHWVVT0lfDq'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rack = soup.find('class', attrs={'class': 'tinytable'})
table_head = soup.thead
    for x in table_head.find('tr'):
        for y in x.find_all('td'):
            print(y.get_text())
