#! /usr/bin/env python

"""
Semaphore的使用
"""

from threading import Semaphore
import threading
import time


def print_info(sem, index):
    sem.acquire()
    time.sleep(2)
    print(threading.currentThread().getName(), '->', index)
    sem.release()


if __name__ == '__main__':
    sem = Semaphore(3)
    for i in range(20):
        t = threading.Thread(target=print_info, args=(sem, i))
        t.start()

