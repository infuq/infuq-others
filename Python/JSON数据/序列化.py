#!/usr/bin/env python3

import json


d = {
    'check': True,
    'name': '骆昊',
    'age': 38,
    'qq': '957658@qq.com',
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BYD', 'max_speed': 180},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 320}
    ]
}

def main():   
    # 如果有中文需要使用 ensure_ascii=False 参数
    data = json.dumps(d, ensure_ascii=False)
    print(data)

def write_file():
    with open('D:/Repository/infuq-others/Python/JSON数据/data.json', mode='w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False)    


if __name__ == '__main__':
    # main()
    write_file()

