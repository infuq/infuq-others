#! /usr/bin/env python3.7
# -*- coding:utf-8 -*-

# pip install bs4

import requests
from bs4 import BeautifulSoup


url = 'https://movie.douban.com/cinema/nowplaying/hangzhou/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

trs = soup.find_all('tr')
for tr in trs:
    print(tr)
    print('='*30)
