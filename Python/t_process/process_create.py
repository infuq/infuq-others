#! /usr/bin/env python

"""
创建进程 (面向过程)
"""

import time
import multiprocessing


def worker(index):
    print("PID={}, Name={}".format(multiprocessing.current_process().pid, multiprocessing.current_process().name))
    print("PID={}, Name={}".format(multiprocessing.Process.pid, multiprocessing.Process.name))


if __name__ == '__main__':

    process = multiprocessing.Process(target=worker, args=(3,), name='My_Process')
    process.start()

