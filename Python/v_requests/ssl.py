# -*- coding: utf-8 -*-

import requests


url = ''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

# 请求不信任的SSL
response = requests.get(url, headers=headers, verify=False)

response = requests.get(url, headers=headers, verify='/PATH/charles-ssl-proxying-certificate.pem')


