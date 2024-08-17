#!/usr/bin/env python3

import re

'''
不一定从字符串起始位置开始匹配

re.sub(pattern, replace, string, count=0, flags=0)
# flags=re.S
# flags=re.M
# replace可以是普通字符串(或者正则字符串)或者函数

'''


# 推荐
def f1():
    data = '2021-03-21'
    res = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', data)
    print(res)

    res = re.sub(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', data)
    print(res)

    data = 'xyz'
    res = re.sub(r'x', r'n', data)
    print(res)


# 推荐
def f2():
    score = '67.57'

    def func(matcher):
        v = matcher.group('value')
        if '7' == v:
            v = int(v) + 1
            return str(v)
        return v

    res = re.sub(r'(?P<value>\d)', func, score)
    print(res)


def f3():
    language = 'Pythox'
    pattern = re.compile(r'x')
    # 替换(原始值保持不变) 将x替换成n
    res = pattern.sub('n', language)
    print(res)


def f4():
    score = '67.57'
    pattern = re.compile(r'(?P<value>\d)')

    def func(matcher):
        v = matcher.group('value')
        if '7' == v:
            v = int(v) + 1
            return str(v)
        return v

    res = pattern.sub(func, score)
    print(res)


if __name__ == '__main__':
    f1()
