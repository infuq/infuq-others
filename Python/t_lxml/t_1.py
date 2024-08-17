#! /usr/bin/env python3.7
# -*- coding:utf-8 -*-

# 正在上映电影

import requests
from lxml import etree

url = 'https://movie.douban.com/cinema/nowplaying/hangzhou/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

response = requests.get(url, headers=headers)

html = etree.HTML(response.text)

ul = html.xpath('//ul[@class="lists"]')[0]
lis = ul.xpath('./li')
for li in lis:
    print(li.xpath('@data-title')[0])
    print(li.xpath('.//img/@src')[0])
