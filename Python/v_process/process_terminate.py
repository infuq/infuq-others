#! /usr/bin/env python

"""
结束子进程
"""

import multiprocessing
import time


class MyProcess(multiprocessing.Process):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("PID={}, Name={}".format(multiprocessing.current_process().pid, multiprocessing.current_process().name))
        time.sleep(5)
        print('子进程结束...')


if __name__ == '__main__':

    process = MyProcess('My_0')
    process.start()

    # 主进程等待3秒钟, 如果子进程还存活, 那么结束子进程
    time.sleep(3)
    if process.is_alive():
        process.terminate()

