#! /usr/bin/env python


'''
替换字符串中的部分内容 返回新的字符串  不改变原字符串
sub -> <class 'str'>

切割
split -> <class 'list'>
查找到满足条件的所有结果
findall -> <class 'list'>

查找到结果即停止搜索
search -> <class 're.Match'>
匹配
match -> <class 're.Match'>
'''


import re

def invoke_1():
    matcher = re.search(r'(?P<value>Py[^ ]*n)', 'this is a py PythoN language Python', re.I)
    print(type(matcher))# <class 're.Match'>

    if matcher:
        print('匹配正确')
        print(matcher.group('value'))
    else:
        print('匹配错误')


def invoke_4():
    language = 'Java C C++ PythoN Shell'
    # 从字符串起始位置开始匹配
    matcher = re.match(r'^.*(?P<value>Python).*$', language, re.I)
    print(type(matcher))# <class 're.Match'>

    if matcher:
        print(matcher.group())
        print(matcher.group(0))
        print(matcher.group(1))
        print(matcher.group('value'))
        print('匹配正确')
    else:
        print('匹配错误')


def invoke_2():
    result = re.split(r'[,;]', 'C,C++,Java;Python')
    print(type(result))# <class 'list'>
    print(result)
    print(result[1])

def invoke_3():
    data = '2021-03-21'
    result = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', data)
    print(type(result))# <class 'str'>
    print(result)
    # x = re.sub(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', data)
    # x = re.sub(r'x', r'n', data)


    score = 'asd67.57'
    def func(matcher):
        v = matcher.group('value')
        if '7' == v:
            v = int(v) + 1
            return str(v)
        return v
    score = re.sub(r'(?P<value>\d)', func, score)
    print(type(score))# <class 'str'>
    print(score)


def invoke_5():
    language = 'Java C C++ Python Shell Py123n PY45mN'
    result = re.findall(r'Py[^ ]*n', language, re.IGNORECASE)
    print(type(result))# <class 'list'>
    print(result)

if __name__ == '__main__':
    invoke_4()