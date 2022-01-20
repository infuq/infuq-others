#! /usr/bin/env python
# -*- coding:utf-8 -*-


def download4Python2(url, filename):
    import urllib
    urllib.urlretrieve(url, filename)

def download4Python3(url, filename):
    import urllib.request
    urllib.request.urlretrieve(url, filename)

if __name__ == '__main__':

    url = 'https://gitee.com/infuq/infuq-file/raw/master/jinfo.exe'
    filename = 'jinfo.exe'
    download4Python3(url, filename)


