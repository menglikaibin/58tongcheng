from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ceshi = client['ceshi']
url_list = ceshi['url_list3']
item_info = ceshi['item_info3']


def get_links_from(channel, pages, who_sells=0):
    # http://hz.58.com/pingbandiannao/0/pn2/
    list_view = '{}{}/pn{}/'.format(channel, str(who_sells), str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    for link in soup.select('td.t a.t'):
        item_link = link.get('href').split('?')[0]
        url_list.insert_one({'url': item_link})
        print(item_link)


def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    title = soup.select('div.col_sub.mainTitle h1')[0].text
    price = soup.select('span.price.c_f50')[0].text
    date = soup.select('.time')[0].text
    area = list(soup.select('.c_25d a')[0].stripped_strings) if soup.find_all('span', 'c_25d') else None
    item_info.insert_one({'title': title, 'price': price, 'date': date, 'area': area})
    print({'title': title, 'price': price, 'date': date, 'area': area})
