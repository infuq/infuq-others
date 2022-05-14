#!/usr/bin/env python3

import json


def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', mode='w', encoding='utf-8') as f:
            json.dump(mydict, f)

        with open('data.json', encoding='utf-8') as f:
            mydict = json.load(f)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()

