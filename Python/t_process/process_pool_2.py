#! /usr/bin/env python

"""
进程池
"""


import psutil
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import time


def worker(index):
    # print(login)
    time.sleep(index)
    return index


if __name__ == '__main__':

    # 进程池
    pool = multiprocessing.Pool(processes=6)

    # 结果顺序与入参顺序一致
    for result in pool.imap(worker, [1, 5, 3]):
        print(result)

    # 谁先执行完谁返回结果
    for result in pool.imap_unordered(worker, [1, 5, 3]):
        print(result)