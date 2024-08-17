#!/usr/bin/env python3


import requests
import base64



def gettoken():

    apikey = "FcOYa6Ymf63tvG8bPvEg27Zj"
    secretkey = "YiDc2C7rZqazer8lqRIRWwNTBkERjzVg"
    host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={apikey}&client_secret={secretkey}'
    response = requests.get(host)
    if response:
        return response.json()["access_token"]

def get_num_from_png(imagedata:str=None):

    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/numbers"
    if imagedata:
        img = imagedata.encode()
    else:
        f = open('D:\\Repository\\infuq-others\\Python\\t_ocr\\t1.png', 'rb')

        img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = gettoken()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        try:
            return response.json()["words_result"][0]['words']
        except IndexError:
            return "验证码获取失败"


if __name__ == '__main__':
    get_num_from_png()



