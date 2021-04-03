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
