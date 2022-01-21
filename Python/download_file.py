#! /usr/bin/env python
# -*- coding:utf-8 -*-



def download4Python2(url, filename):
    import urllib

    urllib.urlretrieve(url=url, filename=filename, data=None)



def download4Python3(url, filename):
    import urllib.request
    urllib.request.urlretrieve(url, filename)

if __name__ == '__main__':

    # url = 'https://gitee.com/infuq/infuq-file/raw/master/jinfo.exe'
    url = 'https://infuq.coding.net/p/infuq/d/infuq-file/git/raw/master/jdk1.8.0_202-simple.tar.gz?download=true'
    filename = 'jdk1.8.0_202-simple.bak.tar.gz'
    download4Python2(url, filename)


