# -*- coding: utf-8 -*-

import requests
import time


"""
pip install requests
"""



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

params = {
    'username': 'Libai'
}

response = requests.get('https://www.infuq.com/')
response = requests.get('https://www.infuq.com/', params=params, headers=headers)

# print(response.content)
# print(response.content.decode('utf-8'))
# print(response.text)

# print(response.url)
# print(response.status_code)
# print(response.encoding)
# response.encoding = 'utf-8'
# print(response.encoding)
# print(response.text)



with open('1.html', 'w', encoding='utf-8') as f:
    f.write(response.content.decode('utf-8'))



if __name__ == '__main__':
    pass