#!/usr/bin/env python3

import re

'''
不一定从字符串起始位置开始匹配
'''


# 推荐
def f1():
    data = 'this is a python language pyTHon nyz'
    matcher = re.search(r'(py..on)', data)
    if matcher:
        print('匹配正确')
        print(matcher.group())
        print(matcher.group(1))
    else:
        print('匹配错误')

    matcher = re.search(r'(?P<value>Py[^ ]*n)', 'this is a py PythoN language Python', re.I)
    print(type(matcher))  # <class 're.Match'>
    if matcher:
        print('匹配正确')
        print(matcher.group('value'))
    else:
        print('匹配错误')


def f2():
    pattern = re.compile(r'py')

    if not pattern.search('this is a py language'):
        print('匹配错误')
    else:
        print('匹配正确')


if __name__ == '__main__':
    f1()

