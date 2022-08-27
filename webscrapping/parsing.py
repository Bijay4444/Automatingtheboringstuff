import bs4
import requests

def getamazonprice(productUrl):

    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.txt, 'lxml')
    elems = soup.select('#a-autoid-9-announce > span.a-color-base > span')
    elems[0].text.strip()

price = getamazonprice('https://www.amazon.com/4-Hour-Workweek-Expanded-Updated-Cutting-Edge-ebook/dp/B002WE46UW/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=&sr=')
print('The price is '+ price)
