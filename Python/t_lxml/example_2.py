#! /usr/bin/env python3.7
# -*- coding:utf-8 -*-

import requests
from lxml import etree


BASE_DOMAIN = 'https://www.ygdy8.net/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}


def x(link):
    response = requests.get(link, headers=headers)

    # text = response.content.decode('gb2312')
    text = response.text
    html = etree.HTML(text)

    hrefs = html.xpath('//table[@class="tbspan"]//a/@href')    
    hrefs = map(lambda v: BASE_DOMAIN + v, hrefs)
    return hrefs
    

if __name__ == '__main__':
    url = 'https://www.ygdy8.net/html/gndy/dyzz/list_23_1.html'
    print(x(url))
