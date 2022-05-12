#!/usr/bin/env python3


import re


# 推荐
def f1():
    res = re.split(r',', 'C,C++,Java,Python')
    print(res)
    print(res[1])

    res = re.split(r'[,;]', 'C,C++,Java;Python')
    print(type(res))  # <class 'list'>
    print(res)
    print(res[1])


def f2():
    pattern = re.compile(r',')
    res = pattern.split('C,C++,Java,Python')
    print(res)
    print(res[1])


if __name__ == '__main__':
    f1()
