# -*- coding: utf-8 -*-

import requests


url = ''
data = {

}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

# login
session = requests.session()
session.post(url, data=data, headers=headers)

# visit
response = session.get('http://www.xxx.com/4372057320/profile')
print(response.text)


