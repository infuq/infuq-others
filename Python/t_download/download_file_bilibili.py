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
    os.system("you-get --playlist %s" % (url))
    

if __name__ == '__main__':
    url = "https://www.bilibili.com/video/BV1e24y1z7eJ/?p=8&spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=62ebf7db76a5df92c9081b0f4659902d"
    download(url)
