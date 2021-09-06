#! /usr/bin/env python

import os

'''
pip install you-get
'''


def download(url):
    os.system("you-get --playlist %s" % (url))
    

if __name__ == '__main__':
    url = "https://www.bilibili.com/video/BV1Cy4y1C7WY?spm_id_from=333.824.b_76696577626f785f7265706f7274.1"
    download(url)
