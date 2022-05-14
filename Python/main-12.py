#! /usr/bin/env python3.7
# -*- coding:utf-8 -*-

from functools import reduce
from datetime import datetime
import re

x = 'tom'
print('Hello World')
print('A', 'B', 'C')
print('username: ' + x)
print('username: ', x)

# address = input('请输入地址: ')
# print(address)

# 转义
print('\\\t\\')
# 不转义
print(r'\\\t\\')

print('''第一行
第二行
第三行
第四行''')

print(True)
print(False)
# and not or
print(True and False)

color = None
print('color:', color)

# 3.3333333333333335
print(10 / 3)
# 3.0
print(9 / 3)
# 3
print(9 // 3)
# 3
print(10 // 3)
# 1
print(10 % 3)

# 65
print(ord('A'))
# 20013
print(ord('中'))
# 文
print(chr(25991))

b = b'ABC'
print(b)

# b'\xe4\xb8\xad\xe6\x96\x87'
print('中文'.encode('UTF-8'))

print(len('中文'))

print('%d %2d' % (3, 6))
print('%.5f' % 3.1415926)
print('username: %s %s' % (12, True))
print('username: {0} password: {1}'.format('tom', '123456'))


arr = ['姓名', 15, True, sex]


color = 'BLACK'
if color == 'BLACK':
    print('黑色')
elif color == 'RED':
    print('红色')
else:
    print('其他')

# 数值型字符串转成数值
k = int('65535')
float('3.14')
# 数值转成字符串
str(3.14)

arr = ['姓名', '性别', '年龄']
for value in arr:
    print(value, '\n')

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(10))

for value in range(10):
    print(value)

index = 0
while index < len(arr):
    print(arr[index])
    index = index + 1


# 空函数
def nothing():
    pass


def check(v):
    if not isinstance(v, (int, float)):
        raise TypeError('类型不匹配')
    if v >= 0:
        return v + 10
    else:
        return -v


# 默认参数
def person(name, address='浙江', school='浙大'):
    print(name)
    print(address)
    print(school)


person('小白')
person('小白', school='南大')


# 可变参数
def init(name, *parameter):
    print(name)
    for v in parameter:
        print(v)


arr = ['google', 'microsoft', 'facebook', 'oracle']
# 将arr作为可变参数
init('公司', *arr)
init('公司', 'A', 'B', 'C')


# 关键字参数
def menu(name, parent, **v):
    print(name)
    print(parent)
    print(v)


dictionary = {'语文': 99, '数学': 78, '外语': 90}
# 将dictionary作为关键字参数
menu('学科', '老师', **dictionary)
menu('学科', '老师', 语文=99, 数学=78, 外语=90)


# 指定命名关键字参数
def reason(name, *, city, distance):
    print(name)
    print(city)
    print(distance)


reason('季节', city='杭州', distance='距离')


# 命名关键字参数默认值
def animal(name, *, city='杭州', distance):
    print(name)
    print(city)
    print(distance)


animal('动物', distance='十万八千里')
animal('动物', city='天堂', distance='未知')


# 参数定义顺序必须是: 必选参数 默认参数 可变参数 命名关键字参数 关键字参数
# 切片功能
# 列表生成器


arr = ['春', '夏', '秋', '冬']
# ['夏', '秋']
print(arr[1:3])
# ['春', '夏', '秋']
print(arr[:3])
# ['秋', '冬']
print(arr[-2:])

arr = list(range(30))
print(arr[0:25:2])

print('这是我的微笑,请好好珍惜'[:6])

dictionary = {'语文': 77, '数学': 90, '外语': 87}
for key in dictionary:
    print(key)
    print(dictionary[key])

for value in dictionary.values():
    print(value)

for key, value in dictionary.items():
    print(key)
    print(value)


arr = [v * v for v in range(2, 12)]
print(arr)


fcount = lambda v: v * 2 + 3
print(fcount(6))

print(list(map(lambda v: v + 2, arr)))
print(list(filter(lambda v: v > 50, arr)))
print(reduce(lambda v, k: v + k, arr))

# 遍历序列
arr = ['春', '夏', '秋', '冬']
for v in arr:
    print(v)

# 倒序遍历序列
arr = ['春', '夏', '秋', '冬']
for v in reversed(arr):
    print(v)

# 遍历2个collection
arr = ['春', '夏', '秋', '冬']
color = ['红', '绿', '黄', '蓝']
for v, k in zip(arr, color):
    print(v, '-', k)

# 遍历3个collection
arr = ['春', '夏', '秋', '冬']
color = ['红', '绿', '黄', '蓝']
sex = ['男', '女', '未知', '不明']
for v, k, s in zip(arr, color, sex):
    print(v, '-', k, '-', s)

# 遍历排序的序列
arr = ['春', '夏', '秋', '冬']
for v in sorted(arr, reverse=True):
    print(v)
for v in sorted(arr):
    print(v)

with open('/Users/promiss/Desktop/others.txt', 'r') as f:
    for line in f.readlines():
        print(line)


# 获取当前日期和时间 2018-12-31 13:50:55.929833
now = datetime.now()
print(now)

# datetime转成timestamp 1546235455.929833
print(now.timestamp())

# timestamp转成datetime
print(datetime.fromtimestamp(1546235455.929833))

# 字符串转成datetime
print(datetime.strptime('2018-12-31 13:50:55', '%Y-%m-%d %H:%M:%S'))

# datetime转成字符串
print(now.strftime('%a, %b %d %H:%M'))


