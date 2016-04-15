import requests
from bs4 import BeautifulSoup
import random
import os
import urllib2
import threading
import re


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

headers = [
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'},
    {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'}
]

def MetuSpider(url,page = 1):
     path = os.getcwd()
     path += '\\meitu'
     url += 'index_' + str(page) + '.html'
     source_code = requests.get(url, headers=random.choice(headers))
     plain_text = source_code.text
     soup = BeautifulSoup(plain_text, from_encoding='gb2312')

     title = soup.title.string
     path += '\\' + title

     img_list = soup.find_all('img',{'target' : '_blank'})
     print  img_list
def do_spider(url):
    threads = []
    source_code = requests.get(url, headers=random.choice(headers))
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, from_encoding='gb2312')
    #print soup
    max_pages = soup.find_all('b')[0].string
    print max_pages
    for i in range(1, int(max_pages)):
        threads.append(threading.Thread(target=MetuSpider(url, i)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
if __name__ == "__main__":
    do_spider('http://www.meipic.me/tupian/')