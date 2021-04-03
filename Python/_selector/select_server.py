#! /usr/bin/env python3.7
# -*- encoding:utf-8 -*-

# from selectors import DefaultSelector
from urllib.parse import urlparse

if __name__ == '__main__':
    url = 'https://www.infuq.com/'
    url = urlparse(url)
    print(url.netloc)
    print(url.path)
    print(url.hostname)
