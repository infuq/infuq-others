#! /usr/bin/env python
# -*- coding:utf-8 -*-

''''
下载bilibili中的视频
'''

import os

'''
pip install you-get
'''

def download(url):
    os.system("you-get --playlist %s" % (url))
    

if __name__ == '__main__':
    url = "https://www.bilibili.com/video/BV12o4y127GC?p=16&t=2.2"
    download(url)
