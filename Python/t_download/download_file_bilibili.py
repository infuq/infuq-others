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
    url = "https://www.bilibili.com/video/BV1Mi421D7ZB"
    download(url)
