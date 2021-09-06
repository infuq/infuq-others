#! /usr/bin/env python3.7
# -*- encoding:utf-8 -*-


import requests


# 文件(包括图片等)下载

response = requests.get('https://mmbiz.qpic.cn/mmbiz_png/MOwlO0INfQqPyiatZNzvHTW5LPtW'
                        '2oV8r2EH9PTDhQp2TZDOZpQKTE1ZHxI3eKHvErkibo3Tq1wkGHGgPdC7wYuA/64'
                        '0?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1')
img = response.content

with open('/Users/promiss/Desktop/1101.png', 'wb') as f:
    f.write(img)


if __name__ == '__main__':
    print('x')
