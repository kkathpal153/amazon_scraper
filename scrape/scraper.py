#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from log import logger

# http://www.networkinghowtos.com/howto/common-user-agent-list/
HEADERS = {
'authority': 'www.amazon.com','pragma': 'no-cache','cache-control': 'no-cache','dnt': '1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',}

#log object for scraper script
LOG = logger.get_logger('scraper.py')


def getPrice(url):
    
    """ 
    This function is the spine of the applications.
    It accepts the url in string type.
    A get request is been done on the url from requests package with appropriate headers.
    The downloaded page is been scraped using bs4 library to get the value of appropriate elements

    PARAMETERS:
    A valid Amazon web page url of String type

    Return Type:
    A dictionary dataype containing {title,price}
    """

    page = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(page.content, features="lxml")

    product = {'title':'', 'price':''}

    # to prevent script from crashing when there isn't a price for the product
    try:
        
        #trying to find if productTitle exist on the page
        title = soup.find(id='productTitle').get_text().strip()
        LOG.info(title)
       
        product['title'] = title

        #trying to find if priceblock_ourprice exist on the page
        price = soup.find(id='priceblock_ourprice').get_text().strip()
        LOG.info(price)
        
        product['price'] = price

    except Exception as e:
        LOG.error(e.args)
    finally:
        
        return product