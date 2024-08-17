#!/usr/bin/env python3

import re

'''
不一定从字符串起始位置开始匹配


res = pattern.findall('被匹配字符串')
res = pattern.finditer('被匹配字符串')
'''


# 推荐
def f2():
    language = 'Java C C++ Python Shell Py123n PY45mN'
    res = re.findall(r'Py[^ ]*n', language, re.IGNORECASE)
    print(type(res))  # <class 'list'>
    print(res)

    content = '英语书，数学书你好|物理书，生物书'
    res = re.findall(r'(?<=[,，^]).*?(?=书)', content, re.S)
    print(res)

    person = '数学'
    res = re.findall(r'%s书%s' % (person, '你好'), content, flags=re.I)
    print(res)


def f1():
    language = 'Java C C++ Python Shell'
    pattern = re.compile(r'Python')

    res = pattern.findall(language)
    print(res)


if __name__ == '__main__':
    f2()
