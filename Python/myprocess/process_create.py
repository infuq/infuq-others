#! /usr/bin/env python

"""
创建进程 (面向过程)
"""

import multiprocessing


def worker(index):
    print("PID={}, Name={}".format(multiprocessing.current_process().pid, multiprocessing.current_process().name))


if __name__ == '__main__':

    for i in range(3):
        # process = multiprocessing.Process(target=worker, args=(i,), name='My_{}'.format(i))
        process = multiprocessing.Process(target=worker, args=(i,), name='My_%s' % (i))
        process.start()
