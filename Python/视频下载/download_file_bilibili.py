#! /usr/bin/env python3
# -*- coding:utf-8 -*-

''''
下载bilibili中的视频
'''

import os

'''
pip install you-get
pip3 install you-get
'''

def download(url):
    os.system("you-get --format=flv --playlist %s" % (url))
    

if __name__ == '__main__':
    url = "https://www.bilibili.com/list/watchlater?oid=424860448&bvid=BV133411s7Sa"
    download(url)
