# -*- coding: utf-8 -*-

import requests
import time


def live():

    # 获取AccessToken
    # 文档 https://developers.weixin.qq.com/doc/channels/API/windowproduct/getaccesstoken.html
    appId = 'wxbbd783b9b9beef3b'
    secret = 'e8bc1dec258f49b672bac36ea2b297f2'
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appId, secret)
    response = requests.get(url)
    access_token = eval(response.text)['access_token']


    # 获取当前的直播记录
    # 文档 https://developers.weixin.qq.com/doc/channels/API/live/getfinderliverecordlist.html
    url = 'https://api.weixin.qq.com/channels/ec/finderlive/getfinderliverecordlist?access_token=%s' % (access_token)
    response = requests.post(url, json={})
    print(response.text)


    # 获取当前的直播预约记录
    # 文档 https://developers.weixin.qq.com/doc/channels/API/live/getfinderlivenoticerecordlist.html
    url = 'https://api.weixin.qq.com/channels/ec/finderlive/getfinderlivenoticerecordlist?access_token=%s' % (access_token)
    response = requests.post(url, json={})
    print(response.text)


if __name__ == '__main__':
    live()
