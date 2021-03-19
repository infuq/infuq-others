#! /usr/bin/env python

import os

'''
pip install you-get
'''

def download(url):
    os.system("you-get --playlist %s" % (url))
    

if __name__ == '__main__':
    url = "https://www.bilibili.com/video/BV1CJ411D7yD?p=1"
    download(url)
