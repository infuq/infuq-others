#!/usr/bin/env python3

import json


d = '{"check": true, "name": "骆昊", "age": 38, "qq": "957658@qq.com", "friends": ["王大锤", "白 元芳"], "cars": [{"brand": "BYD", "max_speed": 180}, {"brand": "Audi", "max_speed": 280}, {"brand": "Benz", "max_speed": 320}]}'

def main():
    data = json.loads(d)
    print(data)

def read_file():
    with open('D:/Repository/infuq-others/Python/JSON数据/data.json', encoding='utf-8') as f:
        data = json.load(f)
        print(data)

        # 等价于
        # data = json.loads(f.read())
        # print(data)


if __name__ == '__main__':
    # main()
    read_file()

