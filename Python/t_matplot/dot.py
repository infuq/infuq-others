#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc("font", family='Microsoft YaHei')


def display():

    # 优惠个数
    couponCnt = ["2", "3", "4", "5"]
    loopCnt = ["4", "8", "16", "32"]
    zh = ["3", "7", "15", "31"]
    cost = ["0", "0", "0", "2"]

    plt.plot(couponCnt, loopCnt, label='循环次数')
    plt.plot(couponCnt, zh, label='组合')
    plt.plot(couponCnt, cost, label='耗时')


    plt.xlabel('优惠数量')
    plt.ylabel('-')
    plt.title("穷举优惠性能测试")

    plt.legend()
    plt.show()


if __name__ == '__main__':
    display()

