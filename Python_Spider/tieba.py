
import requests
from bs4 import BeautifulSoup
import random
import os
import urllib2
import threading


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


def ImageSpider(url, page= 1):
    path = os.getcwd()
    url = url + '?pn=' + str(page)
    source_code = requests.get(url, headers=random.choice(headers))

    # just get the code, no headers or anything
    plain_text = source_code.text

    #print plain_text
    # BeautifulSoup objects can be sorted through easy
    soup = BeautifulSoup(plain_text)
    title = soup.title.string
    path += '\\img'
    list_soup = soup.find_all('img', {'class':"BDE_Image"})

    if not os.path.exists(path):
        os.mkdir(path)


    for url in list_soup:
        img = url.get('src')
        name = img.split('/')[-1]
        conn = urllib2.build_opener().open(urllib2.Request(img))
        #urllib.urlretrieve(img, path+"\\"+name, None)
        data = conn.read()
        f = open(path+"\\"+name, 'w + b')
        f.write(data)
        f.close()

    print 'Done...' + str(page)


def do_spider(url):
    threads = []
    source_code = requests.get(url, headers=random.choice(headers))
    # just get the code, no headers or anything
    plain_text = source_code.text

    # print plain_text
    # BeautifulSoup objects can be sorted through easy
    soup = BeautifulSoup(plain_text)

    max_page = soup.find_all('input', {'class': 'jump_input_bright'})
    page = max_page[0].get('max-page')
    page_list = range(1, int(page))

    #create a lock
    mutex = threading.Lock()
    print page_list
    #create thread
    for i in page_list:
        threads.append(threading.Thread(target=ImageSpider(url, i)))
    #start thread
    for t in threads:
        t.start()
    #waiting for sub-thread
    for t in threads:
        t.join()





if __name__ == "__main__":
    do_spider('http://tieba.baidu.com/p/4218517556')
