#! /usr/bin/env python

import time


if __name__ == '__main__':
    #获取年-月-日 2021-03-20
    print(time.strftime('%Y-%m-%d',time.localtime()))
    #获取时:分:秒 23:40:46
    print(time.strftime('%H:%M:%S',time.localtime()))
    #获取年-月-日 时:分:秒
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))


