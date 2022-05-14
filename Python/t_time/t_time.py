#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


def t():

    print(time.strftime('%Y', time.localtime()))  # 获取完整年份      2022

    print(time.strftime('%y', time.localtime()))  # 获取简写年份      22

    print(time.strftime('%m', time.localtime()))  # 获取月             05

    print(time.strftime('%d', time.localtime()))  # 获取日             12

    print(time.strftime('%Y-%m-%d', time.localtime()))  # 获取年-月-日   2022-05-12

    print(time.strftime('%H', time.localtime()))  # 获取时，24小时制       07

    print(time.strftime('%I', time.localtime()))  # 获取时，12小时制       07

    print(time.strftime('%M', time.localtime()))  # 获取分                 24

    print(time.strftime('%S', time.localtime()))  # 获取秒             11

    print(time.strftime('%H:%M:%S', time.localtime()))  # 获取时:分:秒       07:24:11

    print(time.strftime('%a', time.localtime()))  # 本地简化星期          Thu

    print(time.strftime('%A', time.localtime()))  # 本地完整星期          Thursday

    print(time.strftime('%b', time.localtime()))  # 本地简化月份          May

    print(time.strftime('%B', time.localtime()))  # 本地完整月份          May

    print(time.strftime('%c', time.localtime()))  # 本地日期和时间表示       Thu May 12 07:24:11 2022

    print(time.strftime('%j', time.localtime()))  # 一年中的第几天         132

    print(time.strftime('%p', time.localtime()))  # P.M等价符          AM

    print(time.strftime('%U', time.localtime()))  # 一年中的第几个星期,星期天为星期的开始     19

    print(time.strftime('%w', time.localtime()))  # 星期几,星期天为星期的开始       4

    print(time.strftime('%W', time.localtime()))  # 一年中的第几个星期,星期一为星期的开始     19

    print(time.strftime('%x', time.localtime()))  # 本地日期表示      05/12/22

    print(time.strftime('%X', time.localtime()))  # 本地时间表示      07:24:11

    print(time.strftime('%Z', time.localtime()))  # 当前时区            中国标准时间

    print(time.strftime('%%', time.localtime()))  # 输出%本身           %

    print(time.strftime('%Y-%m-%d %H:%M:%S %w-%Z', time.localtime()))  # 2022-05-12 07:24:11 4-中国标准时间

    n = 3
    print(time.strftime('%Y-%m-%d', time.localtime(time.time() - n * 3600 * 24)))   # 获取前n天时间   2022-05-09

    time.sleep(2)

    print(time.time())          # 1652311671.2421024


# 时间戳转日期
def timestamp2date(timestamp):
    time_local = time.localtime(timestamp / 1000)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    print(dt)


if __name__ == '__main__':
    timestamp2date(1599528585000)

    # 获取年-月-日 2021-03-20
    print(time.strftime('%Y-%m-%d', time.localtime()))
    # 获取时:分:秒 23:40:46
    print(time.strftime('%H:%M:%S', time.localtime()))
    # 获取年-月-日 时:分:秒
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

    t()
