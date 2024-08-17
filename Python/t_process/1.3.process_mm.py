#! /usr/bin/env python

"""
进程通信 共享内存
"""

from multiprocessing import Process, Queue, Manager
import time


def add(m_dict, key, value):
    m_dict[key] = value


if __name__ == '__main__':

    m_dict = Manager().dict()

    producer1 = Process(target=add, args=(m_dict, "color", "blue"))
    producer2 = Process(target=add, args=(m_dict, "year", 2021))
    producer1.start()
    producer2.start()

    time.sleep(3)
    print(m_dict)
