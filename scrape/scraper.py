import requests
from bs4 import BeautifulSoup

from log import logger

# http://www.networkinghowtos.com/howto/common-user-agent-list/
HEADERS = {
'authority': 'www.amazon.com',
'pragma': 'no-cache',
'cache-control': 'no-cache',
'dnt': '1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-dest': 'document',
'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

log = logger.get_logger('scraper.py')


def getPrice(url):
    
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, features="lxml")

    product = {'title':'', 'price':''}

    # to prevent script from crashing when there isn't a price for the product
    try:
        
        title = soup.find(id='productTitle').get_text().strip()
        log.info(title)
        
        price = soup.find(id='priceblock_ourprice').get_text().strip()
        log.info(price)
        
        product = {
            'title': title,
            'price': price
        }

    except Exception as e:
        log.error(e.args)
    finally:
        return product