#! /usr/bin/env python
# -*- coding:utf-8 -*-

''''
下载gitee仓库中的文件
'''


import sys

cookie = """user_locale=zh-CN; oschina_new_user=false; tz=Asia/Shanghai; remote_way=http; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkchannel={"prop":{"_sa_channel_landing_url":""}}; Hm_lvt_24f17767262929947cc3631f99bfd274=1642762127; gitee_user=true; sensorsdata2015jssdkcross={"distinct_id":"662799","first_id":"17e7c40c77e4e6-0cc6c28bc399758-f791b31-921600-17e7c40c77f65a","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":""},"$device_id":"17e7c40c77e4e6-0cc6c28bc399758-f791b31-921600-17e7c40c77f65a"}; Hm_lpvt_24f17767262929947cc3631f99bfd274=1642762168; gitee-session-n=b3Awb3lqNmN4MHBSYnFNNEJzTU9rZWYxVTA3OE1saXlBQ3hGOHRqa3pVdFkrRlhoQ1NRc2lCa2pQM2wyQm9KL0N4cjNicFExWHZTSXlnNit4M3IwTlQ1bDArSmFFOTAwYWRWbFh6Tm1mbGN6WXI4TmJBVXd0QW9ad3NpQ3dJYVJoVjFoMVB1ZDg0aklOOTExSmo1NE9Fak9Pb1l1TXFrL0lidGlQcjZXem0yWkdCbFpxSEVpblh3YlRMY3BGOXQrTm1JWHVJMlJSL0pMTWNZU2V5c0VpcklBUjY1L1ZkTFlkVlowSjJDRGVERGs3ZkVQY3hyYkh2aGZ5Y3FHSmdDa0pTYlRUdGVLY3pXMG9HcWJzdHpsMHMrNWdVakc5aFpQcnUxdHVLWkxMK215OWVPeEtXSXhsZitjazNTVmlJenFlRE5GOUMvMWxxd0p1SitHcjMxdlBVVWxxL1draThQdkFIekY5SkxZT01DSXNIQ1FMVHVsQWhlVzhSU04yRHpNM29jSFdtd0l4dVJIa3R4NkFaWGRGWWh6am5Bc2dFUTF3NHVHZFBmaWFwd25VZ1dnY0xTR0ZuZGlnT1hTS0pBVThkaU90RnNkMER0YnFBVXJmNWZpMytHcUpmWS9iYmxRRXpyY3dDRmFqM1ZNRFpVZ3JmZ0t5dnpkLzlaeE9yREdaZGphR0pnSGJnVjFFZktINXplaGR3PT0tLVFSWDE5U2Yrd1N2VkZnd01ZY29nK2c9PQ==--be8427815656e73c2c9b48de7f2dd50a8eb791e6"""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Connection": "keep-alive",
    "Cookie": cookie
}

def download(url, filename, version):
    if version == 2:
        download4Python2(url, filename, headers)
    if version == 3:
        headers["Cookie"] = headers["Cookie"].encode("utf8")
        download4Python3(url, filename, headers)


def download4Python2(url, filename, headers):
    import urllib2
    request = urllib2.Request(url=url, data=None, headers=headers)
    response = urllib2.urlopen(request)
    if response.getcode() == 200:
        with open(filename, 'ab') as f:
            f.write(response.read())


def download4Python3(url, filename, headers):
    import urllib.request
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    if response.getcode() == 200:
        with open(filename, 'ab') as f:
            f.write(response.read())


if __name__ == '__main__':
    url = 'https://gitee.com/infuq/infuq-file/raw/master/jdk1.8.0_202-simple.v2.tar.gz'
    filename = 'jdk1.8.0_202-simple.tar.gz'

    version = sys.version.split('.')[0]
    download(url, filename, int(version))

