#!/usr/bin/env python3

import re

'''
从字符串起始位置开始匹配
'''


# 推荐
def f2():
    language = 'Java C C++ Python Shell'
    matcher = re.match(r'^.*(Python).*$', language)
    if matcher:
        print(matcher.group())
        print(matcher.group(0))
        print(matcher.group(1))
        print('匹配正确')
    else:
        print('匹配错误')

    matcher = re.match(r'^.*(?P<value>Python).*$', language, re.I)
    print(type(matcher))  # <class 're.Match'>
    if matcher:
        print(matcher.group())
        print(matcher.group(0))
        print(matcher.group(1))
        print(matcher.group('value'))
        print('匹配正确')
    else:
        print('匹配错误')


def f1():
    language = 'Java C C++ Python Shell'
    pattern = re.compile(r'^.*(Python).*$')

    matcher = pattern.match(language)
    if matcher:
        print(matcher.group())
        print(matcher.group(0))
        print(matcher.group(1))
        print('匹配正确')
    else:
        print('匹配错误')


if __name__ == '__main__':

    f2()

