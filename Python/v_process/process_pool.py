#! /usr/bin/env python

"""
进程池
"""


import psutil
import multiprocessing
from concurrent.futures import ProcessPoolExecutor


def worker(index):
    print(index)


if __name__ == '__main__':

    # 进程池
    # pool = ProcessPoolExecutor()

    # 进程池
    pool = multiprocessing.Pool(processes=6)
    result = pool.apply_async(func=worker, args=(3,))

    pool.close()
    pool.join()  # 调用join方法之前必须调用close方法
    result.get()
