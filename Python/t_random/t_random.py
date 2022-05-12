#!/usr/bin/env python3

import random


def r():
    # 0 <= n < 1.0 随机浮点数
    print(random.random())  # 0.30567030500006964
    # 5 <= n <= 15 随机浮点数
    print(random.uniform(5, 15))    # 11.01654241438142
    # 5 <= n <= 15 随机整数
    print(random.randint(5, 15))    # 9
    # 例random.randrange(10,30,2)相当于从[10,12,14,16,...,26,28]序列中获取一个随机数
    print(random.randrange(10, 30, 2))   # 14
    # sequence表示字符串,列表,元组,集合,映射
    print(random.choice(['A', 'B', 'C', 3, 5.2]))   # C
    # 将一个列表中的元素打乱(会修改原有列表)
    year = ['2019', '1990', '1919', '1992', '1998']
    random.shuffle(year)
    print(year)
    # 从序列中随机获取指定k长度的数据并随机排列(不会修改原有序列)
    print(random.sample(['A', 'B', 'C', 3, 5.2], 3))  # ['A', 5.2, 'C']


if __name__ == '__main__':
    r()
