import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

url = 'http://openinsider.com/'
response = requests.get(url)
soup = bs(response.content, 'html.parser')

table = soup.find('table', attrs={'class': 'tinytable'}) ## extract all tags from so called table
row = []

for x in table.find_all('thead'):
     var3 = x.find(string='Trade&nbsp;Date')
     var = x.find(string='Ticker')
     var1 = x.find(string='ΔOwn')
     var2 = x.find(string='Value')
     print(var3,var,var1,var2)
#table_val = row.append(tdr)

for y in table.find_all('tbody'):
    rows = y.find_all('tr')
    for x in rows:
        date = x.find_all('td')[2]
        own = x.find_all('td')[11]
        value = x.find_all('td')[12]
        tick = x.find_all('td')[3]

        for z in tick.find('b').find_all('a'):
            empty = [date.get_text(), z.get_text(), own.get_text(), value.get_text()]
            df = pd.DataFrame(empty)
            sort = df.sort_values(by='value.get_text()', ascending=True)
            df.head()
            print(df)

            df.to_csv()


