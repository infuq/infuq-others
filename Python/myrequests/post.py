# -*- coding: utf-8 -*-

import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

data = {
    'username': 'Libai'
}

# curl -d "key=value&key=value" "http://www.infuq.com/"

response = requests.post('https://www.infuq.com/', data=data, headers=headers)


