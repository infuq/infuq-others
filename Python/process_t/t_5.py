#! /usr/bin/env python

'''
进程池
'''


import psutil
import multiprocessing


def worker(index):
    print(index)


if __name__ == '__main__':

    pool = multiprocessing.Pool(processes=6)
    for i in range(3):
        result = pool.apply_async(func=worker, args=(i,))




