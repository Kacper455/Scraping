
# Miejski Scraping

This script is for extracting all publications from specific letter you choose and place them in a .xlsx file. In file there will be two columns with all definitions sorted by rating in a descending mode


## Usage

```python
# most important libraries used
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs
import pandas as pd

# iterating through all pages
 for idx,address in enumerate(list, start=1):
        page = requests.get(address).content
        soup = bs(page, 'html.parser')

# extracting name definition from page
        for a in soup.find_all('main'):
            for art in a.find_all('article'):
                for head in art.find_all("header"):
                    header = head.find_all(string=True)

# extracting rating from page with correct formating
        for x in soup.find_all('main'):
            title = x.find("div", class_="rating-box")
            rate = title.find("span", class_="rating")
            rating = rate.text
            inr = int(rating)
            result.append(inr)

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
