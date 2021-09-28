#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


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

