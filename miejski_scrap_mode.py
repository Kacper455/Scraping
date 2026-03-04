import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs
import pandas as pd

def getHTML(url):
    r = requests.get(url)
    r.raise_for_status()
    return r.content

url_to_scape = 'https://www.miejski.pl/a-3.html'
html = getHTML(url_to_scape)

urel = 'https://www.miejski.pl/a-'
def getURLS():
     urls = {
        f"url{i}": f"{urel}{i}.html"
        for i in range(1, 31)

}
     return urls
list = []
result = []
listed = []

print(getURLS())

for idx, urls in enumerate(getURLS()):
    html = getHTML(urls) #dynamicznie przypisac adresy url do scrapowania
    soup = bs(html, 'html.parser')

    for x in soup.find_all('ul', id = "simple-link-list"):
        for link in x.find_all('li'):
            ln = link.find("a", href=True)
            list.append(ln['href'])

            list = [
                urljoin(url_to_scape, a['href'])
                for a in x.find_all("a", href=True)
                if a["href"].startswith("/")]
            pr = len(list)
            print(list)

    for idx,address in enumerate(list, start=1):
        page = requests.get(address).content
        soup = bs(page, 'html.parser')

        for b in soup.find_all('div', attrs={'id': "content"}):
            for a in b.find_all('main'):
                for art in a.find_all('article'):
                    for head in art.find_all("header"):
                        header = head.find_all(string=True)

        l = listed.append(header)
        ll = len(listed)

        for x in soup.find_all('main'):
            title = x.find("div", class_="rating-box")
            rate = title.find("span", class_="rating")
            rating = rate.text
            inr = int(rating)
            result.append(inr)
        ll = len(listed)
        r = len(result)
    #print(header)
    if (ll == r):
        data = {
        'Nazwa': listed,
        'Rating': result,
    }
        df = pd.DataFrame(data)
        sorted = df.sort_values(by=['Rating'], ascending=False)
        print(sorted)
    else:
        print("Data is not matching")
        print(result)
    print(ll,r)
