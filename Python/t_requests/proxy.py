# -*- coding: utf-8 -*-

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}


proxy = {
    'http': '171.14.209.188:27829'
}

response = requests.get('https://www.infuq.com/?', headers=headers, proxies=proxy)


